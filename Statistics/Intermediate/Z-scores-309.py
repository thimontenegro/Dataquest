## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(), houses['SalePrice'].max()))
mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
plt.axvline(mean, color = 'black', label = 'Mean')
plt.axvline(mean + st_dev, color = 'red', label = 'Standard deviation')
plt.axvline(220000, color = 'orange', label = '220000')
plt.legend()

very_expensive = False

## 2. Number of Standard Deviations ##

mean = houses['SalePrice'].mean()
distance = 220000 - mean
st_dev = houses['SalePrice'].std(ddof = 0)
st_devs_away = distance / st_dev



## 3. Z-scores ##

from numpy import std
min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    return z

min_z = z_score(min_val, houses['SalePrice'])
mean_z = z_score(mean_val, houses['SalePrice'])

max_z = z_score(max_val, houses['SalePrice'])

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

north_ames = houses[houses['Neighborhood'] == 'NAmes']
college_creek = houses[houses['Neighborhood'] == 'CollgCr']
old_town = houses[houses['Neighborhood'] == 'OldTown']
edwards = houses[houses['Neighborhood'] == 'Edwards']
somerset = houses[houses['Neighborhood'] == 'Somerst']

#zip the z-score for 200000
z_by_location = {}
for data, neighborhood in [(north_ames, 'NAmes'), (college_creek, 'CollgCr'),
                     (old_town, 'OldTown'), (edwards, 'Edwards'),
                     (somerset, 'Somerst')]:
    
    z_by_location[neighborhood] = z_score(200000, data['SalePrice'],
                                          bessel = 0)
print(z_by_location)

best_investment = 'College Creek'


## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses['z_prices'].mean()

z_stdev_price = houses['z_prices'].std(ddof = 0)


mean_area = houses['Lot Area'].mean()
st_dev_area = houses['Lot Area'].std(ddof = 0)
houses['z_area'] = houses['Lot Area'].apply(
    lambda x: ((x - mean_area) / st_dev_area))

z_mean_area = houses['z_area'].mean()
z_stdev_area = houses['z_area'].std(ddof = 0)

result1 = z_mean_area == z_mean_price
result2 = z_stdev_area == z_stdev_price

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]
mean_pop = mean(population)
stdev_pop = std(population, ddof = 0)

standardized_pop = []

for val in population:
    z = (val - mean_pop) / stdev_pop
    standardized_pop.append(z)

mean_z = mean(standardized_pop)
stdev_z = std(standardized_pop, ddof = 0)




## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample, ddof = 1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof = 0)

houses['z_1'] = houses['index_1'].apply(
    lambda x: (( x - mean_index1) /stdev_index1)
)

mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof = 0)

houses['z_2'] = houses['index_2'].apply(
    lambda x: (( x - mean_index2 ) / stdev_index2)
)

print(houses[['z_1', 'z_2']].head(2))

better = 'first'

## 9. Converting Back from Z-scores ##

mean = 50
st_dev = 10
houses['transformed'] = houses['z_merged'].apply(lambda z: (z * st_dev + mean))

mean_transformed = houses['transformed'].mean()
stdev_transformed = houses['transformed'].std(ddof = 0)