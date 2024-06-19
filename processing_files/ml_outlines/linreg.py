'''
Framework for ML Model 1: linear regression

X is training sample array (n_samples, n_features)
y is class labels array (n_samples,)

'''

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

dataset = np.array(
[['Asset Flip', 100, 1000],
['Text Based', 500, 3000],
['Visual Novel', 1500, 5000],
['2D Pixel Art', 3500, 8000],
['2D Vector Art', 5000, 6500],
['Strategy', 6000, 7000],
['First Person Shooter', 8000, 15000],
['Simulator', 9500, 20000],
['Racing', 12000, 21000],
['RPG', 14000, 25000],
['Sandbox', 15500, 27000],
['Open-World', 16500, 30000],
['MMOFPS', 25000, 52000],
['MMORPG', 30000, 80000]
])

# input correct values for these
X = dataset[:, 1:2].astype(int)
y = dataset[:, 2].astype(int)

# replace following with necessary changes
feat_list = [895] # list of features for sample

plt_title = 'replace this with plot title'
x_label = 'replace with x-lab'
y_label = 'replace with y-lab'
feat_names = [] # feature names

# create & fit the linear regression object
reg = linear_model.LinearRegression()
reg.fit(X, y)

# predict on a sample
pred = reg.predict([feat_list])

# visualise results ----------------------------------------------

# create range of vals
X_grid = np.arange(min(X), max(X), 0.01)

# reshape data
X_grid = X_grid.reshape((len(X_grid), 1))

# scatter plot
plt.scatter(X, y, color='red') # orig data
plt.plot(X_grid, reg.predict(X_grid), color='blue') # predicted data

plt.title(plt_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.show()

