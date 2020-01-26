## 2. The Empirical Probability ##

heads = 56
total_times = 100
p_tail = (total_times - heads) / total_times
#Six died die 200 times
six = 28
times = 200
p_six = six / times

p_odd = 102/times

print(p_tail)
print(p_six)
print(p_odd)

## 3. Probability as Relative Frequency ##

p_heads_1 = (300 - 162) / 300
percentage_1 = p_heads_1 * 100

p_heads_2 = (5000 - 2450) / 5000
percentage_2 = p_heads_2 * 100

## 4. Repeating an Experiment ##

# INITIAL CODE
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'
    
probabilities = []
heads = 0

for n in range(1, 10001):
    outcome = coin_toss()
    if (outcome == 'HEAD'):
        heads += 1
    current_probability = heads / n
    probabilities.append(current_probability)
    
# Uncomment above and complete code from here

## 5. The True Probability Value ##

life_inserance = 87
life_car_inserance = 40
house_inserance = 63
one_type = 160
total = 200 
p_l = 87 / 200

p_l_and_c = 40 / 200

p_h = house_inserance / total 

p_no = (total - one_type) / total



## 6. The Theoretical Probability ##

p_5 = 1/6

p_ht = (1/2) * (1/2)

p_tt = (1/2) * (1/2)

## 7. Events vs. Outcomes ##

p_even = 3/6

p_odd_no_3 = 2 / 6

p_odd_greater_5 = 0


## 8. A Biased Die ##

p_blue = 10 / 100
p_red = 90 / 100