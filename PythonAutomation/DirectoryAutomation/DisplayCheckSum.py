import os
from sys import *
import hashlib

def hashfile(path , blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayChecksum(Dir_Name):

    flag = os.path.isabs(Dir_Name)
    if flag == False:
        path = os.path.abspath(Dir_Name)
    
    exists = os.path.isdir(Dir_Name)
     
    if(exists):
        
        for foldername, subfolder, filenames in os.walk(Dir_Name):
            print("Current Folder is "+foldername)
            for fname in filenames:
                Dir_Name = os.path.join(foldername,fname)
                file_hash = hashfile(Dir_Name)
                print(Dir_Name)
                print(file_hash)
            print(" ")
    else:
        print("invlaid inputs")

    
def main():
    

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()
    
    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This script will travel the directory and display the checksum of files")
        exit()
    
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : application name ,dir name")
        exit()
    
    try:
        DisplayChecksum(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception:
        print("Error : Invalid input")
    

    
  

if __name__ == "__main__":
     main()
