---
layout: default
title: Understand Python dependencies
permalink: /dependencies
---

## Managing Python dependencies

Python dependency management is a serious topic, as you want to:

- reproduce code behaviour on your computer;
- let other users (and your favourite teacher) reproduce that behaviour on their computer.

During your classes (and future professional life), your most common need will be to import libraries which are not installed by default, often on computers where you do not have administrator rights.

### The `import` instruction

The `import` instruction allows you to access code located in separated files (_modules_). A bundled arborescence of modules is called a _package_.

When you type `import foo`, the Python interpreter will look for:

- a file called `foo.py`, or
- a folder called `foo/` with a file called `__init__.py` inside.

It will look in order in the directories listed in `sys.path`.

Try running in your Python interpreter:

```python
>>> import sys
>>> sys.path
[
    '',
    '/usr/lib/python312.zip',
    '/usr/lib/python3.12',
    '/usr/lib/python3.12/lib-dynload',
    '/home/xo/.local/lib/python3.12/site-packages',
    '/usr/local/lib/python3.12/dist-packages',
    '/usr/lib/python3/dist-packages'
]
```

This is just an example with the default Python interpreter shipped with Ubuntu, and the result will probably be different for you. What is important here is the order of import resolution:

- first look at the current directory;
- directories set in the `PYTHONPATH` environment variable come next;
- then look in the system folders;
- finally, perhaps in a private home folder with no required administrator rights.

<div class="alert alert-warning">
<b>Warning</b> &nbsp;&nbsp; When external dynamic libraries (mostly written in C or C++) need to be loaded, other folders are watched, depending on your operating system. The <code>LD_LIBRARY_PATH</code> variable lets you extend the list of folders to check.
</div>

### Managing dependencies with `pip`

`pip` is the standard Python package installer. It downloads packages and their Python dependencies from [PyPI](https://pypi.org/), or installs a package from a local folder, for example with `pip install .`.

Installing packages directly into the Python provided by your operating system, or with `pip install --user`, is inconvenient: packages for unrelated projects can conflict and it is difficult to reproduce a working installation later. A virtual environment avoids that problem by keeping each project's Python packages separate.

### Managing the course environment with `uv`

[`uv`](https://docs.astral.sh/uv/) manages Python versions, virtual environments and packages. For this course, the project configuration is in `pyproject.toml` and the exact resolved dependency versions are recorded in `uv.lock`.

After cloning the repository, create or update the environment from its lockfile:

```sh
uv sync --locked
```

This creates a virtual environment in `.venv`. The `--locked` option ensures that everyone uses the versions recorded for the course rather than silently choosing newer ones.

You usually do not need to activate this environment. Prefix a command with `uv run` instead:

```sh
uv run python my_test_file.py
uv run jupyter notebook
```

In Visual Studio Code, select the interpreter located in `.venv` when prompted. The Jupyter extension will then use the same packages as the terminal.

If you maintain your own project, use `uv add` to add a dependency. It updates both `pyproject.toml` and `uv.lock`:

```sh
uv add pandas
```

Do not use `uv add` in this course repository unless you intend to change its shared environment.

## Appendix: Conda, Mamba and Pixi

Older versions of this course used the Conda ecosystem. These tools remain useful references, especially for projects that depend on non-Python system libraries, but they are not required for this course.

### Conda and Mamba

[Anaconda](https://www.anaconda.com/) is a Python distribution, and `conda` manages environments and packages from channels such as `conda-forge`. For example:

```sh
conda install pandas
```

`mamba` is a faster compatible implementation of Conda's dependency solver:

```sh
conda install -c conda-forge -n base mamba
```

Conda environments keep a Python version and its selected dependencies together, so a broken environment can be removed and recreated without affecting other projects.

### Pixi

[Pixi](https://pixi.sh/) is a project-oriented tool built around Conda packages and environments. The repository still contains `pixi.toml` and `pixi.lock` as a fallback for maintainers, but the student instructions use `uv`.

[↑ Home](.)
