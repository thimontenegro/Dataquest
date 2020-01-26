## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

numerical_train = train.select_dtypes(include = ['int', 'float'])

numerical_train = numerical_train.drop(['PID', 'Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold'], axis = 1)

null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]
corrmat = train_subset.corr()
sorted_corrs = corrmat['SalePrice'].abs().sort_values()


## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs = sorted_corrs[sorted_corrs > 0.3]

corrmat = train_subset[strong_corrs.index].corr()

sns.heatmap(corrmat)

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'

clean_test = test[final_corr_cols.index].dropna()

linear_model = LinearRegression()
linear_model.fit(train[features], train[target])

train_predictions = linear_model.predict(train[features])
test_predictions = linear_model.predict(clean_test[features])

train_mse = mean_squared_error(train_predictions, train[target])
test_mse =  mean_squared_error(test_predictions, clean_test[target])

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

## 5. Removing Low Variance Features ##

unit_train = (train[features] - train[features].min()) / (train[features].max() - train[features].min())
              
print(unit_train.min())
print(unit_train.max())

sorted_vars = unit_train.var().sort_values()

## 6. Final Model ##

clean_test = test[final_corr_cols.index].dropna()
features = features.drop('Open Porch SF')

linear_model = LinearRegression()
linear_model.fit(train[features], train['SalePrice'])

train_predictions = linear_model.predict(train[features])
test_predictions = linear_model.predict(clean_test[features])

train_mse = mean_squared_error(train_predictions, train['SalePrice'])
test_mse = mean_squared_error(test_predictions, clean_test['SalePrice'])

train_rmse_2 = np.sqrt(train_mse)
test_rmse_2 = np.sqrt(test_mse)