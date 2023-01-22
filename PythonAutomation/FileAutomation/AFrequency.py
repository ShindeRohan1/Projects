import os 
from sys import *

def FindFreqency(File_name, String):
    if(os.path.exists(File_name)):
        fd = open(File_name, "r")
        Data = fd.readlines()
        iCnt = 0
        for word in Data:
            if word.find(String) != -1:
                iCnt = iCnt + 1
        print("Frequency is ::",iCnt)

    else:
        print("File is not exists")

def main():
    File_name = argv[1]
    String = argv[2]

    FindFreqency(File_name, String)

if __name__ == "__main__":
    main()