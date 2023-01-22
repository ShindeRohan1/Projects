import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


diabetes = pd.read_csv("diabetes.csv")

print("Columns of dataset")
print(diabetes.columns)


print("First 5 records")
print(diabetes.head())


X_train , X_test ,Y_train, Y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],diabetes['Outcome'],stratify=diabetes['Outcome'],random_state = 66)

rf = RandomForestClassifier(n_estimators=100,random_state=0)

rf.fit(X_train,Y_train)

TrainingAccuracy = rf.score(X_train,Y_train)
print(TrainingAccuracy)


predicted = rf.predict(X_test)

Accuracy = accuracy_score(Y_test,predicted)
print(Accuracy*100)



