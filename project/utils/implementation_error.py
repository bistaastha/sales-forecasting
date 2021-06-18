from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

def error_calculator(model, features_train, target_train, features_test, target_test):
    target_train_predict = model.predict(features_train)
    rmse = (np.sqrt(mean_squared_error(target_train, target_train_predict)))
    r2 = r2_score(target_train, target_train_predict)
    
    html = f"Model Performance - Training set:<br>Root Mean Square Error: {rmse}<br>R2 Score: {r2}<br><br>"

    target_test_predict = model.predict(features_test)
    rmse = (np.sqrt(mean_squared_error(target_test, target_test_predict)))
    r2 = r2_score(target_test, target_test_predict)
    html += f"Model Performance - Testing set:<br>Root Mean Square Error: {rmse}<br>R2 Score: {r2}<br><br>"
    return html
