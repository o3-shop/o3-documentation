#!/usr/bin/env python3
"""Generate source/WhatsChanged.md from GitHub releases.

Reads tools/repos.txt for an "anchor:" line plus the list of repos under
ORG. Resolves the anchor release's publish date, then fetches every
release from every repo dated on or after the *start* of that day (UTC),
excluding releases whose tag matches the anchor tag exactly. Coordinated
releases that share a tag across repos within a short window are grouped
into one section.

Stdlib only. Reads GH_TOKEN/GITHUB_TOKEN if set (recommended locally;
unauthenticated quota is enough for the small repo list on RTD).
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ORG = "o3-shop"
PER_PAGE = 100
ROOT = Path(__file__).resolve().parent.parent
REPO_LIST = ROOT / "tools" / "repos.txt"
OUTPUT = ROOT / "source" / "WhatsChanged.md"

ISO = "%Y-%m-%dT%H:%M:%SZ"
FULL_CHANGELOG_RE = re.compile(
    r"\*\*Full Changelog\*\*:\s*\S+", re.IGNORECASE
)
RC_SUFFIX_RE = re.compile(r"-RC\d*$", re.IGNORECASE)

# Linkification — turn bare URLs and @-mentions into clickable, new-window
# links. PR URLs are shortened to "<repo>#<num>"; other URLs keep their full
# text. Lookbehinds avoid matching inside an existing markdown/HTML link.
PR_URL_RE = re.compile(
    r"(?<![\(\[\<\"\=])https://github\.com/([^/\s]+)/([^/\s]+)/pull/(\d+)"
)
URL_RE = re.compile(r"(?<![\(\[\<\"\=])https?://[^\s<>)]+")
USER_RE = re.compile(r"(?<![\w/@])@([A-Za-z0-9](?:[A-Za-z0-9-]{0,38})?)")


def canonical_tag(tag: str) -> str:
    """Strip a trailing ``-RC<n>`` so all release-candidate tags map to their
    final tag (e.g. ``v1.6.0-RC4`` and ``v1.6.0-RC1`` both become ``v1.6.0``)."""
    return RC_SUFFIX_RE.sub("", tag)


def _anchor(href: str, text: str) -> str:
    return f'<a target="_blank" rel="noopener" href="{href}">{text}</a>'


def linkify(text: str) -> str:
    """Turn bare URLs and @-mentions in a release body into HTML anchors that
    open in a new window."""
    text = PR_URL_RE.sub(
        lambda m: _anchor(m.group(0), f"{m.group(2)}#{m.group(3)}"),
        text,
    )
    text = URL_RE.sub(lambda m: _anchor(m.group(0), m.group(0)), text)
    text = USER_RE.sub(
        lambda m: _anchor(f"https://github.com/{m.group(1)}", f"@{m.group(1)}"),
        text,
    )
    return text


def read_target_version() -> str:
    """Pick up the release string from source/conf.py so the page title
    tracks the documented version automatically."""
    conf = (ROOT / "source" / "conf.py").read_text()
    m = re.search(r"^\s*release\s*=\s*['\"]([^'\"]+)['\"]", conf, re.MULTILINE)
    if not m:
        raise SystemExit("Could not find 'release = ...' in source/conf.py")
    return m.group(1)


def parse_repos_file() -> tuple[str, str, list[str]]:
    """Return (anchor_repo, anchor_tag, [repo, ...])."""
    anchor_repo = anchor_tag = None
    repos: list[str] = []
    for raw in REPO_LIST.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("anchor:"):
            value = line.split(":", 1)[1].strip()
            if "@" not in value:
                raise SystemExit(
                    f"Bad anchor line: {raw!r} (expected 'anchor: repo@tag')"
                )
            anchor_repo, anchor_tag = value.split("@", 1)
            continue
        repos.append(line)
    if not anchor_repo or not anchor_tag:
        raise SystemExit("tools/repos.txt is missing an 'anchor: repo@tag' line.")
    if anchor_repo not in repos:
        repos.insert(0, anchor_repo)
    return anchor_repo, anchor_tag, repos


def gh_get(path: str) -> dict | list:
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "o3-shop-docs-fetch_releases",
        },
    )
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_anchor_published_at(anchor_repo: str, anchor_tag: str) -> datetime:
    data = gh_get(f"/repos/{ORG}/{anchor_repo}/releases/tags/{anchor_tag}")
    if not isinstance(data, dict) or "published_at" not in data:
        raise SystemExit(f"Could not resolve anchor {anchor_repo}@{anchor_tag}")
    return datetime.strptime(data["published_at"], ISO).replace(tzinfo=timezone.utc)


def fetch_releases(repo: str) -> list[dict]:
    data = gh_get(f"/repos/{ORG}/{repo}/releases?per_page={PER_PAGE}")
    return data if isinstance(data, list) else []


def parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    return datetime.strptime(s, ISO).replace(tzinfo=timezone.utc)


def strip_full_changelog(body: str) -> str:
    """Drop the GitHub-generated ``**Full Changelog**: …`` footer from a body."""
    return FULL_CHANGELOG_RE.sub("", body or "").strip()


REDUNDANT_BODY_HEADINGS = {"what's changed", "whats changed", "changes"}


def normalize_body(body: str) -> str:
    """Drop boilerplate ``## What's Changed`` headers and flatten any
    remaining headings to bold paragraphs so they don't pollute the
    sidebar TOC."""
    out_lines: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if m:
            text = m.group(2).strip().lower().rstrip(":")
            if text in REDUNDANT_BODY_HEADINGS:
                continue
            if out_lines and out_lines[-1] != "":
                out_lines.append("")
            out_lines.append(f"**{m.group(2)}**")
            out_lines.append("")
        else:
            out_lines.append(line)
    cleaned = "\n".join(out_lines)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def merge_repo_bodies(releases: list[dict]) -> str:
    """Concatenate every release body for one repo, in newest-first order,
    deduping identical lines (so a bullet that appears in both RC1 and RC4
    shows up once)."""
    releases = sorted(releases, key=lambda r: r["published_at"], reverse=True)
    seen: set[str] = set()
    kept: list[str] = []
    for rel in releases:
        cleaned = strip_full_changelog(rel.get("body") or "")
        cleaned = normalize_body(cleaned)
        cleaned = linkify(cleaned)
        for line in cleaned.splitlines():
            norm = line.strip()
            if not norm:
                if kept and kept[-1] != "":
                    kept.append("")
                continue
            if norm in seen:
                continue
            seen.add(norm)
            kept.append(line)
    return "\n".join(kept).strip()


def render(
    target_version: str,
    anchor_repo: str,
    anchor_tag: str,
    anchor_dt: datetime,
    releases_by_repo: dict[str, list[dict]],
    repo_order: list[str],
) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    anchor_display = anchor_tag.lstrip("vV")
    anchor_link = _anchor(
        f"https://github.com/{ORG}/{anchor_repo}/releases/tag/{anchor_tag}",
        f"<code>{anchor_repo} {anchor_tag}</code>",
    )
    out: list[str] = [
        "<!-- AUTO-GENERATED by tools/fetch_releases.py. "
        "Edit the script or tools/repos.txt; do not hand-edit this file. -->",
        "",
        f"# Changes from {anchor_display} to {target_version}",
        "",
        f"_Aggregated from releases across the o3-shop GitHub organisation since "
        f"{anchor_link} ({anchor_dt.strftime('%Y-%m-%d')}). "
        f"Last updated: {now}._",
        "",
    ]

    rendered_any = False
    for repo in repo_order:
        releases = releases_by_repo.get(repo) or []
        if not releases:
            continue
        block = merge_repo_bodies(releases)
        if not block:
            continue
        latest_tag = max(releases, key=lambda r: r["published_at"])["tag_name"]
        version_label = canonical_tag(latest_tag)
        out.append(f"## {repo} ({version_label})")
        out.append("")
        out.append(block)
        out.append("")
        rendered_any = True

    if not rendered_any:
        out.append("_No changes since the anchor — check back after the next release._")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    anchor_repo, anchor_tag, repos = parse_repos_file()
    target_version = read_target_version()
    print(
        f"fetch_releases: target {target_version}, anchor {anchor_repo}@{anchor_tag}",
        file=sys.stderr,
    )

    try:
        anchor_dt = fetch_anchor_published_at(anchor_repo, anchor_tag)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        print(f"fetch_releases: cannot resolve anchor ({e}); aborting.", file=sys.stderr)
        return 0
    cutoff = anchor_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    print(f"  anchor day cutoff: {cutoff.isoformat()}", file=sys.stderr)

    releases_by_repo: dict[str, list[dict]] = {}
    successes = 0
    for repo in repos:
        try:
            releases = fetch_releases(repo)
            successes += 1
            kept = [
                rel
                for rel in releases
                if (ts := parse_dt(rel.get("published_at"))) is not None
                and ts >= cutoff
                and rel.get("tag_name") != anchor_tag
            ]
            if kept:
                releases_by_repo[repo] = kept
            print(
                f"  {repo}: {len(releases)} fetched, {len(kept)} after cutoff",
                file=sys.stderr,
            )
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            print(f"  {repo}: FAILED ({e})", file=sys.stderr)

    if successes == 0:
        print(
            f"fetch_releases: no repos reachable; leaving "
            f"{OUTPUT.relative_to(ROOT)} unchanged.",
            file=sys.stderr,
        )
        return 0

    OUTPUT.write_text(
        render(target_version, anchor_repo, anchor_tag, anchor_dt, releases_by_repo, repos)
    )
    print(
        f"fetch_releases: wrote {OUTPUT.relative_to(ROOT)} "
        f"({len(releases_by_repo)} repo(s))",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
