## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def get_range(array):
    max_element = max(array)
    min_element = min(array)
    result = max_element - min_element
    return result
range_by_year = {}

for year in houses['Yr Sold'].unique():
    sold_per_year = houses[houses['Yr Sold'] == year]
    range_by_year[year] = get_range(sold_per_year['SalePrice'])
one = False
two = True


## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]


def average_distance(array):
    mean = sum(array) / len(array)
    distances = []
    
    for value in array:
        distance = value - mean
        distances.append(distance)
    mean_distances = sum(distances) / len(distances)
    return mean_distances

avg_distance = average_distance(C)

print(avg_distance)
        

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def mean_absolute_deviation(array):
    absolute_deviation = sum(array) / len(array)
    distances = []
    
    for value in array:
        deviation = absolute_deviation - value
        deviation = abs(deviation)
        distances.append(deviation)
    
    result = sum(distances) / len(distances)
    return result
mad = mean_absolute_deviation(C)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def get_variance(array):
    mean = sum(array) / len(array)
    
    variance_distances = []
    for value in array:
        variance_distance = (mean - value) ** 2
        variance_distances.append(variance_distance)
        
    result = sum(variance_distances) / len(variance_distances)
    return result

variance_C = get_variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    distances = []
    
    for value in array:
        distance = (reference_point - value) ** 2
        distances.append(distance)
    
    result = sum(distances) / len(distances)
    return sqrt(result)

standard_deviation_C = standard_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

years = {}

for year in houses['Yr Sold'].unique():
    year_segment = houses[houses['Yr Sold'] == year]
    st_dev = standard_deviation(year_segment['SalePrice'])
    years[year] = st_dev

greatest_variability = max(years, key = years.get)
lowest_variability = min(years, key = years.get)

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)


bigger_spread = 'sample 2'

st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
sample_deviations = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    sample_deviation = standard_deviation(sample)
    sample_deviations.append(sample_deviation)

plt.hist(sample_deviations)
plt.axvline(standard_deviation(houses['SalePrice']), color = 'red')

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

pop_stdev = standard_deviation(houses['SalePrice'])
#plt.hist(st_devs)
#plt.axvline(pop_stdev)
from math import sqrt

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances) - 1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(pop_stdev)

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std(ddof = 1)
numpy_stdev = std(sample['SalePrice'], ddof = 1)

equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var(ddof = 1)
numpy_var = var(sample['SalePrice'], ddof = 1)

equal_vars = (pandas_var == numpy_var)

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
population_std = std(population, ddof = 0)


population_var = var(population, ddof = 0)
samples_std = []
samples_var = []

for sample in samples:
    samples_std.append(std(sample, ddof = 1))
    samples_var.append(var(sample, ddof = 1))

mean_std = sum(samples_std) / len(samples_std)
mean_var = sum(samples_var) / len(samples_var)

equal_stdev = (population_std == mean_std)
equal_var = (population_var == mean_var)
