# O3-Shop documentation

These are the sources for the generated documentation at [https://docs.o3-shop.com](https://docs.o3-shop.com).

## Contribute

If you have a suggestion for improvement, create a fork of the repository and create a pull request. Alternatively, you can simply create an issue. Add the project to your favourites. Thank you.

- Create a fork of the project
- Create a feature branch (git checkout -b feature/AmazingFeature).
- Add your changes (git commit -m 'Add some AmazingFeature').
- commit the branch (git push origin feature/AmazingFeature)
- Open a pull request

## Local development

For development purposes, the documentation can be created locally. This saves unnecessary correction runs.

Assuming you have Python already, install Sphinx:

```
pip install sphinx
pip install myst-parser
pip install sphinx-rtd-theme
```

Check out the fork and change to the root directory. 

Now, edit your desired files or add new content. Orientate the document structure on the existing elements.

Execute this command to start the build:

```
make html
```

You will find the generated project in the folder `build/html`.

If you are satisfied with your adjustments, transfer them to us as a merge request.

Many thanks for your contribution.

## Release notes page

The "What's Changed" page (`source/WhatsChanged.md`) is auto-generated from GitHub releases across the o3-shop organisation by `tools/fetch_releases.py`. Read the Docs runs the script on every build (via `.readthedocs.yaml`), so the published page always reflects the latest releases — there is nothing to commit by hand.

What controls the page:

- `tools/repos.txt` — the repo list and the anchor.
  - The `anchor: <repo>@<tag>` line pins the start of the release window. Every release on or after that anchor's publish day is collected; releases whose tag exactly matches the anchor are excluded.
  - One repo name per line below the anchor. Order is preserved in the rendered page (top of file = first section).
- `source/conf.py` — the `release` value is used as the target version in the page title (`Changes from <anchor> to <release>`).

### When cutting a new release

Worked example: cutting **1.6.1** (previous release was **1.6.0**).

1. **`source/conf.py` — bump `release` to the new full version.**
   - Set `release = '1.6.1'` (the full version; appears as the target in the page title).
   - Leave `version` (the short `X.Y`, e.g. `'1.6'`) unchanged for a patch release. Only bump it when the minor line changes (e.g. `'1.6'` → `'1.7'`).

2. **`tools/repos.txt` — set `anchor:` to the *previous* release's shop-ce tag.**
   - Cutting 1.6.1 → `anchor: shop-ce@v1.6.0`. Always use the `v`-prefixed tag exactly as it appears on GitHub.
   - The page then collects every listed repo's releases published on or after that tag's day, excluding releases that share the anchor tag itself. That yields a clean "1.6.0 → 1.6.1" window.

3. **Composer constraint in `source/User/Installation/NewInstallation.md` — usually leave it.**
   - The command pins `~1.6.0`, a tilde range that already resolves to the latest `1.6.x` (including `1.6.1`), so it does **not** need a bump for patch releases.
   - Only update it when the minor line changes — e.g. for the 1.7 line it becomes `~1.7.0`.

4. **Regenerate and preview the page locally** (see below), then sanity-check the new title and per-repo sections in `source/WhatsChanged.md`.

5. **Open a pull request** with the `conf.py` + `repos.txt` (and regenerated `WhatsChanged.md`) changes. Once merged, Read the Docs rebuilds and the page refreshes automatically.

> Note: `WhatsChanged.md` is regenerated on every Read the Docs build, so committing it is optional — but committing the regenerated copy keeps the repo in sync and makes the release diff reviewable.

### Previewing locally

```sh
GH_TOKEN=$(gh auth token) python3 tools/fetch_releases.py
make html
```

`GH_TOKEN` is optional but recommended — it lifts the unauthenticated GitHub rate limit. If GitHub is unreachable the script leaves the committed copy untouched, so the build still succeeds.
