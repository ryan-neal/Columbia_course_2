import pandas as pd
import numpy as np 
import math
def clean_data(file):
    data = pd.read_csv(file)
    data.dropna(inplace=True)
    nb_rows = len(data)
    return ([nb_rows, data])

df = clean_data("Stocks.csv")[1]

def compute_mean_portfolio(data):  
    def expected_value(df):
        portfolio_weights = {"BA": .16, "AAPL": .17, "AMZN": .35, "GOOGL": .21, "MC.PA": .08, "MSFT": .03}
        x = data.drop(["Date", "GM"], axis=1)
        if "Portfolio" in x.columns:
            x.drop(["Portfolio"], axis = 1, inplace=True)
        value = 0
        for col in x.columns:
            value += x[col] * portfolio_weights[col]
        return value
    
    data["Portfolio"] = expected_value(data)
    return([data["Portfolio"].mean(), data])

df = compute_mean_portfolio(df)[1]
print(compute_mean_portfolio(df)[0])


def compute_standard_deviation_portfolio(data):
    portfolio_weights = {"BA": .16, "AAPL": .17, "AMZN": .35, "GOOGL": .21, "MC.PA": .08, "MSFT": .03}
    x = data.drop(["Date", "GM", "Portfolio"], axis=1)
    weights = []
    cor = x.cov()
    for col in x.columns:
        weights.append(portfolio_weights[col])
    weights = np.array([weights])
    variance = weights*np.matrix(cor)*weights.T
    return math.sqrt(variance)

std = compute_standard_deviation_portfolio(df)

def compute_interval(mean_portfolio, std_dev_portfolio):
    # a = lower bound interval
    a = mean_portfolio - (1.96 * std_dev_portfolio)
    # b = upper bound interval
    b = mean_portfolio + (1.96 * std_dev_portfolio)
    return([a, b])

print(compute_interval(compute_mean_portfolio(df)[0], std))


def compute_correlation_matrix(data):
    # data = dataset returned in q2 (includes the portfolio returns)
    x = data.drop(["Portfolio"], axis = 1)
    cor = x.corr()
    # Code goes here
    lst = cor.sort_values(["GM"], ascending=False)
    max_cor = lst["GM"][1]
    # max_cor = value of the largest correlation coefficient (see exercise description)
    # cor = correlation matrix of the seven stocks (please provide it as a pandas dataframe)
    return([max_cor, cor])