## 2. Removing features ##

drop = ['room_type', 'city', 'state', 'latitude', 'longitude', 'zipcode', 'host_acceptance_rate', 'host_listings_count', 'host_response_rate']

dc_listings = dc_listings.drop(drop, axis = 1)


## 3. Handling missing values ##

drop_columns = ['cleaning_fee', 'security_deposit']
dc_listings = dc_listings.drop(drop_columns, axis = 1)

dc_listings = dc_listings.dropna(axis = 0)

print(dc_listings.isnull().sum())

## 4. Normalize columns ##

normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())

normalized_listings['price'] = dc_listings['price']

print(normalized_listings.head(3))



## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance

first_listing = normalized_listings.iloc[0][['accommodates', 'bathrooms']]
fifth_listing = normalized_listings.iloc[4][['accommodates', 'bathrooms']]
first_fifth_distance = distance.euclidean(first_listing, fifth_listing)
print(first_fifth_distance)

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

knn = KNeighborsRegressor(n_neighbors = 5, algorithm = 'brute')
train_features = train_df[['accommodates', 'bathrooms']]
train_target = train_df['price']
knn.fit(train_features,  train_target)
predictions = knn.predict(test_df[['accommodates', 'bathrooms']])

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error
from math import sqrt

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse = mean_squared_error(test_df['price'], predictions)

two_features_rmse = sqrt(two_features_mse)

## 9. Using more features ##

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

knn.fit(train_df[features], train_df['price'])

four_predictions = knn.predict(test_df[features])

from sklearn.metrics import mean_squared_error

four_mse = mean_squared_error(test_df['price'], four_predictions)

from math import sqrt

four_rmse = sqrt(four_mse)

## 10. Using all features ##

knn = KNeighborsRegressor(n_neighbors = 5, algorithm ='brute')
features = train_df.columns.tolist()
features.remove('price')

knn.fit(train_df[features], train_df['price'])

all_features_predictions = knn.predict(test_df[features])

all_features_mse = mean_squared_error(test_df['price'] , all_features_predictions)

all_features_rmse = sqrt(all_features_mse)