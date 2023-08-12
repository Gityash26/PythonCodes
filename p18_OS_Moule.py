'''
_________________________________________________________________________________________________
==========================================OS Module==============================================
=================================================================================================

-> The OS module is a built-in module that provides a way to interact with the operating system functionalities. 
    It allows you to perform various operations related to file and directory management, process management, and other system-related tasks.


    
_________________________________________________________________________________________________
===================================Features of OS Module=========================================
=================================================================================================

1. File and Directory Operations:
   --> os.mkdir(path)      : Creates a new directory at the specified path.
   --> os.rename(src, dst) : Renames a file or directory from the source path to the destination path.
   --> os.listdir(path)    : Returns a list of files and directories in the given path.
   --> os.getcwd()         : Returns the current working directory.
   --> os.chdir(path)      : Changes the current working directory to the specified path.
   --> os.remove(path)     : Deletes a file at the specified path.

2. Path Manipulation:
   --> os.path.exists(path)      : Checks if a path exists.
   -> os.path.isfile(path)      : Checks if a given path is a file.
   -> os.path.isdir(path)       : Checks if a given path is a directory.
   -> os.path.basename(path)    : Extracts the base name of a file from a given path.
   -> os.path.dirname(path)     : Extracts the directory name from a given path.
   -> os.path.join(path1, path2, ...) : Joins multiple path components intelligently.

3. Process Management:
   -> os.system(command)   : Executes the specified shell command.
   -> os.popen(command)    : Opens a pipe to or from a command.
   -> os.kill(pid, signal) : Sends a signal to a process with the specified process ID.

'''


import os


def CreateDirectory(D_name):
    if not os.path.exists(D_name):
        os.mkdir(D_name)
        print(f"\n-> Directory ({D_name}) Created")

    else:
        print(f"\n-> Directory ({D_name}) already exists")


def RenameDirectory(Old_name,New_name):
    if not os.path.exists(Old_name):
        print(f"\n-> Directory ({Old_name}) Not exists")
    else:
        if not os.path.exists(New_name):
            os.rename(Old_name,New_name)
            print(f"\n-> Directory Renamed to : {New_name}")
        else:
            print(f"\n-> Directory ({New_name}) alreay exists")


def ShowFolder(D_name):
    if os.path.exists(D_name):
        print(f"\n-> Inside {D_name} : {os.listdir(D_name)}")
    else:
        print(f"\n-> Directory ({D_name}) Not exists")


def currentDirectory():
    print(f"Current directory : {os.getcwd()}")


def changeDirectory(path):
    if os.path.exists(path):
        os.chdir(path)
        print(f"\nPath changed to {os.getcwd()}")
    else:
        print("\nPath doesn't exist")

def Delete(path):
    if os.path.exists(path):
        os.removedirs(path)
        print(f"\nDelete sucessfully done")
    else:
        print("\nPath doesn't exist")


CreateDirectory("mydirectory")
RenameDirectory("mydirectory","NewDirectory")
ShowFolder("NewDirectory")
currentDirectory()
changeDirectory("C:\python projects")
changeDirectory("C:\python playlist")
Delete("mydirectory")


