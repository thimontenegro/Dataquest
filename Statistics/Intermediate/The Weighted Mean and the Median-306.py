## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()

difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']

sum_per_year = houses_per_year['sum_per_year'].sum()
total_n_houses = houses_per_year['Houses Sold'].sum()
weighted_mean = sum_per_year / total_n_houses

mean_original = houses['SalePrice'].mean()

difference = round(mean_original, 10) - round(weighted_mean, 10)

## 3. The Weighted Mean ##

import numpy as np
def weighted_mean(distribution, weights):
    weighted_sum = []
    for mean, weight in zip(distribution, weights):
        weighted_sum.append(mean * weight)
    
    return sum(weighted_sum) / sum(weights)

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])

weighted_mean_numpy = np.average(houses_per_year['Mean Price'],
        weights = houses_per_year['Houses Sold'])

equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
distribution2.sort(reverse = False)


median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

median_value = houses['TotRms AbvGrd'].replace('10 or more', 10).copy().astype(int).sort_values(ascending = True)
                                                                                                
median = (len(median_value -1 /2) + len((median_value )/2)) / 2  
middle_indices = [int((len(median_value) / 2) - 1), int((len(median_value) / 2))]
middle_values = median_value.iloc[middle_indices]

median = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt
houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()


mean_area = houses['Lot Area'].mean()
median_area = houses['Lot Area'].median()

mean_price = houses['SalePrice'].mean()
median_price = houses['SalePrice'].median()

lotarea_difference = mean_area - median_area
saleprice_difference = mean_price - median_price

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()

houses['Overall Cond'].plot.hist()
plt.show()

more_representative = 'mean'