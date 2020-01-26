## 2. Introduction To The Data ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter = '\t')

train = data.iloc[0:1460]

test = data.iloc[1460:]

target = 'SalePrice'

## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn

fig  = plt.figure(figsize = (7,15))
ax1 = fig.add_subplot(3, 1,1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

train.plot(x = 'Garage Area', y = 'SalePrice', ax = ax1, kind = 'scatter')
train.plot(x = 'Gr Liv Area', y = 'SalePrice', ax = ax2, kind = 'scatter')
train.plot(x = 'Overall Cond', y = 'SalePrice', ax = ax3, kind = 'scatter')
plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(train[['Gr Liv Area']], train['SalePrice'])
print(model.coef_)

print(model.intercept_)

a0 = model.intercept_

a1 = model.coef_

## 6. Making Predictions ##

import numpy as np

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

test_predictions = lr.predict(test[['Gr Liv Area']])
train_predictions = lr.predict(train[['Gr Liv Area']])
from sklearn.metrics import mean_squared_error

mse_train = mean_squared_error(train_predictions, train['SalePrice'])
mse_test = mean_squared_error(test_predictions, test['SalePrice'])

train_rmse = np.sqrt(mse_train)
test_rmse = np.sqrt(mse_test)



## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

linear_model = LinearRegression()

linear_model.fit(train[cols], train['SalePrice'])
train_predictions = linear_model.predict(train[cols])
test_predictions = linear_model.predict(test[cols])

train_mse = mean_squared_error(train_predictions, train['SalePrice'])
test_mse = mean_squared_error(test_predictions, test['SalePrice'])

train_rmse_2 = np.sqrt(train_mse)
test_rmse_2 = np.sqrt(test_mse)