import pandas as pd 
import matplotlib.pyplot as ptl 

excel_file = "Students.xlsx"
data = pd.read_excel(excel_file)

print("All data from excel file")
print(data)

print("First 5 data")
print(data.head())


print("First 4 data")
print(data.head(4))

print("last 5 row")
print(data.tail())


print(data.shape)

Sorted_data = data.sort_values(['Name'],ascending=False)

print("sorted data")
print(Sorted_data)

data['Age'].plot(kind = "hist")
ptl.show()

data['Age'].plot(kind = "barh")
ptl.show()