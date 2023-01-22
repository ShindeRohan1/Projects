import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score

def HeadBrainPredictor():
    #Load Data 

    data = pd.read_csv("HeadBrain.csv")

    print("Size of dataset is",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))

    n = len(X)

    

    reg = DecisionTreeClassifier()
    reg  = reg.fit(X,Y)

    y_pred = reg.predict(X)

    Accuracy = accuracy_score(Y,y_pred)

    print(Accuracy*100)

def main():
    print("Linear Regression")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()