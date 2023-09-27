import os
def current_path():
    print("curent directory is before :")
    cwd=os.getcwd()
    print(cwd)
current_path()

os.chdir('../')
print("current directory after :")
current_path()

    