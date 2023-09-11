sp98_dept_filled = (  # adding brackets is nice to chain methods and pretty-print
    sp98_dept
    .groupby(['departement', 'week'])
    ['prix']
    .mean()
    .unstack('departement')
    .fillna(method='ffill')
    .fillna(method='bfill')
)

Xpca = PCA(n_components=2).fit_transform(sp98_dept_filled.T)

plt.figure(figsize=(7, 5))
points = plt.scatter(Xpca[:, 0], Xpca[:, 1], s=10)
for (x, y), name in zip(Xpca, sp98_dept_filled.columns):
    plt.annotate(" {}".format(name), (x,y),)
