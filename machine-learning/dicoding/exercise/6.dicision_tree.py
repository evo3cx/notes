# Pada latihan ini, kita akan melakukan klasifikasi data yang kita miliki dengan teknik Decision Tree menggunakan dataset iris,
# salah satu dataset paling populer yang dipakai dalam belajar ML. 
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

# Membaca file iris.csv
iris = pd.read_csv('../assets/Iris.csv')


# Hilangkan kolom yg tidak penting
iris.drop('Id', axis=1, inplace=True)

# Memisahkan attribute dengan label
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm' ]]
y = iris['Species']

# membuat model Decision Tree
tree_model = DecisionTreeClassifier()

# melakukan pelatihan model terhadap data
tree_model.fit(X,y)

# prediksi model dengan tree_model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
predict = tree_model.predict([[5.1,2.5,3.0,1.1]])
print(predict, "predict")


export_graphviz(
  tree_model,
  out_file="iris_tree.dot",
  feature_names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
    class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica' ],
    rounded= True,
    filled =True
)
