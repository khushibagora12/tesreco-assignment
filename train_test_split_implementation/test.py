from train_test_split import train_test_split

X = [i for i in range(20)]
y = [i for i in range(20)]

X_train, y_train, X_test, y_test = train_test_split(X, y, 0.2)

print("x train: ", X_train)
print("y train: ", y_train)
print("x test: ", X_test)
print("y test: ", y_test)

X_train, y_train, X_test, y_test = train_test_split(X, y, 0.3)

print("x train: ", X_train, X_train.shape)
print("y train: ", y_train, y_train.shape)
print("x test: ", X_test, X_test.shape)
print("y test: ", y_test, y_test.shape)