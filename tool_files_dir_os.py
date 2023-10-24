# mkdir(): создает новую папку
# rmdir(): удаляет папку
# rename(): переименовывает файл
# remove(): удаляет файл

import os

print(os.getcwd())                      # C:\Users\alexa\Desktop\py\python_tools
#os.chdir("C:\\Users\\alexa\\Desktop")
#print(os.getcwd())                      # C:\Users\alexa\Desktop
print(os.listdir())                     # ['.git', '.gitignore', 'bool_true_false_sic.py', 'input_name_pass.py', ...
os.mkdir("a")
print(os.listdir())                     # ['.git', '.gitignore', 'a', 'bool_true_false_sic.py', 'input_name_pass.py', ...
os.rename("a", "a2")
print(os.listdir())                     # ['.git', '.gitignore', 'a2', 'bool_true_false_sic.py', 'input_name_pass.py', ...
#os.remove("a")                          # PermissionError
# or
os.rmdir("a2")

os.system('cls')                                                           # clear console
print(os.name)                                                             # nt
print(os.cpu_count())                                                      # 4
print(os.path.isabs('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))    # True/False
print(os.path.isfile('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))   # True/False
print(os.path.isdir('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))    # True/False
print(os.path.islink('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))   # True/False
print(os.path.exists('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))   # True/False
print(os.path.lexists('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))  # True/False
print(os.path.basename('E:\\music\\Various Artists\\Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
                                                # Bob Kerrey-The Band Played Waltzing Matilda.mp3
print(os.path.getsize('E:\\music\\Various Artists\\Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
                                                # 4657964 [bytes]
print(os.listdir('E:\\music\\playlist'))        # ['AaRON - Birds in the Storm.flac', ...
for data in os.environ: print(os.environ[data]) # ...

import os.path, time
print("This file    : %s" % __file__)
print("Last modified: %s" % time.ctime(os.path.getmtime("../python_tools/.gitignore")))
print("Created      : %s" % time.ctime(os.path.getctime("../python_tools/.gitignore")))
print("Access time  : %s" % time.ctime(os.path.getatime("../python_tools/.gitignore")))
# This file    : C:\\Users\\alexa\\Desktop\\py\\python_syntax\\draft1_syntax.py
# Last modified: Fri Sep 15 13:46:48 2023
# Created      : Wed Sep 13 14:38:01 2023
# Access time  : Sun Sep 17 17:43:23 2023
