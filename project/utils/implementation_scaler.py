from sklearn.preprocessing import StandardScaler

def standard(train, test):
    s = StandardScaler()
    return s.fit_transform(train), s.transform(test)

