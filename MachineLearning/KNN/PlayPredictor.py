from sklearn.neighbors import KNeighborsClassifier


#sunny = 1
#overcast = 2
#rainy = 3

#hot = 11
#cool = 12
#mild = 13

def PlayPredictor(weather,temperature):
    independant = [[1,11],[1,11],[2,11],[3,13],[3,12],[3,12],[2,12],[1,13],[1,12],[3,13]]
    depandant = [0,0,1,1,1,0,1,0,1,1]

    obj = KNeighborsClassifier()

    obj = obj.fit(independant,depandant)

    ret = obj.predict([[weather,temperature]])

    if(ret == 1):
        print("yes")
    else:
        print("no")


def main():
    print("______________________________PlayPredictor case study____________________________")
    print("Enter Weather condition")
    weather = input()

    print("Enter Temperature")
    temperature = input()

    if(weather.lower() == "sunny"):
        weather = 1
    elif(weather.lower() == "overcast"):
        weather = 2
    elif(weather.lower() == "rainy"):
        weather = 3

    if(temperature.lower() == "hot"):
        temperature = 11
    elif(temperature.lower() == "cool"):
        temperature = 12
    elif(temperature.lower() == "mild"):
        temperature = 13
    
    PlayPredictor(weather,temperature)

    


if __name__ == "__main__":
    main()