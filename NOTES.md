# Cluster and Python Workshop Notes 27-09-2024
## Morning: using the cluster (online)
* Nodes are like computers
* Processes are the number of cores in the computers
```
$ srun —cpus-per-task=16 —pty bash
$ nproc
16
```
## Afternoon: Python packaging
* Good practice: to install new package, add it to the YAML and reinstall the environment from the YAML file ```micromamba create -f env.yaml```.
* Using `pyproject.toml` is the new standard for publishing. It doesn't need extra packages (`setuptools`) like `setup.py` does. Most people use `pyproject.toml` now.
* [GithHub Actions](https://docs.github.com/en/actions) is good for publishing to PyPi
* PyOpenSci provides guidance for publishing
    * Hatch can generate a lot of the stuff for you
    * Also has a functionality to migrate your `setup.py` files to `pyproject.toml`
* Use `.github` folder to build and test package and deploy to pypi
#### Licensing
* Use [choosealicense.com](choosealicense.com) for guidance
* Tom recommends MIT for permissive licensing –others can modify without telling you use in products that they subsequently profit from
* GPL license is a bit stricter
#### Documentation 
* NISMOD example: [east-africa-transport.readthedocs.io](east-africa-transport.readthedocs.io)
* Use [Sphinx](https://www.sphinx-doc.org/en/master/) to create docs

```
$ mkdir docs
$ cd docs
$ sphinx-quickstart
$ y
$ Mandelbrot
$ Alison Peard
$ 0.0.1
$ make html
$ cd build/html
$ open index.html # to view in browser
```
To edit, just edit `index.rst` and rerun `make html`.

Now we want to automatically import our docstrings. In `conf.py` under general configuration add to the extensions option
```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]
```
Make a new file `api.rst` and save it in `docs/source` . Fill it with the contents shown and, to `index.rst`, add `api` under `.. toctree::`.

* To display file trees:
```
$ brew install tree
$ tree
```
* Can deploy to GitHub packages using YAML file in `.github` folder
#### Debugging
* Add breakpoints by clicking on the line number
* In VS Code, click the drop-down arrow by Run and select "Python Debugger: debug Pythonfile"
* In `DEBUG CONSOLE` you can interact with the script and intermediate variables
#### Testing
* Tests are also a nice way of having example code for your package
* Add pytest and pytest-cov to the YAML and reinstall
* Create `test_mandelbrot.py` and run `python -m pytest`
* Tip from Fred: once your code is working, run it once and output a numpy file for testing later, then use that to keep testing
* Should have enough tests to be sure your code is doing what you want it to, so then you can modify more freely
* To check coverage of tests: `python -m pytest --cov-report=term-missing --cov`
* make a `.github` folder in home of repo and add `build.yaml`
    * code builds, checks linting, and runs pytest --if it works you get a green tick on your GitHub repo
    * Look at GitHub Actions docs