import os
from sys import *

def CompareData(File1 , File2):
    if(os.path.exists(File1) & os.path.exists(File2)):
        fd1 = open(File1, "r")
        Data1 = fd1.read()

        fd2 = open(File2, "r")
        Data2 = fd2.read()

        if(Data1 == Data2):
            print("Data is same")
        else:
            print("Data is not same")

    else:
        print("check the files")

def main():
    File1 = argv[1]
    File2 = argv[2]

    CompareData(File1, File2)

if __name__ == "__main__":
    main()

