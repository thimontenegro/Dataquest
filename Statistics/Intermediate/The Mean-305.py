## 2. The Mean ##

def mean_mode(l):
    total = 0
    for i in range(len(l)):
        total += l[i]
    result = total / len(l)
    return result

distribution = [0,2,3,3,3,4,13]
mean = int(mean_mode(distribution))

center = False

dist_list_below_mean = []
dist_list_above_mean = []
for i in range(len(distribution)):
    if( distribution[i] >= mean):
        dist_list_above_mean.append(- mean + distribution[i])
    else:
        dist_list_below_mean.append(mean - distribution[i])
        distance = 0

below_mean = sum(dist_list_below_mean)
above_mean = sum(dist_list_above_mean)
equal_distances = ( below_mean == above_mean )

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
below_mean = []
above_mean = []
equal_distances = 0
for i in range(5000):
    seed(i)
    distribution = randint(0, 1000, 10)
    mean = sum(distribution) / len(distribution)
    
    for value in distribution:
        if value < mean:
            below_mean.append(mean - value)
        elif value > mean:
            above_mean.append(value - mean)
        else:
            continue
   
    sum_above = round(sum(above_mean), 1)
    sum_below = round(sum(below_mean), 1)
    
    if(sum_above == sum_below):
        equal_distances += 1

        

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def calculate_mean(l):
    total_sum = 0
    for val in l:
        total_sum += val 
    mean = total_sum / len(l)
    return mean 

mean_1 = calculate_mean(distribution_1)
mean_2 = calculate_mean(distribution_2)
mean_3 = calculate_mean(distribution_3)

    

## 6. Introducing the Data ##

houses = pd.read_csv('AmesHousing_1.txt', sep = '\t')
one = True
two = False
three = True

## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])
pandas_mean = houses['SalePrice'].mean()

means_are_equal = ( function_mean == pandas_mean)

## 9. Estimates from Low-Sized Samples ##

means = []

for i in range(10000):
    sample = houses['SalePrice'].sample(100, random_state = i)
    sample_mean = sample.mean()
    means.append(sample_mean)
    
plt.hist(means)
plt.axvline(houses['SalePrice'].mean(), color = 'red')
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0, 500000)


## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
population_mean = sum(population) / len(population)
sample_means = [[3,7], [3,2], [7,3], [7,2], [2,3], [2,7]]

means = []
for sample in sample_means:
    mean = sum(sample) / len(sample)
    means.append(mean)
mean_of_sample_means = sum(means) / len(means)

unbiased = (population_mean == mean_of_sample_means)