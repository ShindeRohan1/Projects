#Below application is used to demonstrate the creation of Data Frame using pandas
import pandas as pd 

print("Empty data frame")
df = pd.DataFrame()
print(df)

print("dataframe with list")
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

print("Data frame with list")
data = [['PPA',4],['LB',3],['Angular',5],['Python',9]]
df = pd.DataFrame(data)
print(df)

data = {'Name':['PPA','LB','ANGULAR','PYTHON'],'Duration':[6,7,4,2]}
df = pd.DataFrame(data)
print(df)

data = [{'Name':'PPA','Duration':4,'Fees':393939},{'Name':'LB','Duration':4,'Fees':3939},{'Name':'ANG','Duration':9,'Fees':3939}]
df = pd.DataFrame(data)
print(df)

d = {'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['x','y','z','h'])}
df = pd.DataFrame(d)
print(df)
print(df['one'])