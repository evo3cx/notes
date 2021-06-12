import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split

# load iris dataset, ini  dataset yang umum digunakan untuk masalah klasifikasi
iris = datasets.load_iris()

# pisahkan atribut dan label pada iris dataset
x = iris.data # training set
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.2)

print(len(x_train))
print(len(x_test))
print(len(y_train))
print(len(y_test))
