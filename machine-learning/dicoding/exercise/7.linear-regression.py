import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

# %matplotlib inline

# number of bedrooms
bedrooms = np.array([[1,2,2,2,3,4,4,5,5,5]])

# data harga rumah. asumsi dalam dollar
house_price = np.array([15000, 18000, 27000, 34000, 50000, 68000, 65000, 81000,85000, 90000])

bedrooms = bedrooms.reshape(-1,1)

# mulai lati model kita
linear_regression = LinearRegression()

linear_regression.fit(bedrooms, house_price)

# draw scanner
plt.scatter(bedrooms, house_price)

# draw plot
plt.plot(bedrooms, linear_regression.predict(bedrooms))

plt.show()
