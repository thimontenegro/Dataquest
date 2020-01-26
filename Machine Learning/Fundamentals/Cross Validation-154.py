## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

shuffled_index = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.reindex(shuffled_index)

split_one = dc_listings.iloc[0:1862].copy()
split_two = dc_listings.iloc[1862:].copy()


## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two

train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
test_one['predicted_price'] = knn.predict(test_one[['accommodates']])
iteration_one_rmse = mean_squared_error(test_one['price'], test_one['predicted_price']) ** (1/2)

#Second Training

knn.fit(train_two[['accommodates']], train_two['price'])
test_two['predicted_price'] = knn.predict(test_two[['accommodates']])
iteration_two_rmse = mean_squared_error(test_two['price'], test_two['predicted_price']) ** (1/2)
import numpy as np
avg_rmse = np.mean([iteration_one_rmse , iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings.loc[dc_listings.index[0:745], 'fold'] = 1
dc_listings.loc[dc_listings.index[745:1490], 'fold'] = 2
dc_listings.loc[dc_listings.index[1490:2234], 'fold'] = 3
dc_listings.loc[dc_listings.index[2234:2978], 'fold'] = 4
dc_listings.loc[dc_listings.index[2978:3723], 'fold'] = 5

print(dc_listings['fold'].value_counts())
print('\n Num of missing values: ', dc_listings['fold'].isnull().sum())

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_iteration_one = dc_listings[dc_listings['fold'] != 1]
test_iteration_one = dc_listings[dc_listings['fold'] == 1].copy()


knn = KNeighborsRegressor()

knn.fit(train_iteration_one[['accommodates']], train_iteration_one['price'])

#Predicting
labels = knn.predict(test_iteration_one[['accommodates']])
test_iteration_one['predicted_price'] = labels
iteration_one_mse =mean_squared_error(test_iteration_one['price'], test_iteration_one['predicted_price'])
iteration_one_rmse = iteration_one_mse ** (1/2)


## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]


def train_and_validate(df, folds):
    folds_rmse = []
    for fold in folds:
        knn = KNeighborsRegressor()
        train = df[df['fold'] != fold]
        test = df[df['fold'] == fold].copy()
        knn.fit(train[['accommodates']], train['price'])
        labels = knn.predict(test[['accommodates']])
        test['predicted_price'] = labels
        mse = mean_squared_error(test['price'], test['predicted_price'])
        rmse = mse ** (1/2)
        folds_rmse.append(rmse)
    return folds_rmse

rmses = train_and_validate(dc_listings, fold_ids)
print(rmses)
avg_rmse = np.mean(rmses)
print(avg_rmse)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits = 5, shuffle = True, random_state = 1)

knn = KNeighborsRegressor()

mses = cross_val_score(knn, dc_listings[['accommodates']], dc_listings['price'], scoring = 'neg_mean_squared_error', cv = kf)
rmses = np.sqrt(np.absolute(mses))
avg_rmse = np.mean(rmses)