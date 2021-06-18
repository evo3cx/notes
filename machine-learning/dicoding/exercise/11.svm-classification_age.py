import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from path import sample_path

df = pd.read_csv(sample_path + "/diabetes.csv")

# Kita ingin mengecek apakah ada korelasi antara age dengan penyakit diabetes
# memisahkan atribute pada dataset dan menyimpan pada sebuah variabel
columns = df.columns.tolist()
a = columns.pop(7);
X = df[columns]

# memisahkan label pada dataset dan menyimpannya pada sebuah variabel
y = df['Age']

# agar semau memiliki nilai dengan skala yang sama, maka kita akan me-standarisasi semua atribut
scaller = StandardScaler()
scaller.fit(X)
X = scaller.transform(X)
print(X)

# memisahkan data untuk training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# membuah objek SVC dan memanggil fungi fit untuk melatih model
clf = SVC()
clf.fit(X_train, y_train)

# print akurasi prediksi
score = clf.score(X_test, y_test)
print(score)
