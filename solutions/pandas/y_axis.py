fig, ax = plt.subplots(figsize=(8.8, 5))
points = plt.scatter(*Xpca.T, c=sp98_dept_filled.std(), cmap='cubehelix')
for (x, y), name in zip(Xpca, sp98_dept_filled.columns):
    plt.annotate(name, (x,y))
plt.colorbar(label='Écart type des prix par station')
