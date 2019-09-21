def clean_data():
    import pandas as pd
    dirty_data = pd.read_csv("house_prices_train.csv", index_col="Unnamed: 0")
    data_train = dirty_data.dropna()
    nb_rows = len(data_train)
    return ([nb_rows, data_train])

