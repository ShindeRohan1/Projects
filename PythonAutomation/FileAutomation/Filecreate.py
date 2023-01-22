import os
from sys import *

def CreateFile(FileName):
    
    if(os.path.exists(FileName)):
        print("File is already existing")
        return
    else:
        fd = open(FileName, "w")



def main():
   

    CreateFile(argv[1])


if __name__ == "__main__":
    main()
