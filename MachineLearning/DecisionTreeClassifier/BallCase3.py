from sklearn import tree

#Rough 1
#Smooth 0

#Tennis 1
#Cricket 2

def BallPredictor(waight,surface):
    Freatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[92,0]] 
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Freatures,Labels)#fit meathod internally perform training

    ret = obj.predict([[waight,surface]])

    if ret == 1:
        print("Tennis Ball")
    else:
        print("cricket Ball")





def main():
    print("_______________________________Ball preddictor case study_______________________________")

    print("Please Enter the waight of your object in grams")
    waight = int(input())

    print("Please Enter the type of surface (Rough / Smooth)")
    Surface = input()

    if Surface.lower() == "rough":
        Surface = 1
    elif Surface.lower() == "smooth":
        Surface = 0
    else:
        print("Invalid type of Surface")
        exit()
    

    BallPredictor(waight,Surface)


if __name__ == "__main__":
    main()