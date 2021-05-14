from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

def error_calculator(model, x_train, y_train, x_test, y_test):
    #Training prediction
    y_train_predict = model.predict(x_train)
    rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
    r2 = r2_score(y_train, y_train_predict)
    print("Model performance for training set:")
    print("-----")
    print(f"RMSE is {rmse}")
    print(f"R2 score is {r2}")
    print("\n")

    #Testing prediction
    y_test_predict = model.predict(x_test)
    rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
    r2 = r2_score(y_test, y_test_predict)
    print("The model performance for testing set")
    print("-----")
    print(f"RMSE is {rmse}")
    print(f"R2 score is {r2}")
