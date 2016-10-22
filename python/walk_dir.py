import sys  
import platform  
import os  
from subprocess import *  
  
  
def main(input_dir):  
    if os.path.isfile(input_dir):  
        exit(1);  
    else:  
        for root, dirs, files in os.walk(input_dir):  
            for name in files:  
                filepath = os.path.join(root, name);  
                fileData = open(filepath, 'rb')
                data = fileData.read(6);  
                fileData.close();  
                print (filepath)  
                if data.lower() == "sqlite":  
                    print ("db=" + filepath)  
  
  
if __name__ == "__main__":  
    if len(sys.argv) != 2:  
        print("arg error ");  
        print("usage:python "+os.path.basename(sys.argv[0]) + " input_dir");  
        exit(1)  
    input_dir = sys.argv[1];  
    main(input_dir);  
    print ("finish!");  
    exit(0);  

