################# Function to fit your Linear Regression Model ###################
def linear_regression_all_variables(data_train):
    from sklearn.linear_model import LinearRegression
    regr = LinearRegression()
    target = data_train["SalePrice"]
    features = data_train[["LotArea", "YearBuilt", "GarageArea", "BedroomAbvGr"]]
    columns = features.columns.tolist()
    regr.fit(features, target)
    coefs = regr.coef_
    dict_coeff = {}
    for i in range(len(columns)):
        dict_coeff[columns[i]] = coefs[i]
    return([dict_coeff, regr])



################# Function to compute the Root Mean Squared Error ###################
def compute_mse_test(data_train, data_test):
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    dict_coeff, lreg = linear_regression_all_variables(data_train)
    test_features = data_test[["LotArea", "YearBuilt", "GarageArea", "BedroomAbvGr"]]
    test_target = data_test["SalePrice"]
    y_pred = lreg.predict(test_features)
    rmse = mean_squared_error(test_target, y_pred)
    return(rmse)