import numpy as np
from sklearn.cluster import KMeans

data = np.random.rand(100, 2)
k = 4

kmean = KMeans(n_clusters=k).fit(data)
labels = kmean.labels_

print("\nCluster Centers:")
print(kmean.cluster_centers_)

print("\nCluster Labels:")
print(labels)
