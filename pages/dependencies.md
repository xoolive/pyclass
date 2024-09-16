---
layout: default
title: Understand the difference between pip and conda
permalink: /dependencies
---

## Managing Python dependencies

Python dependency management is a serious topic, as you want to be able to:

- be able to reproduce code behaviour on your computer;
- have other users (and your favourite teacher) reproduce the behaviour you got on their computer.

During your classes (and future professional life), your most common need will be to import libraries which are not necessarily installed by default, and on computers where you do not necessarily have administrator rights.

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

This is just an exemple with the default Python interpreter shipped with Ubuntu 20.04, and the result will probably be different for you.
What is important here is to note that the order of import resolution will proceed as follow:

- first look at the current directory;
- directories set in the `PYTHONPATH` environment variables come next  
  (between `''` and `'/usr/lib/python312.zip'` in the current example);
- in the system folders mentioned above;
- a private home folder with no required administrator rights, but **it may not appear on your side**.

<div class="alert alert-warning">
<b>Warning</b> &nbsp;&nbsp; When external dynamic libraries (mostly written in C or C++) need to be loaded, other folders are watched, depending on your operating systems. The <code>LD_LIBRARY_PATH</code> variable lets you extend the list of folders to check.
</div>

### Managing dependencies with `pip`

Dealing with dependencies in custom folders does not scale well. Some people like to extend the `sys.path` folder programmatically, but in most cases it is a poor idea.

`pip` is an excellent tool provided to install packages (and their dependencies!) from:

- local folders, most of the time with `pip install .` ;
- remote servers, like [https://pypi.org/](https://pypi.org/), with commands like `pip install pandas`.

`pip` installs packages in system folders first, but you can use the `--user` option to install in local folders. Remember `'/home/xo/.local/lib/python3.12/site-packages'`. It is important to ensure that such folder where `pip` installs packages is part of your Python `sys.path` list of folders, but `pip` will warn you if that's not the case.

`pip` installs only Python dependencies. Publishing a package on PyPI (out of the scope of this seminar) is pretty flexible. Also, it does not ensure the global consistency of the Python ecosystem you have installed on your computer, which can become problematic when you install, update, deinstall, reinstall a lot of packages. **It is very likely that you will reach a point where your Python is "broken" because of dependency requirement conflicts.**

<img class="giphy" src="https://media.giphy.com/media/F7yLXA5fJ5sLC/giphy.webp"/>

A common solution is to use virtual environments to avoid such issue. It is possible to use those without Anaconda, but since Anaconda solves other dependency problems as well, let's move to that topic.

### The Anaconda suite

You should already have installed Anaconda by now. Anaconda is a distribution providing Python with a number of optional libraries, tools and their dependencies. Where `pip` is only focused on Python dependencies and requires **YOU** to provide other non Python dependencies, Anaconda lets you install other dependencies compiled in C, C++, R or more. Moreover, the global consistency in versions of dependencies is consistently enforced.

You may then install any missing package as follows:

```text
conda install pandas
```

<div class="alert alert-success">
<b>Good practice</b> &nbsp;&nbsp; The dependency resolution mechanism is rather slow with <code>conda</code>. If you have administrator rights on your computer, we recommend that you install a faster implementation called <code>mamba</code>:

<pre style="margin-top: 1em; margin-bottom: -.5em;"><code>conda install -c conda-forge -n base mamba</code></pre>
</div>

<div class="alert alert-danger">
<b>Warning</b> &nbsp;&nbsp; It is still possible to <span style="text-decoration: line-through">$*@</span> break your environment when you start <code>pip install</code>ing libraries in your Anaconda environment as versions of dependencies are no longer enforced.
</div>

The `conda-forge` channel is very comprehensive, and even more strict about consistency of your environment, which is why we recommend that you set the following options once for all.

```sh
conda config --add channels conda-forge
```

In addition to this strict mechanism, it is considered good practice to work in custom environments. A `conda` environment sets a specific Python version with chosen dependencies:

- If anything breaks one day, you can just remove the environment and create a new one;
- You can have several Python versions for the same project, and segregate environments for different projects.

### Pixi

Pixi is a tool that simplifies and makes conda environment management faster and more efficient.

[↑ Home](.)
