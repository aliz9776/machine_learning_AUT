# -*- coding: utf-8 -*-
"""hw4_ML_Q6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rBh6H7_-iTMSvQQD2O09EdPainvyAnYW

**Problem 6: Synthetic Clusters | DBSCAN**

a )Write a command using sklearn.datasets.make_blobs to generate synthetic clusters and standardize the data.
"""

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Generate synthetic clusters
x, y = make_blobs(n_samples=100, centers=3, random_state=42)

# Standardize
sc = StandardScaler()
X_standardized = sc.fit_transform(x)

"""b) Provide the command to create a scatter plot to visualize the generated data."""

import matplotlib.pyplot as plt


plt.scatter(X_standardized[:, 0], X_standardized[:, 1], c=y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot')
plt.show()

"""c) Implement the DBSCAN algorithm using sklearn.cluster.DBSCAN on the standardized data."""

from sklearn.cluster import DBSCAN

# DBSCAN clustering
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X_standardized)

# Get the cluster labels
cluster_labels = dbscan.labels_

"""d) Write the command to access the resulting cluster labels and calculate the estimated number of clusters and noise points."""

import numpy as np

# Access the resulting cluster labels
cluster_labels = dbscan.labels_

# Calculate the estimated number of clusters
num_clusters = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)

# Calculate the number of noise points
num_noise_points = np.sum(cluster_labels == -1)

"""e) Write a command to evaluate the clustering performance using various metrics such as homogeneity, completeness, V-measure, adjusted Rand Index, adjusted mutual information, and silhouette coefficient using sklearn.metrics on the true labels and the DBSCAN cluster labels."""

from sklearn import metrics

# Evaluate clustering performance
homogeneity = metrics.homogeneity_score(y, cluster_labels)
completeness = metrics.completeness_score(y, cluster_labels)
v_measure = metrics.v_measure_score(y, cluster_labels)
adjusted_rand_index = metrics.adjusted_rand_score(y, cluster_labels)
adjusted_mutual_info = metrics.adjusted_mutual_info_score(y, cluster_labels)
silhouette_coefficient = metrics.silhouette_score(X_standardized, cluster_labels)

# Print the evaluation scores
print("Homogeneity: {:.3f}".format(homogeneity))
print("Completeness: {:.3f}".format(completeness))
print("V-measure: {:.3f}".format(v_measure))
print("Adjusted Rand Index: {:.3f}".format(adjusted_rand_index))
print("Adjusted Mutual Information: {:.3f}".format(adjusted_mutual_info))
print("Silhouette Coefficient: {:.3f}".format(silhouette_coefficient))