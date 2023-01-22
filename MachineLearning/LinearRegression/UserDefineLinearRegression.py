import numpy as np 

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    mean_x = np.mean(X)
    mean_Y = np.mean(Y)
   
    numerator = 0
    denumerator = 0
    for i in range(0,len(X),1):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_Y))
        denumerator = denumerator + (X[i] - mean_x)**2

    Slop_of_line = numerator / denumerator

    print("Slope of the line is :",Slop_of_line)

    Y_Intercept = mean_Y - Slop_of_line * mean_x

    print("Y intercept is :",Y_Intercept)


    R2 = 0
    numerator = 0
    denumerator = 0
    for i in range(0,len(Y),1):
        YP = Slop_of_line * X[i] + Y_Intercept

        numerator = numerator + (YP - mean_Y)**2

        denumerator = denumerator + (Y[i] - mean_Y)**2


    R2 = (numerator /denumerator) * 100
    print("Accuracy is :",R2)


    
    



if __name__ == "__main__":
    main()

