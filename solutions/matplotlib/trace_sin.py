import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0.0, 2 * np.pi, 100)
r = np.sin(5 * theta)
x, y = r * np.cos(theta), r * np.sin(theta)
fig, ax = plt.subplots(figsize=(10, 10))
plt.plot(x, y)
plt.show()
