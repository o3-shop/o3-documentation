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

1. Bump `version` and `release` in `source/conf.py`.
2. Update the `anchor:` line in `tools/repos.txt` to the previous release's tag.
3. Update any version references in the documentation itself (e.g. the Composer command in `source/User/Installation/NewInstallation.md`).
4. Open a pull request. Once merged, Read the Docs rebuilds and the page refreshes automatically.

### Previewing locally

```sh
GH_TOKEN=$(gh auth token) python3 tools/fetch_releases.py
make html
```

`GH_TOKEN` is optional but recommended — it lifts the unauthenticated GitHub rate limit. If GitHub is unreachable the script leaves the committed copy untouched, so the build still succeeds.
