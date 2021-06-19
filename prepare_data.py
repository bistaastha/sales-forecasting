import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("./data/train.csv")
stores = pd.read_csv("./data/stores.csv")
features = pd.read_csv("./data/features.csv")

for i in range(1, 6):
    features[f"MarkDown{i}"] = features[f"MarkDown{i}"].fillna(0)
features["Unemployment"] = features["Unemployment"].fillna(np.mean(features["Unemployment"]))
features["CPI"] = features["CPI"].fillna(np.mean(features["CPI"]))

main = pd.merge(train, stores, on = "Store", how = "right", sort = False)
main = pd.merge(main, features, on = ["Store", "Date"], how = "left", sort = False)

main = main.sort_values(by=["Date"])


main["Month"] = pd.to_datetime(main["Date"]).dt.month
main["Year"] = pd.to_datetime(main["Date"]).dt.year

main["IsHoliday"] = main["IsHoliday_y"]
main.drop(labels=["IsHoliday_y", "IsHoliday_x", "Date"], axis = 'columns', inplace=True)

months = ['All','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temp = pd.get_dummies(main.Type)
main = pd.concat([main, temp], axis='columns')
main = main.drop(columns=['Type'])

main.to_csv('./data/out.csv')

correlation_matrix = main.corr().round(3)

figure, axes = plt.subplots(figsize=(12,12))
sns.heatmap(correlation_matrix, annot=True, linewidths=.7, ax=axes)
plt.show()
