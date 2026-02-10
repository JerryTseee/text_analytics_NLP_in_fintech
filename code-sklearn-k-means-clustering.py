# This script illustrates how to use k-means clustering in
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

X = np.array(
        [[1, 2],
         [1, 4],
         [1, 0],
         [10, 2],
         [10, 4],
         [10, 0]])

# Perform k-means clustering of the data into two clusters.
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
kmeans.labels_
centers = kmeans.cluster_centers_



plt.figure(figsize=(8, 6))

# Visualize the clusters
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=100, alpha=0.7, edgecolor='black')
    
# Plot the cluster centers
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centroids')

# Predict and plot new points
new_points = np.array([[0, 0], [12, 3]])
new_labels = kmeans.predict(new_points)
plt.scatter(new_points[:, 0], new_points[:, 1], c=new_labels, s=150, marker='*', edgecolor='black', label='New points')

# Add labels and legend
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering Results (k=2)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()