import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    #load data
    data = pd.read_csv("WinePredictor.csv")

    #clean prepare and manipulate data
    label = data.Class
    

    feature_alcohol = data.Alcohol 
    feature_MalicAcid = data.Malicacid
    feature_Ash = data.Ash
    feature_Alcalinity_of_ash = data.Alcalinity_of_ash
    feature_Magnesium = data.Magnesium
    feature_Total_phenols = data.Total_phenols
    feature_Flavanoids = data.Flavanoids
    feature_Nonflavanoid_phenols = data.Nonflavanoid_phenols
    feature_Proanthocyanins = data.Proanthocyanins
    feature_Color_intensity = data.Color_intensity
    feature_Hue = data.Hue
    feature_Proline = data.Proline

    features = list(zip(feature_alcohol,feature_MalicAcid,feature_Ash,feature_Alcalinity_of_ash,feature_Magnesium,feature_Total_phenols,feature_Flavanoids,feature_Nonflavanoid_phenols,feature_Proanthocyanins,feature_Color_intensity,feature_Hue,feature_Proline))

    Data_train , Data_test , Target_train , Target_test = train_test_split(features , label , test_size = 0.3)

    #train data
    model = KNeighborsClassifier(n_neighbors=7)

    model.fit(Data_train,Target_train)

    #training data
    
    predicted = model.predict(Data_test)
 

    #calculate accuracy
    accuracy = accuracy_score(Target_test,predicted)
    print(accuracy*100)



    



if __name__ == "__main__":
    main()