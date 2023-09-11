stats = sp98.groupby(['id', 'week'])['prix'].mean().unstack('id')
stats.head()
