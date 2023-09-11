stats_filled = stats.fillna(method='ffill').fillna(method='bfill')
Xpca = PCA(n_components=2).fit_transform(stats_filled.T)
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(Xpca[:, 0], Xpca[:, 1], s=.3)
