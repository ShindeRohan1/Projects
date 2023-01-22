import shutil
from sys import *
import os

def Copy_File(File_name):
    if(os.path.exists(File_name)):
        DF = open("Demo.txt","w")
        
        shutil.copyfile( File_name , "Demo.txt")
    else:
        print("This file is not exists")
        return

def main():
    print("________________________Automation_________________________")

    print("Application name :",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to perform copy the content from given file to Demo.txt file")
        exit()
    
    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : provide two number of arguments as")
        print("First Arguments as : RupaliCopyContent.py")
        print("Second Arguments as : txt1.txt")
        exit()

    else:
        FileName = argv[1]
        Copy_File(FileName)


if __name__ == "__main__":
    main()
