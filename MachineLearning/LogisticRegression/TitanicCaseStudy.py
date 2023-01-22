import pandas as pd 
from matplotlib.pyplot import figure,show
import matplotlib.pyplot as ptl 
from seaborn import countplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def TitanicLogistic():
    #step 1 Load data
    Titanic_data = pd.read_csv("TitanicDataset.csv")

    print("first 5 entries of loaded data set")
    print(Titanic_data.head())

    print("Number of passangers are "+str(len(Titanic_data)))

    #step2 analyze data
    print("visualization : Survived and non survived pasangers")
    figure()
    target = "Survived"

    countplot(data=Titanic_data,x=target).set_title("Survived and non survived passangers")
    show()

    print("Survived and non survived passangers based on dender")
    figure()
    target = "Survived"

    countplot(data = Titanic_data,x=target,hue="Sex").set_title("Survived and non survived passangers based on gender")
    show()

    print("Visualization : Survived and non survived based on the passanger class")
    figure()
    target = "Survived"

    countplot(data=Titanic_data,x=target,hue="Pclass").set_title("Survived and non survived based on the passanger class")
    show()

    print("Visualization : Survived and non survived based on the Age")
    figure()

    Titanic_data["Age"].plot.hist().set_title("Survived and non survived based on the Age")
    show()

    print("Visualization : Survived and non survived based on the Fare")
    figure()

    Titanic_data["Fare"].plot.hist().set_title("Survived and non survived based on the Fare")
    show()


    #stpe3 : Data Cleaning

    Titanic_data.drop("zero",axis = 1,inplace = True)

    print("First 5 entries from loaded dataset after removing zero column")

    print(Titanic_data.head())

    print("Values of Sex column")
    print(pd.get_dummies(Titanic_data["Sex"]))

    print("Value of sex column after removing one field")
    Sex = pd.get_dummies(Titanic_data["Sex"], drop_first = True)
    print(Sex.head())


    print("Value of Pclass column after removing one field")
    Pclass = pd.get_dummies(Titanic_data["Pclass"], drop_first = True)
    print(Pclass.head())


    print("values of data set after concatenating new columns")
    Titanic_data = pd.concat([Titanic_data,Sex,Pclass],axis = 1)

    print("values of data set after removing irrelevent columes")
    Titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis = 1, inplace = True)
    print(Titanic_data.head(5))


    X = Titanic_data.drop("Survived",axis = 1)
    Y = Titanic_data["Survived"]

    #step 4 : Data cleaning
    Data_train , Data_test , Target_train , Target_test = train_test_split(X,Y,test_size=0.5)

    logmodel = LogisticRegression()

    logmodel.fit(Data_train,Target_train)

    #step5 : Testing Data
    prediction = logmodel.predict(Data_test)

    #step 6 : calculate Accuracy

    print("Classsification report of logistic regression")
    print(classification_report(Target_test,prediction))

    print("Confussion matrix of logistic regression")
    print(confusion_matrix(Target_test,prediction))

    print("Accuracy score of Logistic regression")
    print(accuracy_score(Target_test,prediction))




def main():
    print("___________Logistic Regression on Titanic data set__________")

    TitanicLogistic()


if __name__ == "__main__":
    main()