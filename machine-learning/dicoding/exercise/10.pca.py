from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.decomposition import PCA

# load iris dataset
iris = datasets.load_iris()
atribut = iris.data
label = iris.target

# bagi dataset menjadi train set and test set
X_train, X_test, y_train, y_test = train_test_split(atribut, label, test_size=0.2)


# gunakan model Dicision Tree untuk menghitung akurasi PCA
decision_tree = tree.DecisionTreeClassifier()
model_pertama = decision_tree.fit(X_train, y_train)
print(model_pertama.score(X_test, y_test))

# membuat objek PCA dengan 4 principan component
pca = PCA(n_components=4)

# mengaplikasikan PCA pada dataset
pca_attributes = pca.fit_transform(X_train)

# melihat variance dari setiap atribute
print(pca.explained_variance_ratio_, pca.n_features_)

# Melihat dari variance sebelumnya kita bisa mengambil 2 principal 
# component terbaik karena total variance nya adalah 0.969 yang sudah cukup tinggi.
pca2 = PCA(n_components=2)
x_train_pca = pca2.fit_transform(X_train)
x_test_pace = pca2.fit_transform(X_test)

# melihat variance dari setiap atribute
print(pca2.explained_variance_ratio_, pca2.n_features_)


# uji akurasi clasfier
model_kedua = decision_tree.fit(x_train_pca, y_train)
print(model_kedua.score(x_test_pace, y_test))
