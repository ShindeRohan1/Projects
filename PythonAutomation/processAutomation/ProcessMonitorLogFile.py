import os 
import psutil
import time 
import os
from sys import *
import schedule

def ProcessDisplay(log_dir):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass 
    
    separator = "_" * 80
    log_path = os.path.join(log_dir,"MarcellousLog.log")
    f = open(log_path,'w')
    f.write(separator +"\n")
    f.write("Marvellous Inosystem process loger :"+time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("_______________________________________________________")
    print("Application name ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to perform _________________")
        exit()
    
    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : provide ______number of arguments as")
        print("First Arguments as : ________")
        print("Second Arguments as : _________")
        exit()

    
    try:
        schedule.every(1).minutes.do(ProcessDisplay,argv[1])
        while(True):
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Invalid Data of input")
    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
