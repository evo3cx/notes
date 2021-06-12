from sklearn.model_selection import train_test_split

y_data = range(10)
x_data = range(10)


print("random state ditentukan")
for i in range(3):
  x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=0.3, random_state=1)
  print(y_test)


print("random stae tidak ditentukan")
for i in range(3):
  x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, test_size=2, random_state=None)
  print(y_test)
