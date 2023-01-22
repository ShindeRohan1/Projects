import numpy as np 
import pandas as pd 
import matplotlib.pyplot as ptl 

def HeadBrainPredictor():
    #load data

    data = pd.read_csv("HeadBrain.csv")
    print("Size of Data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    #Least Square method 
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    n = len(X)

    numerator = 0
    denumerator = 0


    #Equation of line is y = mx + c

    for i in range(n):
        numerator = numerator + (X[i] - mean_x) * (Y[i] - mean_y)
        denumerator = denumerator + (X[i] - mean_x)**2             #square

    m = numerator / denumerator

    C = mean_y - (m * mean_x)

    print("Slop of Regression line is :",m)
    print("Y intercept of Regression line is :",C)
    
    max_X = np.max(X)+100
    min_X = np.min(X)-100


    #Diaplay ploting of above points
    
    x = np.linspace(min_X,max_X,n)

    y = C + m * X

    ptl.plot(X,y,color='#58b970',label='Regression line')

    ptl.scatter(X,Y,color='#ef5423',label = "scatter plot")

    ptl.xlabel('Head size in cm3')

    ptl.ylabel('Brain weight in gram')

    ptl.legend()
    ptl.show()

    #Findout goodness of fit ie R square method
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = C + m * X[i]
        ss_t = ss_t + (Y[i] - mean_y) ** 2
        ss_r = ss_r + (Y[i] - y_pred) ** 2

    r2 = 1 - (ss_r/ss_t)

    print(r2)




def main():
    print("Superwise ML")
    print("Linear regration on head  and brain size of data")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()