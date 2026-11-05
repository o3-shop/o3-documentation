# Module versioning

This page describes how O3-Shop modules are branched, versioned and released, so that
Composer installs the right module version for every shop version.

It applies to every module whose code depends on the shop version: payment modules, theme
extensions, anything that extends shop classes or templates. **PayPal Checkout
(`o3-shop/paypal-checkout`) is the first module that follows this convention; the other
O3-Shop modules will move to it step by step.** Third-party module developers are welcome
to follow it too.

## The problem it solves

O3-Shop maintains several release lines at the same time (1.5, 1.6, 1.7 and the upcoming
2.0). A module often needs small differences per shop line: a changed core method, a
template block that moved, a new service. With a single module branch, Composer can't tell
which module version fits which shop, and every fix has to be tested against every shop
line at once.

## The convention

### 1. One release line per shop line

A module has one branch per shop line it supports:

| Shop line | Module branch | Module tags |
|---|---|---|
| O3-Shop 1.5 | `b-1.5` | `v1.5.0`, `v1.5.1`, … |
| O3-Shop 1.6 | `b-1.6` | `v1.6.0`, `v1.6.1`, … |
| O3-Shop 1.7 | `b-1.7` | `v1.7.0`, `v1.7.1`, … |
| O3-Shop 2.0 | `b-2.0` | `v2.0.0`, `v2.0.1`, … |

A line only exists when the module supports that shop line. A module that only works with
1.7 and newer starts with `b-1.7`.

### 2. The version names the shop line

Tags on `b-X.Y` are always `vX.Y.n`. Only the last number counts up independently, for
every module release on that line. Inside a line there are no minor or major bumps: a
change that would need one belongs on the next shop line.

So `paypal-checkout v1.7.4` reads as "the fifth release of PayPal Checkout for O3-Shop 1.7".

### 3. Each line declares its shop version

The `composer.json` on `b-X.Y` requires the matching shop line in `require` (not in
`require-dev`):

```json
{
  "name": "o3-shop/paypal-checkout",
  "require": {
    "o3-shop/shop-ce": "~1.7.0"
  }
}
```

`~1.7.0` allows every 1.7.x shop, release candidates included, but no 1.6 or 1.8 shop.
Composer refuses a module line that doesn't fit the installed shop, and
`composer require o3-shop/paypal-checkout` in a shop project picks the matching line: a
1.6 shop gets `v1.6.n`, a 1.7 shop gets `v1.7.n`.

The O3-Shop metapackage keeps pinning each module to the exact version it shipped with
(`"o3-shop/paypal-checkout": "v1.7.4"`), so every shop release records exactly which
module versions belong to it. The release tooling updates those pins.

### 4. Fixes go into the oldest affected line and are merged forward

A bug that exists in 1.6 and 1.7 is fixed on `b-1.6` first. The fix is then merged forward
`b-1.6` → `b-1.7` → `b-2.0`, never cherry-picked backwards. Every line keeps the history of
the lines before it, and nothing fixed in an older line gets lost in a newer one.

When merging forward, the target line always keeps its own shop constraint in
`composer.json` and its own `version` in `metadata.php`. Resolve those conflicts in favour
of the target line. Line branches are protected, so a forward merge goes through a pull
request that is merged with a merge commit (never squash or rebase, which would lose the
link between the lines). A forward merge is a new commit on the target line, so its next
release cuts a new patch tag.

New features go into the newest line they make sense for. Backport them only when there
is a real need.

### 5. `main` follows the newest line

`main` points at the newest released line and is the repository's default branch, so
anyone who clones the module or browses it on GitHub sees the current version.

- `main` is protected and never committed to directly.
- After a final shop release, the release tooling opens a merge-back pull request into
  `main` for every repository it tagged (branch `merge-back-<tag>`, titled after the shop
  release: `Merge v1.7.3 release into main`). For the **newest** line, merge it with a
  merge commit, so the release tag becomes part of `main`'s history.
- For an **older** line, close the merge-back pull request without merging and delete its
  `merge-back-<tag>` branch: `main` must not move back to an older shop line. Don't leave
  it open, because an open merge-back pull request blocks the next release.
- When a new shop line ships (for example 2.0), `main` moves on to `b-2.0`.

Pull requests target the line they fix (`b-1.6`, `b-1.7`, …), not `main`.

### 6. Shop-independent libraries keep a single line

Packages that don't depend on the shop, such as `o3-shop/paypal-client` (a plain client
for the PayPal REST API), keep one release line with their own semantic version and no
`o3-shop/shop-ce` requirement.

## Releasing a line-versioned module

O3-Shop releases are cut with `bin/release` (see [How to Contribute](./HowToContribute.md),
Phase 5). Line-versioned modules are supported by the release tooling from
[shop-ce#265](https://github.com/o3-shop/shop-ce/pull/265):

- The module is listed in `ReleaseLine::LINE_VERSIONED_PACKAGES`
  (`source/Internal/ReleaseTooling/Version/ReleaseLine.php` in shop-ce).
- `DefaultBranchResolver::PACKAGE_TO_BRANCH` maps it, by hand, to the same `b-X.Y` as
  `o3-shop/shop-ce`. The map holds one branch per package, so releasing an older shop line
  means switching the map for that release, as for the shop repositories themselves.
- On `b-X.Y` the tool only looks at `vX.Y.*` tags to find the latest release and refuses
  any new tag that is outside the line or not above the line's latest tag. A listed module
  mapped to a branch not named `b-X.Y`, `main` included, stops the plan with an error. The tool
  does not check that X.Y matches the shop version being released; the map has to be right.
- A line's first tag needs an exact bump, for example
  `bin/release --from v1.7.2 --to v1.7.3 --bump paypal-checkout=v1.7.0`. After that, the
  default patch bump continues the line. A `.next-bump` file with `minor` or `major` on a
  line branch stops the plan; delete it.
- The tool cuts final module tags, also during a shop release candidate. A module
  pre-release (`v1.7.0-RC1`) needs an exact bump, and so does the final that follows it
  (`--bump <module>=v1.7.0`): a patch bump from `v1.7.0-RC1` would give `v1.7.1`.

The tool does not check the `composer.json` constraint from rule 3, and it does not update
the `version` in the module's `metadata.php` (it only does that for theme files). Bump
`metadata.php` to the upcoming tag in a pull request on the line before each release.

## Moving a module onto the convention

1. Create `b-X.Y` for the current shop line from the module's present release branch.
2. On `b-X.Y`, move `o3-shop/shop-ce` from `require-dev` (if it is there) to `require` as
   `~X.Y.0`, and set the `version` in `metadata.php` to the first tag. For a fork that still
   carries its upstream version (PayPal Checkout's `metadata.php` says `2.10.3`), the admin
   then shows a lower number (`1.7.0`); that is expected.
3. Add the module to `ReleaseLine::LINE_VERSIONED_PACKAGES` and map it in
   `DefaultBranchResolver` to `b-X.Y`.
4. Cut its first tag with an exact bump (`--bump <module>=vX.Y.0`).
5. Create the older lines the module needs, each from the next newer line plus the
   changes for its shop version (for example `b-1.6` from `b-1.7`), with its constraint.
   Then record the new line as already merged into the newer one
   (`git switch b-1.7 && git merge -s ours b-1.6`, through a pull request merged with a
   merge commit), so the first real forward merge doesn't carry the 1.6-specific changes
   into 1.7. `bin/release` only reaches modules the shop line's metapackage requires: an
   older line gets its first tag in a release of that shop line, after the module has been
   added to that line's metapackage (a product decision per line) and the map switched.
6. Point `main` at the newest line, make it the default branch, protect it, and keep
   *Automatically delete head branches* off (the release tooling checks this).

## Status

| Module | Status |
|---|---|
| PayPal Checkout (`o3-shop/paypal-checkout`) | First module on the convention. Still released from its single `b-1.0` line (`v1.0.x`, default branch `b-1.0`); moving to `b-1.7`, then the other lines ([o3-shop/o3-shop#274](https://github.com/o3-shop/o3-shop/issues/274)). Shop 1.5 ships the classic PayPal module instead (package `o3-shop/paypal-module`, a different package), and the 1.6 metapackage doesn't include PayPal Checkout yet. |
| Other O3-Shop modules | Will follow. |
