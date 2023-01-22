import os 

def CheckFile(File_Name):
    if(os.path.exists(File_Name)):
        print("File is exists")
    else:
        print("File is not exists")

def main():
    
    print("Enter file name")
    fName = input()

    CheckFile(fName)


if __name__ == "__main__":
    main()