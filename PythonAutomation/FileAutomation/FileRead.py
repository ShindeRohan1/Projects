import os
from sys import *
def ReadFile(FileName):
    flag = os.path.isabs(FileName)
    if flag == False:
        path = os.path.abspath(FileName)
    
    
    if(os.path.exists(FileName)):
        fd = open(FileName, "r")  
        Data = fd.read()
        print("Data from the file is ")
        print(Data)


        fd.close()
    
    else:
        print("File is not existing")
        return



def main():
    

    ReadFile(argv[1])


if __name__ == "__main__":
    main()
