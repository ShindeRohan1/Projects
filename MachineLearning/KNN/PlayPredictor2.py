import numpy as np 
import pandas as pd 
from sklearn import preprocessing 
from sklearn.neighbors import KNeighborsClassifier



def MYPlayPredictor(data_path):

    #step 1 :load data
    data = pd.read_csv(data_path, index_col = 0)

    print("Size of Actual dataset",len(data))

    #step 2:Clean , Preapare and Manipulate Data

    features_names = ['Whether','Temperature']
    print("Names of Features",features_names)

    Whether = data.Whether
    Temperature = data.Temperature
    play = data.Play


    #creating labelEncoder
    le = preprocessing.LabelEncoder()


    #converting string labels into number

    weather_encoded = le.fit_transform(Whether)
    print("Encoded weather",weather_encoded)

    #converting string labels into number

    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    #combining weather and temp into single touples
    features = list(zip(weather_encoded,temp_encoded))
    print("zip features",features)

    #step 3:train data 
    model = KNeighborsClassifier(n_neighbors=3)

    #train the model using training sets

    model.fit(features,label)

    #step 4:test data

    predicted = model.predict([[2,2]])         #0 :Overcast  2:Mild
    print(predicted)

def main():

    print("Play predictor Application of ML  using KNN Algorithm")
    
    MYPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()



