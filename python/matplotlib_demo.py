# # The `matplotlib` library
#
# `matplotlib` offers a wide range of commands to display data, plot lines, fill
# areas with colors, print text, etc. in order to produce top quality data
# visualisations.
# %%

import numpy as np
import matplotlib.pyplot as plt


# The `plot` instruction takes a list of x-coordinates and a list of
# y-coordinates.
# %%

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


# A default style is applied automatically, but it is possible to select:
#
# - colors;
# - marker styles;
# - axis length;
# - etc.
# %%


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro-")
plt.xlim(0, 6)
plt.ylim(0, 20)
plt.xlabel("Time")
plt.ylabel("Money")


# Consider using Matplotlib with Numpy arrays
# %%
# 200ms interval samples
t = np.arange(0.0, 5.0, 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, "r--", t, t ** 2, "bs", t, t ** 3, "g^")


# Lastly, note that it is possible to display several graphs side by side.
# You can also specify the size of the figure.
# %%


fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(10, 10))

# Some sites help finding consistent colors:
# http://paletton.com/#uid=7000u0kllllaFw0g0qFqFg0w0aF

ax[0, 0].plot(t, np.sin(t), "#aa3939")
ax[0, 1].plot(t, np.cos(t), "#aa6c39")
ax[1, 0].plot(t, np.tan(t), "#226666")
ax[1, 1].plot(t, np.sqrt(t), "#2d882d")


# Consider it good practice to start your plots with:
# ```python
# fig, ax = plt.subplots()
# ```

# ## Exercice #1 (solutions/numpy/trace_cos.py)
# Trace the graph of function $t \mapsto e^{-t} \cdot \cos(2\,\pi\,t)$
# for $t\in[0,5]$
# %%

# ## Exercice #2 (solutions/numpy/trace_sin.py)
# Consider the polar coordinate curve defined by $r = \sin(5\,\theta)$, compute
# the x- and y- coordinates using Numpy functions, then plot the curve.
# %%


# ## Further references
# - The official documentation: https://matplotlib.org/
# - Matplotlib cheatsheets: https://github.com/matplotlib/cheatsheets
# - The dedicated chapter in: https://www.xoolive.org/python/matplotlib/
