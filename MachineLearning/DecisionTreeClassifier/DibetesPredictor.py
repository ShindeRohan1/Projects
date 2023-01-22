import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    #get data
    Dataset = pd.read_csv("diabetes.csv")
    print(Dataset.head())

    #prepare and manipulate data
    target = Dataset.Outcome

    #features_Pregnancies = Dataset.Pregnancies
    features_Glucose = Dataset.Glucose
    #features_BloodPressure = Dataset.BloodPressure             overfitted
    #features_SkinThickness = Dataset.SkinThickness
    #features_Insulin = Dataset.Insulin
    features_BMI = Dataset.BMI
    features_DiabetesPedigreeFunction = Dataset.DiabetesPedigreeFunction
    features_Age = Dataset.Age 


    features = list(zip(features_Glucose  ,features_BMI,features_DiabetesPedigreeFunction ,features_Age ))

    Data_train , Data_test , Target_train , Target_test = train_test_split(features , target , test_size = 0.3)

    #train data
    model = DecisionTreeClassifier()
    

    model.fit(Data_train,Target_train)

    #test data

    predoction = model.predict(Data_test)


    #calculate Accuracy

    Accuracy = accuracy_score(Target_test,predoction)

    print(Accuracy * 100)





if __name__ == "__main__":
    main()