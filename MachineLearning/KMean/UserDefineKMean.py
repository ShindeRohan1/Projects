#generate the dataset at runtime randomly and apply User define K-mean algorithm

import numpy as np 
import pandas as pd 
from copy import deepcopy
from matplotlib import pyplot as ptl 

def KMean():
    print("_______________________________________________________________")
    #set three centers , the model should predict similar results.
    center_1 = np.array([1,1])
    print(center_1)
    print("_______________________________________________________________")
    center_2 = np.array([5,5])
    print(center_2)
    print("_______________________________________________________________")
    center_3 = np.array([8,1])
    print(center_3)
    print("_______________________________________________________________")

    #Generate random data and center it to the three centers
    data_1 = np.random.randn(7,2) + center_1
    print("Elements of the first cluster with size "+str(len(data_1)))
    print(data_1)
    print("_______________________________________________________________")
    data_2 = np.random.randn(7,2) + center_2
    print("Elements of the second cluster with size "+str(len(data_2)))
    print(data_2)
    print("_______________________________________________________________")
    data_3 = np.random.randn(7,2) + center_3
    print("Elements of the third cluster with size "+str(len(data_3)))
    print(data_3)
    print("_______________________________________________________________")
    
    data = np.concatenate((data_1,data_2,data_3),axis = 0)
    print("Size of complete data set "+str(len(data)))
    print(data)
    print("_______________________________________________________________")

    ptl.scatter(data[:,0],data[:,1],s = 7)
    ptl.title("Input Dataset")
    ptl.show()
    print("_______________________________________________________________")

    #Number of clusters

    k = 3

    #Number of training data

    n = data.shape[0]
    print("Totle number of elements are",n)
    print("_______________________________________________________________")

    #Number of features in the data
    c = data.shape[1]
    print("Totle number of features are",c)
    print("_______________________________________________________________")

    #Generate random centers here we use sigma and mean to ensure it represent whole data
    mean = np.mean(data,axis=0)
    print("Value of the mean",mean)
    print("_______________________________________________________________")
    #Calculate standerd deviation
    std = np.std(data,axis=0)
    print("Value of std",std)
    print("_______________________________________________________________")

    centers = np.random.randn(k,c)*std + mean
    print("random points are",centers)
    print("_______________________________________________________________")

    #plot the data and centers generated as random 
    ptl.scatter(data[:,0],data[:,1],c='r',s=7)
    ptl.scatter(centers[:,0],centers[:,1],marker="*",c='g',s=150)
    ptl.title("Input dataset with random centroid")
    ptl.show()
    print("_______________________________________________________________")

    centers_old = np.zeros(centers.shape)         #to store old centers
    centers_new = deepcopy(centers)                #store new centers

    print("Value of old centroids")
    print(centers_old)
    print("_______________________________________________________________")

    print("Value of new centroids")
    print(centers_new)
    print("_______________________________________________________________")

    data.shape
    clusters = np.zeros(n)
    distences = np.zeros((n,k))

    print("Initial distences are")
    print(distences)
    print("_______________________________________________________________")

    error = np.linalg.norm(centers_new - centers_old)
    print("Value of error is ",error)

    #when , after an update , the enstimate of that center stays the same ,exit loop

    while error != 0:
        print("Value of error is ",error)
        #Measure the distance to every center
        print("Measure the distance to every center")
        for i in range(k):
            print("Itteration number ",i)
            distences[:,i] = np.linalg.norm(data - centers[i],axis=1)

        #Assign all training data to closest center
        clusters = np.argmin(distences,axis = 1)

        centers_old = deepcopy(centers_new)


        #Calculate mean for every cluster and update the center 
        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i],axis = 0)
        error = np.linalg.norm(centers_new - centers_old)

    #end while
    centers_new 

    #plot the data and centers generated as random 
    ptl.scatter(data[:,0],data[:,1],s=7)
    ptl.scatter(centers_new[:,0],centers_new[:,1],marker="*",c='g',s=150)
    ptl.title('Final data with centroid')
    ptl.show()       




    

def main():

    print("___________Unsupervised Machine Learing__________")
    print("Clustering Using K Mean Algorithm")

    KMean()


if __name__ == "__main__":
    main()