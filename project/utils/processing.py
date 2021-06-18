import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from project.utils.implementation_scaler import standard
from project.algorithm.implementation_dtree import prediction
from project.utils.implementation_error import error_calculator

def d_processing(req, out):
    request_data = json.loads(req)

    month = request_data["month"]
    test_s = request_data["test"]
    if not test_s:
        test_s = 20
    test_s *= .01
    features = request_data["features"]
    features.append("Month")
    features.append("Weekly_Sales")
    s = "np.c_["
    for i in features:
        s += "out." + i + ","
    s += "]"
    n = eval(s)
    # filtering by months

    res_df = pd.DataFrame(n, columns = features)

    if month >= 1 or month <= 12:
        res_df.set_index(keys = ['Month'], drop = False, inplace = True)
        res_df = res_df.loc[res_df.Month == month]
    else:
        pass
    y = res_df['Weekly_Sales']
    res_df = res_df.iloc[: , :-1]
    res_df.to_csv('./data/n1.csv')
    res_df = res_df.iloc[: , :-1]
    res_df.to_csv('./data/n2.csv')
    y.to_csv('./data/n3.csv')
    features_training, features_testing, target_training, target_testing = train_test_split(res_df,y, test_size=test_s)
    features_training, features_testing = standard(features_training, features_testing)
    model, target_pred = prediction(features_training, target_training, features_testing, target_testing)
    error_c = error_calculator(model, features_training, target_training, features_testing, target_testing)
    return [error_c, pd.DataFrame(target_pred).describe()]
