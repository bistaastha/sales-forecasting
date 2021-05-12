from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor

def prediction(x, y, x_test, y_test):
    knn = KNeighborsRegressor(n_neighbors=10,n_jobs=4)
    knn.fit(x, y)
    print(knn.score(x_test, y_test))
    return knn.predict(x_test)


def printer():
    print("Hello")
