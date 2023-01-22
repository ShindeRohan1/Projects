from sys import *
import os

def FindExtention(dir_path, Extention):

    flag = os.path.isabs(dir_path)

    if(flag == False):
        path = os.path.abspath(dir_path)
    
    exists = os.path.isdir(dir_path)
    
    if(exists):
        for foldername, subfolder, filenames in os.walk(dir_path):
            
            for fname in filenames:
                file_path = os.path.join(foldername,fname)
                result = os.path.splitext(file_path)
                if(result[1] == Extention):
                    print(fname)
            print(" ")

    else:
        print("Invalid input")



def main():

    print("Automation script started with name :",argv[0])

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to search files of given Extention")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : provide  arguments as")
        print("First Arguments as : Name of Diretory")
        print("Second Arguments as : Extension")
        exit()

    if(len(argv) != 3) :
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    try:
        FindExtention(argv[1],argv[2])
    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()