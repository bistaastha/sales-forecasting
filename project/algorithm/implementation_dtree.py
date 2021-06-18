from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def prediction(features_train, target_train, features_test, target_test):
    dtree = DecisionTreeRegressor()
    dtree.fit(features_train, target_train)
    target_pred = dtree.predict(features_test)
    return [dtree, target_test]
