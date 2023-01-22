from sys import *
import os
import hashlib


def hashfile(path , blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()


def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
           
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid path")


def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1,dict1.values()))

    if len(results) > 0:
        print("Duplicates Found:")
        print("The following files are duplicate")
        icnt = 0
        for result in results:
            for subresult in result:
                icnt = icnt + 1
                print('\t\t%s'% subresult)
    else:
        print("No duplicate files found")



def main():

    print("________________________Automation_________________________")

    print("Automation script started with name :",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to perform traverse specific directory and display duplicate files")
        exit()
    
    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application name AbsolutePath_of _Directory Extension")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)
    except ValueError as E:
        print("Error : Invalid datatype of input",E)
    


if __name__ == "__main__":
    main()