## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
print(wnba.head())
print(wnba.tail())

parameter = wnba['Games Played'].max()
sample = wnba['Games Played'].sample(30, random_state = 1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
sample_means = []
population_mean = wnba['PTS'].mean()

for i in range(100):
   result = wnba['PTS'].sample(10, random_state = i)
   sample_means.append(result.mean())

plt.scatter(range(1,101), sample_means)
plt.axhline(population_mean)
    

## 7. Stratified Sampling ##

wnba['Pts_per_game'] = wnba['PTS'] / wnba['Games Played']
#Stratifying 
stratum_C = wnba[wnba.Pos == 'C']
stratum_F = wnba[wnba.Pos == 'F']
stratum_FC = wnba[wnba.Pos == 'F/C']
stratum_G = wnba[wnba.Pos == 'G']
stratum_GF = wnba[wnba.Pos == 'G/F']
points_per_position = {}

for stratum, position in [(stratum_G, 'G'), (stratum_F, 'F'), (stratum_C, 'C'),
                (stratum_GF, 'G/F'), (stratum_FC, 'F/C')]:
    
    sample = stratum['Pts_per_game'].sample(10, random_state = 0)
    points_per_position[position] = sample.mean()

position_most_points = max(points_per_position, key = points_per_position.get)




## 8. Proportional Stratified Sampling ##

under_12 = wnba[wnba['Games Played'] <= 12]
btw_13_22 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)]
over_23 = wnba[wnba['Games Played'] > 22]

proportional_sampling_means = []
for i in range(100):
    sample_stratum_under_12 = stratum_under_12['PTS'].sample(1, random_state = i)
    sample_less_22 = stratum_less_22['PTS'].sample(2, random_state = i)
    sample_over_22 = stratum_over_22['PTS'].sample(7, random_state = i)
    
    final_sample = pd.concat([sample_stratum_under_12, sample_less_22, sample_over_22])
    proportional_sampling_means.append(final_sample.mean())
plt.scatter(range(1,101), proportional_sampling_means)
plt.axhline(wnba['PTS'].mean())

## 10. Cluster Sampling ##

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)
sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = sample.append(data_collected)

sampling_error_height = wnba['Height'].mean() - sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()
