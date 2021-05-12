from sklearn.svm import LinearSVR

def prediction(x, y, x_test, y_test):
    lsvr = LinearSVR()
    lsvr.fit(x, y)
    print(lsvr.score(x_test, y_test))
    return lsvr.predict(x_test)
