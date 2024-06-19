'''
Framework for ML Model 3: random forest regression

X is training sample array (n_samples, n_features)
y is class labels array (n_samples,)

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
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
X = dataset[:, 1:2].astype(int) # features
y = dataset[:, 2].astype(int) # target
x = 'things to predict'

features = ['list of features']
title = 'title of plot'
x_label = 'label of x'
y_label = 'label of y'

reg = RandomForestRegressor(n_estimators=10, random_state=0, oob_score=True)
reg.fit(X, y)

# making predictions on new data
preds = reg.predict(x)
mse = mean_squared_error(y, preds)
print(f'MSE: {mse}')

r2 = r2_score(y, preds)
print(f'R-squared: {r2}')

# visualise results
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)

plt.scatter(X, y, color='blue')
plt.plot(X_grid, reg.predict(X_grid), color='green')

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()

# visualise the dtree
# from sklearn.tree import plot_tree
# import matplotlib.pyplot as plt
#
# tree_to_plt = reg.estimators_[0] # pick which tree to visualise
# plt.figure(figsize=(20, 10))
# plot_tree(tree_to_plt, feature_names=[features], filled=True, rounded=True, fontsize=10)
# plt.title('Decision Tree from Random Forest')
# plt.show()