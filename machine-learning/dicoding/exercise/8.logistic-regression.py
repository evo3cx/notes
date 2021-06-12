import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import os 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# load dataset from assets
path = os.path.dirname(__file__)
df = pd.read_csv(path+"/sample_data/Social_Network_Ads.csv")


# drop kolom yang tidak perlukan
data = df.drop(columns=['User ID'])

# jalankan prosess one-hot encoding dengan pd.get_dummies()
#  prosses akan mengubah nilai Femal & male menjadi numeric value
data = pd.get_dummies(data)

print(data)

# Pisahkan antara atribute dan label
predictions = ['Age' , 'EstimatedSalary' , 'Gender_Female' , 'Gender_Male']
X = data[predictions]
y = data['Purchased']

# lakukan normalisasi terhadap data yg kita miliki
scaler = StandardScaler()
scaler.fit(X)

scaled_data = scaler.transform(X)
frame = pd.DataFrame(scaled_data, columns=X.columns)
print(frame.head())

# bagi data menjadi train dan test untuk setiap atribut dan label
X_train, X_test, y_train, y_test = train_test_split(frame, y, test_size=0.1, random_state=1)

# latih model dengan fungsi fit
model = linear_model.LogisticRegression()
model.fit(X_train,y_train)

print(X_test)

# fungsi score digunakan untuk menghitung akurasi model
score = model.score(X_test, y_test);
print(score)
