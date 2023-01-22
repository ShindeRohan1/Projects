import os

def DisplayFile(File_Name):
    if(os.path.exists(File_Name)):
        file_directory = open(File_Name ,"r")
        Data = file_directory.read()
        print(Data)
        file_directory.close()
        

    else:
        print("File is not exists")

def main():
    print("Enter file to display")
    File_Name = input()

    DisplayFile(File_Name)

if __name__ == "__main__":
    main()