# How to Contribute

Welcome, developer! This guide covers everything you need to contribute to O3-Shop — from opening your first issue through to a published release.

## Why contribute?

- Help improve O3 for everyone
- Learn from a community of experienced developers
- Influence the direction of the project
- Build your open-source portfolio

## Knowledge you should have before contributing

### If you want to contribute with code

- **PHP:** Good knowledge of PHP 7.4 up to the latest version used in O3
- **O3 Modules:** Profound experience in writing modules for O3 or its predecessor
- **Docker:** Secure handling and understanding of Docker containers
- **Unit Testing:** Ability to write and run unit tests using PHPUnit

### If you want to contribute to the documentation

- **Documentation Writing:** Understanding of how to write clear, concise, and helpful documentation
- **Sphinx/Markdown:** Familiarity with Sphinx and Markdown is a plus

## Roles

The workflow is built around clearly defined roles. A single person can assume multiple roles at different stages of the same issue. For example, a developer who discovers a bug may first act as a Reporter when opening the issue, then later transition into the Developer role when implementing the fix.

| Role | Responsibility |
|------|----------------|
| Reporter | Opens the issue in the central repository |
| Product Owner (PO) | Triages, categorizes, and assigns issues to a milestone |
| Developer | Assigns the ticket, creates a branch, and implements the fix or feature |
| Reviewer | Reviews the pull request, verifies correctness, and provides feedback |
| Approver | Gives final approval and merges the pull request |
| Release Manager | Coordinates the release, tags the version, and publishes the changelog |

## Workflow

### Phase 1: Issue Reporting

#### Step 1 — Open an Issue (Role: Reporter)

Every piece of work — whether it is a bug report, a feature request, or a task — must begin with an issue. Even if you intend to fix the problem yourself, always open an issue first. Issues are always created in the central repository:

👉 [https://github.com/o3-shop/o3-shop/issues](https://github.com/o3-shop/o3-shop/issues)

- **Choose an issue with no assignee.** If the issue already has an assignee, ask in the comments whether you can work on it and check if it is already in progress.
- Do not start any development work before an issue exists. This ensures full traceability and allows the team to coordinate effectively.

### Phase 2: Triage & Planning

#### Step 2 — Triage the Issue (Role: Product Owner)

The Product Owner reviews all incoming issues, verifies their validity, categorizes them (e.g., bug, enhancement, documentation), and assigns them to a milestone. This step ensures that only properly scoped and prioritized work enters the development pipeline.

### Phase 3: Development

#### Step 3 — Assign to the Correct Repository (Role: Developer)

Once an issue has been triaged and assigned to a milestone, the responsible developer assigns it to the appropriate sub-repository within the [o3-shop GitHub organization](https://github.com/o3-shop) where the actual code change will take place.

#### Step 4 — Fork the Repository and Create a Branch (Role: Developer)

Fork the relevant O3 repository to your own GitHub account and create a dedicated feature branch for the issue. Branch names should follow the project's naming conventions:

- Bug fixes: `fix/issue-123-short-description`
- New features: `feature/issue-456-short-description`

#### Step 5 — Set Up Your Development Environment (Role: Developer)

Clone your fork locally. In your project directory, run:

```sh
./docker.sh start
```

This command will start the development environment using Docker. For a detailed walkthrough of the full setup process, refer to the README in the main shop repository:

👉 [https://github.com/o3-shop/shop-ce/blob/b-1.6/README.md](https://github.com/o3-shop/shop-ce/blob/b-1.6/README.md)

#### Step 6 — Implement the Change (Role: Developer)

Write your code or documentation following the project's coding standards and documentation guidelines. Keep your commits focused and your commit messages descriptive. Refer to the issue number in your commits where appropriate.

Ensure your changes are covered by unit tests (for code contributions).

**Signalling a version bump.** If you are working in a leaf package (a theme, demo data, a bundled module, or an asset/tooling package) and your change warrants more than a patch bump, record that intent so it survives until release time: commit a file named `.next-bump` at the repository root, containing a single line with `minor`, `major`, or an exact version such as `v2.0.0`. The release tooling reads it when the next release is cut (see Step 12) and then deletes it automatically, so it applies exactly once. You do not need this for `shop-ce` itself — it is always versioned in lockstep with the shop release.

#### Step 7 — Run Tests and Code Style Checks (Role: Developer)

In your project directory, run:

```sh
./docker.sh test-all
```

This command will run all tests and the PHP code fixer to ensure your code meets project standards.

#### Step 8 — Open a Pull Request (Role: Developer)

Once the implementation is complete and all tests pass, open a pull request (PR) against the target branch. The PR description should:

- Reference the original issue (e.g., `Fixes #123`)
- Summarize the changes made
- Include any relevant testing notes

### Phase 4: Review & Merge

#### Step 9 — Review the Pull Request (Role: Reviewer)

The Reviewer examines the code for correctness, quality, and adherence to project standards. They also verify that the implementation actually addresses the requirements described in the original issue. The Reviewer provides constructive feedback and requests changes if necessary. The Developer addresses the feedback and updates the PR accordingly.

#### Step 10 — Approve and Merge (Role: Approver)

Once the Reviewer is satisfied, the Approver gives final sign-off and merges the pull request into the target branch. The Approver is responsible for ensuring that no unresolved review comments remain before merging.

### Phase 5: Release

#### Step 11 — Verify the Milestone (Role: Release Manager)

Before starting a release, confirm that all issues assigned to the milestone are either resolved and merged, or explicitly deferred to a future milestone. No open or in-progress issues should remain on the milestone being released.

The milestone overview can be found here:
👉 [https://github.com/o3-shop/o3-shop/milestones](https://github.com/o3-shop/o3-shop/milestones)

#### Step 12 — Cut the Release with `bin/release` (Role: Release Manager)

O3-Shop is not a single repository — a release moves the whole package network together (`o3-shop` → `shop-metapackage-ce` → `shop-ce` → leaf packages such as themes, demo data, and bundled modules). You do **not** edit `composer.json` version pins or create tags by hand. The `bin/release` CLI shipped in `shop-ce` orchestrates the entire cut.

The version number follows [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`, and every tag is prefixed with `v` (e.g., `v1.6.0`). There is no version constant to edit in the code — the shop resolves its own version at runtime from the installed Composer package.

**Before you run it**, make sure every release-eligible repository is cloned as a sibling of your `shop-ce` checkout, and that each one:

- is on its release branch (e.g., `b-1.6`),
- has a clean working tree,
- has a green test suite, and
- has no unmerged merge-back PR left over from the previous release.

`bin/release` enforces all of these with pre-flight gates and aborts with a clear diagnostic if any repo fails.

**Bump levels.** Leaf packages are bumped by one patch level by default. To request a larger bump for a leaf, either commit a `.next-bump` file (containing `minor`, `major`, or an exact `vX.Y.Z`) at that repository's root on the release branch, or pass `--bump <repo>=<level>` on the command line — the flag wins over the file, and a consumed `.next-bump` file is deleted automatically in the tag commit. `shop-ce` and `shop-metapackage-ce` are always tagged at the `--to` version, since they move in lockstep with the shop release.

**Preview first.** `--dry-run` prints the full plan — which tags get cut and which constraints get rewritten — without changing anything:

```sh
bin/release --from v1.6.0 --to v1.6.1 --dry-run
```

`--from` is the previous shop release tag; `--to` is the version you are cutting (release-candidate tags such as `v1.6.1-RC1` are supported).

**Run it live** once the plan looks right:

```sh
bin/release --from v1.6.0 --to v1.6.1
```

In live mode the tool walks the repositories in dependency order (leaves first) and, for each repo that changed since `--from`:

- rewrites its `composer.json` dependency constraints and commits + pushes them to the release branch,
- cuts and pushes the new `v`-prefixed tag,
- creates a **draft** GitHub release with auto-generated notes, and
- for final releases (not release candidates), opens a merge-back PR from the release branch into `main`.

`bin/release` deliberately stops short of publishing. It prints a finish checklist of the draft releases to publish and the merge-back PRs to merge — you complete those in Step 14.

#### Step 13 — Update the Documentation (Role: Release Manager)

Update the O3-Shop documentation to reflect the new release:

1. Update the version numbers in `source/conf.py`:
   - Set `version` to the short `MAJOR.MINOR` version (e.g., `1.6`)
   - Set `release` to the full version string (e.g., `1.6.0`)

2. Review all installation instructions (e.g., `source/User/Installation/NewInstallation.md`) and update any version constraints referenced in Composer commands to reflect the new release.

3. Build and verify the documentation locally before publishing:
   ```sh
   sphinx-build -b html source build/html
   ```
   Or using the Makefile:
   ```sh
   make html
   ```

4. Commit and push the documentation changes to the documentation repository:
   👉 [https://github.com/o3-shop/o3-documentation](https://github.com/o3-shop/o3-documentation)

   Open a pull request targeting the `main` branch. Once merged, the updated documentation will be published automatically via Read the Docs at:
   👉 [https://docs.o3-shop.com](https://docs.o3-shop.com)

#### Step 14 — Publish the Release (Role: Release Manager)

`bin/release` (Step 12) cut every tag and created the GitHub releases as **drafts**, leaving the merge-back PRs **open** so that a human makes the final call. Work through the finish checklist printed at the end of the live run:

1. Open each draft release on GitHub, review the auto-generated notes and the release title (e.g., `O3-Shop v1.6.0`), and click **Publish release**.
2. Review and merge each merge-back PR (release branch → `main`). These appear only for final releases, not for release candidates.

The releases page for the main project is located at:
👉 [https://github.com/o3-shop/o3-shop/releases](https://github.com/o3-shop/o3-shop/releases)

#### Step 15 — Close the Milestone (Role: Release Manager)

Once the release tag has been published, close the corresponding milestone in the central issue tracker:
👉 [https://github.com/o3-shop/o3-shop/milestones](https://github.com/o3-shop/o3-shop/milestones)

Any issues that were deferred should have already been moved to a future milestone in Step 11.

#### Step 16 — Communicate the Release (Role: Release Manager)

Announce the new release to the community. This typically includes:

- An update to any social channels or community spaces used by the project

## Quick Reference

| Phase | Step | Role |
|-------|------|------|
| Issue Reporting | 1. Open an issue | Reporter |
| Triage & Planning | 2. Triage the issue | Product Owner |
| Development | 3. Assign to repository | Developer |
| Development | 4. Fork and create a branch | Developer |
| Development | 5. Set up dev environment | Developer |
| Development | 6. Implement the change | Developer |
| Development | 7. Run tests | Developer |
| Development | 8. Open a pull request | Developer |
| Review & Merge | 9. Review the pull request | Reviewer |
| Review & Merge | 10. Approve and merge | Approver |
| Release | 11. Verify the milestone | Release Manager |
| Release | 12. Cut the release with `bin/release` | Release Manager |
| Release | 13. Update the documentation | Release Manager |
| Release | 14. Publish the release | Release Manager |
| Release | 15. Close the milestone | Release Manager |
| Release | 16. Communicate the release | Release Manager |

---

## GitHub Organization and Issue Tracker

- **GitHub Organization:** [https://github.com/o3-shop](https://github.com/o3-shop)
- **Central Issue Tracker:** [https://github.com/o3-shop/o3-shop/issues](https://github.com/o3-shop/o3-shop/issues)

All issues for O3 projects — regardless of which repository they concern — should be created in the central [o3-shop/o3-shop issue tracker](https://github.com/o3-shop/o3-shop/issues) using the issue form. **Always specify the relevant repository in the form when submitting an issue.**

This helps maintainers quickly route and address your contribution or report. Automation may be used to triage or label issues based on your selection.