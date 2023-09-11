stations = stations.assign(
    departement=stations.code_postal.apply(
        lambda x: x[:3] if x[:2] == '97' else x[:2]
    )
)
stations.head()
