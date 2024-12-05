import os

path = 'tree' #input("path = ")
searchTarget = 'python' #input("dir = ")

os.chdir(path)
for dir1 in os.listdir():
    if dir1 == searchTarget:
        os.chdir(dir1)
        print(os.getcwd())
    print(dir1)
    os.chdir(os.getcwd() + '\\' + dir1)

    for dir2 in os.listdir():
        if dir2 == searchTarget:
            os.chdir(dir2)
            print(os.getcwd())
        print(os.getcwd())

    os.chdir('C:\ '+path)

