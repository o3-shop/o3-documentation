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
