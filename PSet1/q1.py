def clean_data(file = 'Stocks.csv'):
    import os
    import pandas as pd
    # path to the csv file containing the data
    cwd = os.getcwd()
    path = '/'.join(cwd.split('/')[:-1]) + '/resource/asnlib/public/' + file
    # Code goes here
    # data = cleaned pandas dataframe
    # nb_rows = number of rows in data
    with open(path) as f:
        data = pd.read_csv(f)
    data.dropna(inplace=True)
    nb_rows = len(data)
    return([nb_rows, data])

print(clean_data())