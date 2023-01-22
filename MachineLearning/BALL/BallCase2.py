from sklearn import tree

#Rough 1
#Smooth 0

#Tennis 1
#Cricket 2

Freatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[92,0]] 
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

obj = tree.DecisionTreeClassifier()

obj = obj.fit(Freatures,Labels)#fit meathod internally perform training

print(obj.predict([[97,0],[35,1],[43,1],[86,0]]))
