
import os

print('====os module overview====')
print("create path: " + os.path.join('home', 'ram', 'Test'))
print("get current dir: " + os.getcwd())
# os.chdir -- to change directory
print("seperator: " + os.sep)
print("get absolute path: " + os.path.abspath('fileHandling.py'))
xfile = os.path.abspath('fileHandling.py')
# os.path.isabs(pathname) -- to check for absolute path
print("dirname: " + os.path.dirname(xfile))
print("basename: " + os.path.basename(xfile))
print("check for file: " + str(os.path.isfile(xfile)))
print("check for dir: " + str(os.path.isdir(xfile)))
print("check file size: " + str(os.path.getsize(xfile)))
print("get list dir: " + str(os.listdir('/home/ram/Python')))
# os.makedirs()  -- to create the directories

# use shutil library to copy, move, rename files in through python
# open() to open a file
# -- use 'w' as 2nd arg for writing
# -- use 'a' as 2nd arg for appending
# read() -- read content of files
# readlines() -- readlines from file (returns list of lines)

# os.unlink(file) -- to delete single file
# os.rmdir(path) -- to remove empty dir
# shutil.rmtree(path) -- delete that dir with entire content in it
# all above delete permantely, use send2trash library to move to OS's recycle bin

print("====File search and delete code====")
os.chdir("/home/ram/Downloads/")
for filename in os.listdir():
    if filename.endswith(".zip"):
        print(filename)
        #os.unlink(filename)

print("====walking os paths====")
for folderName, subFolders, filenames in os.walk('/home/ram/Test/'):
    print("Folder name: " + str(folderName))
    print("Sub folders: " + str(subFolders))
    print("filenames: " + str(filenames))
    
    #walking through each subfolders
    for subfolder in subFolders:
        if 'some' in subfolder:
            pass

    #walking through each files
    for file in filenames:
        if file.endswith('.exe'):
            #copy that file, take a backup, move that file or rename
            pass
