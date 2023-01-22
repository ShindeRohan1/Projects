import os
from sys import *

def Directory_Watcher(Dir_Name):
    
    
    flag = os.path.isabs(Dir_Name)
    if flag == False:
        path = os.path.abspath(Dir_Name)
    
    exists = os.path.isdir(Dir_Name)

    if(exists):
        for foldername, subfolder, filenames in os.walk(Dir_Name):
            print("Folder name is "+foldername)
            for subf in subfolder:
                print("Subfolder name of "+foldername+" is "+subf)
            for fname in filenames:
                File_Path = os.path.join(foldername,fname)
                print("File inside folder "+foldername+" is "+fname+" having size " ,os.path.getsize(File_Path))
            print(" ")
    else:
        print("invlaid inputs")

    


def main():
    print("Directory watcher application")

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()#CLOSE THE APPLICATION
    
    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This script will travel the directory and display the name of all entries")
        exit()
    
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : application name dir name")
        exit()
    
    try:
        Directory_Watcher(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception:
        print("Error : Invalid input")
    

    
  

if __name__ == "__main__":
     main()
