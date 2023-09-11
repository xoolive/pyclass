carburant = carburant.assign(week=carburant.date.dt.isocalendar().week)
carburant.loc[(carburant.week == 53) & (carburant.month == 1), "week"] = 0
