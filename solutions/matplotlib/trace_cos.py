import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))
t = np.arange(0.0, 5.0, 0.2)
ax.plot(t, np.exp(-t) * np.cos(2 * np.pi * t))
plt.show()
