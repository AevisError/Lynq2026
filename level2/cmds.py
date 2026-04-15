import os, shutil 
from pathlib import Path
# import organizer_mcp

print("in commands")

def abs_conv(filename):

    full_path = os.path.abspath(filename)
    if os.path.exists(full_path):
        return full_path
    
    ws_path = os.path.abspath(os.path.join("ws", filename))
    if os.path.exists(ws_path):
        return ws_path
        
    return full_path


# def list_files(abspath):
    # print("Current Directory: ", abspath, "\n")
# 
    # command = "ls "+abspath
    # os.system(command)
    # return os.listdir(abspath)

  
def list_files(directory): 
    full_path = os.path.abspath(directory)
    print(f"list files is running: Listing {full_path}")
    
    files = os.listdir(full_path)
    # print("\n".join(files)) #<--- debug
    return "\n".join(files)

def makedir(name):
    abs_conv(name)
    os.mkdir(name)

    return name

def remdir(name):
    abs_conv(name)
    os.rmdir(name)

    return 1

def valid(name):
    validity=Path(abs_conv(name)).exists()
# v=1 if exists
    if(validity == 0):
        print("item not found. try again")  
    return validity
    
def move_file(item, dest):

    item = abs_conv(item)
    dest = abs_conv(dest)
    print(f"in move file: moving {(item)} to {(dest)}")
    value =0


    if (valid((item)) ==0):
        print("not a valid location")
        return 0

    Path((dest)).mkdir(parents=True, exist_ok=True)

    if((dest)==(item)):
        print("same file")
        return 0
    else:
        shutil.move((item),(dest))
        print("move is successful")
        return 1
    


    # take all paths as abs


# ---

def read_file(filename):
    abs_conv(filename)

    if (valid(filename) ==0):
        exit()
    file = open(filename, "rb")
    

    # for line in file:
    file_data=file.read()
    file.close()
    print(file_data)
    return file_data

def send_file(filename):
    abs_conv(filename)

    valid(filename)

    organizer_mcp.send_file(filename)

    return 1
    # organizer_mcp.deletefiles_incloud()