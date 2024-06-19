'''
Framework for ML Model 2: decision tree (regression)

X is training sample array (n_samples, n_features)
y is class labels array (n_samples,)
https://www.geeksforgeeks.org/python-decision-tree-regression-using-sklearn/
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import export_graphviz

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

plt_title = 'replace this with plot title'
x_label = 'replace with x-lab'
y_label = 'replace with y-lab'
out_name = 'replace with desired output tree file name' + '.dot'
feat_names = [] # feature names

# create & fit regressor
reg = tree.DecisionTreeRegressor(random_state=0)
reg.fit(X, y)

# predict new value
new_val = [3570]
y_pred = reg.predict([new_val])
print('Predicted y: % d\n' % y_pred)

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

# export the tree to tree.dot file
# export_graphviz(reg, out_file=out_name, feature_names=feat_names)


