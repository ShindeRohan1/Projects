import os

def WriteFile(FileName):
    
    if(os.path.exists(FileName)):
        print("Enter the data you want to write in the file")
        Data =input()

        fd = open(FileName, "a") #a :append fd : filedistractor 
        fd.write(Data)
    
    else:
        print("File is not existing")
        return



def main():
    print("Enter the file name to create")
    Name = input()

    WriteFile(Name)


if __name__ == "__main__":
    main()
