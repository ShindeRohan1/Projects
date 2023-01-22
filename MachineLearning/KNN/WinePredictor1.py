from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
def winePredictor():
    # load data
    wine = datasets.load_wine()

    #print name of the features
    print(wine.feature_names)

    #print name of the targets
    print(wine.target_names)

    #print top 5 wine data
    print(wine.data[0:5])

    #print wine target
    print(wine.target)

    #split dataset into training and testing dataset
    Data_train  , Data_test ,Target_train , Target_test = train_test_split(wine.data , wine.target,test_size=0.3)

    #create KNN classifier
    knn = KNeighborsClassifier(n_neighbors=3)

    #train the model
    knn.fit(Data_train,Target_train)

    #test the model
    predicted = knn.predict(Data_test)

    print("Accuracy :",accuracy_score(predicted,Target_test))





def main():
    print("_______Wine predictor application using KNN Algorithm_________ ")

    winePredictor()



if __name__ == "__main__":
    main()