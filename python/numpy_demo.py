# ## The `numpy` library
#
# `numpy` is a Python library designed to manipulate multi-dimensional arrays.
# It is often used together with the `scipy` library, containing tools for
# linear algebra, integration, optimisation, signal analysis and more.
#
# We present here very simple Numpy functionalities. For more details, refer to
# the official documentation:
# https://docs.scipy.org/doc/numpy/reference/

# %%
import numpy as np

# ## Types of embedded arrays
#
# A Numpy array can be made of an iterable structure (table, tuple, list). Numpy
# becomes powerful because all elements in the array have the same type
# (called `dtype`)
# %%
# Types in a Python array
table = [2, 7.3, 4]
type(table), [(value, type(value)) for value in table]

# %%
# Types in a Numpy array
np_table = np.array(table)
(type(np_table), np_table.dtype, [(value, type(value)) for value in np_table])


# ## Performance
#
# Python is commonly blamed for being slow at runtime. This comes for many
# factors, in particular the flexibility of the language, the numerous checks
# made at runtime (Python cannot assume anything about your data) and dynamic
# typing. Now with Numpy, we know with the `dtype`, the types of all elements in
# the array: arithmetic operations can be processed and accelerated in C.
# %%
table = [i for i in range(1, 10000000)]
np_array = np.array(table)


# %%
%%timeit
# Note: the timeit operator is specific to IPython and Jupyter. It is not
# valid Python syntax but will be interpreted correctly in the console if 
# put at the very beginning of a cell.
double = [x * 2 for x in table]

# %%
%%timeit
np_double = 2 * np_array

# ## Views on Numpy array
#
# It is possible to work on views of a previously built array. We use the word
# "view" because modifying data in the "view" also modifies data in the original
# array.
# %%
np_array = np.array([[i + 2 * j for i in range(5)] for j in range(4)])
np_array

# %%
sub = np_array[0:2, 2:4]
sub

# %%
sub = np_array[:3, 2:]
sub

# %%
# Modifying sub values also modifies the original array
sub[:] = 0
np_array

# ## Matrix operations
#
# %%
a = np.array([[4, 6, 7, 6]])
b = np.array([[i + j for i in range(4)] for j in range(4)])

print(f"{a}\n with dimensions {a.shape}")
print(f"{b}\n with dimensions {b.shape}")

# %%
# Dot product (or matrix product)
np.dot(a, b)

# %%
# Term by term addition, multiplication, etc.
2 * a

# %%
a + a

# %%
a * a

# %%
# Dimensions are broadcast when needed:
# (details in https://www.xoolive.org/python/numpy/)

a * b

# This is NOT a dot product!!

# %%
import numpy.linalg  # noqa: E402

a = np.array([[abs(i - j) for i in range(5)] for j in range(5)])
inv_a = numpy.linalg.inv(a)

a * inv_a

# %%
inv_a @ a  # @ operator (called `matmul`), equivalent to np.dot(inv_a, a)

# ## Further references
#
# - Numpy tutorial:
#   https://github.com/rougier/numpy-tutorial
# - From Python to Numpy:
#   https://www.labri.fr/perso/nrougier/from-python-to-numpy/
# - 100 Numpy exercices:
#   https://github.com/rougier/numpy-100/
# - The dedicated chapter in https://www.xoolive.org/python/numpy/
