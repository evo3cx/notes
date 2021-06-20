import pandas as pd
from path import sample_path
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# membaca dataset dan mengubah menjadi dataframe
data = pd.read_csv(sample_path+'/Salary_Data.csv')

# memisahkan atribut dan label
X = data['YearsExperience']
y = data['Salary']


X = X.to_numpy()
# mengubah bentuk atribut from 1D to 2D
X = X[:,np.newaxis]
print(X)

# membangun model dengan parameter C, gamma, dan kernel
model = SVR(C=10000, gamma=0.05, kernel='rbf')

# melatih model dengan fungsi fit
model.fit(X, y)

# visualisasikan model
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.show()
