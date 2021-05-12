from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def split_data(X, y):
     return train_test_split( X, y, test_size=0.20, random_state=0)

def standard(train, test):
    s = StandardScaler()
    return s.fit_transform(train), s.transform(test)

def printer():
    print("hello")
