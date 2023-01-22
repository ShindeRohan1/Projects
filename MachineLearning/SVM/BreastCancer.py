from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn.metrics import accuracy_score



def SVM():

    #load Dataset
    cancer = datasets.load_breast_cancer()

    #print the name of the 13 features
    print("Features of the cancer datasets :",cancer.feature_names)

    #print the label type of the cancer
    print("Label of the cancer dataset :",cancer.target_names)

    #print data(feature) shape
    print("Shape of the dataset is :",cancer.data.shape)

    #print the cancer data features top 5 records
    print("First 5 records are ")
    print(cancer.data[0:5])


    #print the cancer labels (0;malignant , 1:benign)
    print("Target of Dataset :",cancer.target)

    #split the dataset into training set and testing set
    X_train , X_test , Y_train , Y_test = train_test_split(cancer.data , cancer.target , test_size = 0.3, random_state = 109)

    #Create the SVM classifier
    clf = svm.SVC(kernel="linear")#linear kernel

    #train model
    clf.fit(X_train,Y_train)

    #predict 
    y_pred = clf.predict(X_test)

    #Accuracy
    print("Accuracy of model is :",accuracy_score(Y_test,y_pred)*100)





def main():
    print("______________Support vector machine_______________")
    SVM()


if __name__ == "__main__":
    main()