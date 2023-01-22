import os
from sys import *
import shutil


def CopyContent(FileName):
    if(os.path.exists(FileName)):
        DF = open("Demo.txt","w")
        
        shutil.copyfile( FileName , "Demo.txt")



    else:
        print("This file is not exists")
        return

def main():
    
    FileName = argv[1]

    CopyContent(FileName)

if __name__ == "__main__":
    main()