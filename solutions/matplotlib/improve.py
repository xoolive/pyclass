# ruff: noqa: E402
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)

fig, ax = plt.subplots()
(cos_plot,) = ax.plot(x, c)
(sin_plot,) = ax.plot(x, s)
fig

# %%
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.savefig("../assets/images/matplotlib3a.png")
fig

# %%
ax.set_xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
fig.savefig("../assets/images/matplotlib3b.png")
fig
# %%
ax.set_xticklabels(["$-\pi$", "$-\pi/2$", "$0$", "$\pi/2$", "$\pi$"])
fig.savefig("../assets/images/matplotlib3c.png")
fig

# %%
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
fig.savefig("../assets/images/matplotlib3d.png")
fig

# %%
ax.set_yticks([-1, 0, 1])
fig.savefig("../assets/images/matplotlib3e.png")
fig

# %%
t = 2 * np.pi / 3

ax.plot([t, t], [0, np.cos(t)], color=cos_plot.get_color(), ls="--", lw=2)
cos_point = ax.scatter(t, np.cos(t), 50, color=cos_plot.get_color())

ax.plot([t, t], [0, np.sin(t)], color=sin_plot.get_color(), ls="--", lw=2)
ax.scatter(t, np.sin(t), 50, color=sin_plot.get_color())

ax.annotate(
    r"$\sin\left(\dfrac{2\pi}{3}\right)=\dfrac{\sqrt{3}}{2}$",
    xy=(t, np.sin(t)),
    xycoords="data",
    xytext=(+10, +30),
    textcoords="offset points",
    # fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
ax.annotate(
    r"$\cos\left(\dfrac{2\pi}{3}\right)=-\dfrac{1}{2}$",
    xy=(t, np.cos(t)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    # fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

fig.savefig("../assets/images/matplotlib3f.png")
fig

# %%
cos_plot.set_linewidth(5)
cos_plot.set_zorder(0)
cos_point.set_sizes([80])
ax.plot(x, c, color="white", zorder=0)
ax.scatter(t, np.cos(t), 20, color="white")
fig.savefig("../assets/images/matplotlib3g.png")
fig

# %%
from matplotlib import ticker

fig, ax = plt.subplots()
ax.plot(c, s)

# spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
# square ratio
ax.set_aspect(1)

# one tick every .5 (alternative method)
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

fig.savefig("../assets/images/matplotlib3h.png")
fig

# %%
