import os, shutil 
from pathlib import Path

print("in commands")

def list(abspath):
    print("Current Directory: ", abspath, "\n")

    command = "ls "+abspath
    os.system(command)

def makedir(name):
    os.mkdir(name)

def remdir(name):
    os.rmdir(name)

def valid(name):
    validity=Path(name).exists()
# v=1 if exists
    if(validity == 0):
        print("object not found. try again")
        exit()    
    return validity
    
def mvdir(object, dest):
    obj_validity= valid(object)

    Path(dest).mkdir(parents=True, exist_ok=True)

    if(dest==object):
        printf("same file")
        exit()
    else:
        shutil.move(object, dest)
    
    # take all paths as abs

def orchestra(abspath):
    list(abspath)
    


# ---

def readfile(filename):
    valid(filename)
    file = open(filename, "rb")
    

    # for line in file:
    print(file.read())
    file.close()
