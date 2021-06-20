import numpy as np
import pandas as pd
from path import sample_path
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR

# membaca dataset dan mengubah menjadi dataframe
data = pd.read_csv(sample_path+'/Salary_Data.csv')

# memisahkan atribut dan label
X = data['YearsExperience']
y = data['Salary']

# mengubah bentuk atribut dari 1d to 2D
X = X.to_numpy()
X = X[:,np.newaxis]

# membangun model dengan parameter C, gamma, dan kernel
model = SVR()
parameters = {
  'kernel': ['rbf'],
  'C': [1000, 10000, 100000],
  'gamma': [0.5, 0.05, 0.005],
}
grid_search = GridSearchCV(model, parameters)

# melatih model dengan fungsi fit
grid_search.fit(X, y)

print(grid_search.best_params_)

# membuat model SVM baru dengan parameter terbaik hasil grid search
model_baru = SVR(C=100000, gamma=0.005, kernel='rbf')
model_baru.fit(X, y)


# visualization
import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, model_baru.predict(X))
plt.show()
