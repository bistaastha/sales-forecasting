from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def prediction(x, y, x_test, y_test):
    dtree = DecisionTreeRegressor(random_state=0)
    dtree.fit(x, y)
    print(dtree.score(x_test, y_test))
    y_pred = dtree.predict(x_test)
    return [dtree, y_pred]
