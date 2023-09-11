---
layout: default
permalink: /numpy
title: Numpy and Matplotlib
---

This session is based on a Python file. When you open this file with Visual Studio Code, you will notice pseudo-cells prefixed as follows:

![vscode ipython](../assets/images/vscode_ipython.png)

Clicking on `Run Cell` (or pressing `Maj+Enter`) runs an IPython kernel appearing (usually) on the right side of your screen.

This approach is comfortable to preliminary projects:

- you can run, debug the code as a usual Python file, making your work _reproducible_;
- you can explore ideas with a notebook style, making your work _interactive_.

<div class="alert alert-success">
<b>Good practice</b> &nbsp;&nbsp; Consider this option before jumping to Jupyter notebooks when you start a new project. Notebooks are a natural choice for education materials, but they lack rigor in terms of software engineering and management.
</div>

The file is located in the `python/` folder:

- `numpy_demo.py`

## More exercices for NumPy

This is a selection of exercises from https://github.com/rougier/numpy-100

1. Reverse a vector. You may use vector `x` defined as follows:

   ```python
   x = np.arange(50)
   ```

2. Find the min and max values in a 10x10 array. Find their indices.

   ```python
   x = np.random.random((10, 10))
   ```

3. Create a 2d array with 1 on the border and 0 inside.

4. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

5. Create a 8x8 matrix and fill it with a checkerboard pattern

6. Normalize a 5x5 random matrix

   ```python
   x = np.random.random((5, 5))
   ```

## More exercices for Matplotlib

[↑ Home](.) \| [Next >>](matplotlib)
