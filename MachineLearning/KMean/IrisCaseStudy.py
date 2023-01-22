import numpy as np 
import matplotlib.pyplot as ptl 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
dataset = load_iris()
X = dataset.data


#Finding the optimum number of clusters for kmean classification
wcss=[]

for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++',max_iter = 300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


#Ploting the result onto a lineGraph ,allowing us to observe 'The elbow'
ptl.plot(range(1,11),wcss)
ptl.title('The elbow method')
ptl.xlabel('Number of cluster')
ptl.ylabel('wcss')  #within cluster sum of squares
ptl.show()


#Applying kmean to dataset / Creating the kmeans classifier
kmeans  = KMeans(n_clusters = 3,init = 'k-means++',max_iter = 300,n_init=10,random_state=0)
y_kmeans = kmeans.fit_predict(X)

print(y_kmeans)
#visualizing the clusters

ptl.scatter(X[y_kmeans == 0 , 0],X[y_kmeans == 0 , 1],s = 100, c = 'red', label = 'A')

ptl.scatter(X[y_kmeans == 1 , 0],X[y_kmeans == 1 , 1],s = 100, c = 'blue', label = 'B')

ptl.scatter(X[y_kmeans == 2 , 0],X[y_kmeans == 2 , 1],s = 100, c = 'green', label = 'C')


#Ploting the centroid of the cluster
ptl.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow',label='Centroids')

ptl.legend()
ptl.show()

