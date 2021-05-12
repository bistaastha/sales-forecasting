from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

def prediction(x, y, x_test, y_test):
    rf = RandomForestRegressor(n_estimators = 400, max_depth = 15, n_jobs = 5)
    rf.fit(x, y)
    print(rf.score(x_test, y_test))
    return rf.predict(x_test)


def printer():
    print("Hello")
