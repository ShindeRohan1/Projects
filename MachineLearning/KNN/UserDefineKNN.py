from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class MyKNeighboursClassifier:
    def fit(self,trainingdata, trainingtarget):
        self.TrainingData = trainingdata
        self.TrainingTarget = trainingtarget


    def predict(self, TestData):

        predictions = []
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)

        return predictions

    def closest(self,row):
        minimumdistance = euc(row,self.TrainingData[0])
        minimumindex = 0

        for i in range(1,len(self.TrainingData)):
            Distance = euc(row,self.TrainingData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = i 
        return self.TrainingTarget[minimumindex]


    


def MyML():
    border = "_" * 50
    #load data
    Dataset = load_iris()  
    
    Data = Dataset.data
    Target = Dataset.target

    print(border)
    print("Actual data set :")
    print(border)
    for i in range(len(Dataset.target)):
        print("ID: %d, features %s Label: %s"%(i,Dataset.data[i],Dataset.target[i]))
    print("Size of Actual data set %d"%(i+1))
    
    #2 manipulate the data
    Data_train , Data_test , Target_train , Target_test = train_test_split(Data, Target, test_size = 0.5)#shufel

    print(border)
    print("Training data set :")
    print(border)
    for i in range(len(Data_train)):
        print("ID: %d, Features %s Labels: %s"%(i,Data_train[i],Target_train[i]))
    print("Size of taining data set %d"%(i+1))

    print(border)
    print("test data set :")
    print(border)
    for i in range(len(Data_test)):
        print("ID: %d, Features %s Labels: %s"%(i,Data_test[i],Target_test[i]))
    print("Size of test data set %d"%(i+1))

     
    Classifier = MyKNeighboursClassifier()
    
    
     #build the model
    Classifier.fit(Data_train,Target_train)

    predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, predictions)

    return Accuracy


def main():
    Ret = MyML()

    print("Accuracy of iris dataset with KNN is",Ret * 100)

if __name__ == "__main__":
    main()



