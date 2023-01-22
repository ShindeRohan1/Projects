import os
from sys import *
import shutil
import time 

def CopyFiles(Path_1,Path_2):
    flag = os.path.isabs(Path_1)
    if flag == False:
        path = os.path.abspath(Path_1)
    exists_path_1 = os.path.isdir(Path_1)

    
    flag2 = os.path.isabs(Path_2)
    if flag2 == False:
        path_of_2 = os.path.abspath(Path_2) 
    exists_path_2 = os.path.isdir(Path_2)
    if(exists_path_2 == False):
        os.mkdir(Path_2)
    

    if(exists_path_1):
 
        separator = "_" * 80
        
        log_path = os.path.join(Path_1,"FilesCopied.log")
        f = open(log_path,'w')
        f.write(separator +"\n")
        f.write("Application to copy all files from directory to directory :"+time.ctime() + "\n")
        f.write(separator + "\n")

        for foldername, subfolder, filenames in os.walk(Path_1):
            for fname in filenames:
                source = os.path.join(foldername,fname)
                destination = os.path.join(Path_2,fname)
                if os.path.isfile(source):
                    shutil.copy(source,destination)
                    f.write("%s\n" %fname)
                
            print(" ")
    else:
        print("invlaid inputs")



def main():
    print("Automation script started with name :",argv[0])

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This script will travel and copy all files from the given first  directory to second")
        exit()
    
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : application, name first directory name, second directory name ")
        exit()


    if(len(argv) != 3):
        print("Insufficient arguments")
        exit()
    
    try:
        CopyFiles(argv[1],argv[2])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input",E)
    

    
  

if __name__ == "__main__":
     main()
