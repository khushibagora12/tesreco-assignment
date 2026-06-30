import numpy as np
import math

'''
This function takes iterable X and y, and randomly splits them into training as well as testing datasets
parameters ->
    X -> iterable
    y -> iterable
    ratio -> test_size ratio, default = 0.2
returns->
    X_train -> nd array
    y_train -> nd array
    X_test -> nd array
    y_test -> nd array

'''
def train_test_split(X, y, ratio=0.2):
    
    print("og x: ", X)
    print("og y: ", y)

    X = np.array(X)
    y = np.array(y)

    m = X.shape[0]
    
    test_size = math.floor(ratio*m)

    X_train = []
    y_train = []
    X_test = []
    y_test = []

    rng = np.random.default_rng()
    random_numbers = rng.choice(range(0, m), size=test_size, replace=False)

    for i in range(m):
        if i in random_numbers:
            X_test.append(X[i])
            y_test.append(y[i])
        else:
            X_train.append(X[i])
            y_train.append(y[i])

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    return X_train, y_train, X_test, y_test