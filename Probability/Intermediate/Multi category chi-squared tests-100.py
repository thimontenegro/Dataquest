## 2. Calculating expected values ##

males_over50k = 0.241 * 0.67 * 32561
males_under50k  = 0.759 * 0.67 * 32561
females_over50k = 0.241 * 0.33 * 32561
females_under50k = 0.759 * 0.33 * 32561

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5257.6, 2589.6, 16558.2, 8155.6]

diffs = []

for i, obs in enumerate(observed):
    exp = expected[i]
    diff = ((obs - exp) ** 2) / exp 
    diffs.append(diff)

chisq_gender_income = sum(diffs)
   

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = [6662, 1179, 15128, 9592]
expected = [5257.6, 2589.6, 16558.2, 8155.6]

chisq_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas as pd

table = pd.crosstab(income['sex'], [income['race']])
print(table)

## 6. Finding expected values ##

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

table = pd.crosstab(income['sex'], [income['race']])
chisq_value, pvalue_gender_race, df, expect = chi2_contingency(table)