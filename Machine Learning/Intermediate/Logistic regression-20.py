## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt

admissions = pd.read_csv('admissions.csv')

plt.scatter(x = admissions['gpa'], y = admissions['admit'])
plt.show()

## 5. Training a logistic regression model ##

from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
linear_model.fit(admissions[["gpa"]], admissions["admit"])

from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(admissions[['gpa']], admissions['admit'])


## 6. Plotting probabilities ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

pred_probs = logistic_model.predict_proba(admissions[['gpa']])
label_0 = pred_probs[:,0]
label_1 = pred_probs[:,1]

plt.scatter(x = admissions['gpa'], y = label_1)
plt.show()

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
fitted_labels = logistic_model.predict(admissions[['gpa']])
plt.scatter(x = admissions['gpa'], y = fitted_labels)