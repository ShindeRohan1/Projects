import os
from sys import *

def ReadFile(FileName,Word):
    flag = os.path.isabs(FileName)
    if flag == False:
        path = os.path.abspath(FileName)
    
    
    if(os.path.exists(FileName)):
        icnt = 0
        with open(FileName, "r") as file:
            for line_number, line in enumerate(file, start = 1):
                
                if Word in line: 
                    icnt = icnt + 1
                    print(f"word '{Word}' found at line {line_number}")
                
        print("Frequency is :",icnt)

        
    
    else:
        print("File is not existing")
        return



def main():
    

    ReadFile(argv[1],argv[2])


if __name__ == "__main__":
    main()
