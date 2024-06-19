'''
Framework for ML Model 4: clustering

X is training sample array (n_samples, n_features)
y is class labels array (n_samples,)

'''

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

plt_title = 'replace this with plot title'
x_label = 'replace with x-lab'
y_label = 'replace with y-lab'
feat_names = [] # feature names

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

inertias = []

for i in range(1, len(X)):
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(X, y)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, len(dataset)), inertias, marker='o')

plt.title(plt_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()


# plot with best cluster number
kmeans = KMeans(n_clusters=3)
kmeans.fit(X, y)

plt.scatter(X, y, c=kmeans.labels_)
plt.show()