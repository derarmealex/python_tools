#import <library>
#import <library> as <alias>
#from <library> import *
#from <library> import <object>
#from <library> import <object> as <alias>
import getpass
print(getpass.getuser())                       #

import math
#print(pi)                                     # NameError
print(math.pi)                                 # 3.141592653589793
print(int(math.modf(math.pi)[-1]))             # 3
print(round(math.modf(math.pi)[0], 2))         # 0.14
print('%.2f, %i' % math.modf(math.pi))         # 0.14, 3
print(math.floor(4.5))                         # 4
print(math.ceil(4.5))                          # 5
x = 2, 2
print(math.prod(x))                            # 4

from math import *
print(pi)                                      # 3.141592653589793
print(math.pi)                                 # 3.141592653589793

import os
print(os.name)                                 # nt
print(os.cpu_count())                          # 4
print(os.path.isabs('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))  # True/False
print(os.path.isfile('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # True/False
print(os.path.isdir('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))  # True/False
print(os.path.islink('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # True/False
print(os.path.exists('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # True/False
print(os.path.lexists('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))# True/False

#C:\Users\alexa\Desktop\Bob Kerrey-The Band Played Waltzing Matilda.mp3
print(os.path.basename('E:\music\Various Artists\Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
#Bob Kerrey-The Band Played Waltzing Matilda.mp3
print(os.path.getsize('E:\music\Various Artists\Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # 4657964 [bytes]
print(os.listdir('E:\music\playlist'))         # ['AaRON - Birds in the Storm.flac', 'AaRON - Inner Streets.flac...
#print([f for f in listdir('E:\music\playlist') if isfile(join('E:\music\playlist', f))])
#for data in os.environ:
#    print(os.environ[data])                   # ...

import os.path, time
print("File         : %s" % __file__)          #File: C:\Users\alexa\Desktop\.py\python_tools\import.py
print("Last modified: %s" % time.ctime(os.path.getmtime("dzagigrow-moon-calendar-2023.pdf")))#Last modified: Mon Jul 31 18:08:48 2023
print("Created      : %s" % time.ctime(os.path.getctime("dzagigrow-moon-calendar-2023.pdf")))#Created: Mon Jul 31 18:08:48 2023
print("Access time  : %s" % time.ctime(os.path.getatime("dzagigrow-moon-calendar-2023.pdf")))#Access time: Sat Sep  2 00:42:18 2023

import platform
print(platform.python_version())               # 3.11.5
print(platform.system())                       # Windows
print(platform.release())                      # 10
print(platform.machine())                      # AMD64
print(platform.architecture())                 # ('64bit', 'WindowsPE')
print(platform.architecture()[0])              # 64bit

import site
print(site.getsitepackages())                  # ['C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.11...

import socket
print(socket.gethostname())                    # DESKTOP-TD4SVJM
print(socket.gethostbyname('DESKTOP-TD4SVJM')) # 10.0.0.1

import sys
print(sys.version)                             # 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)]
print(sys.platform)                            # win32
print(sys.copyright)                           # Python Copyright Information...
#print(copyright)                               # -//-
print(sys.byteorder)                           # little/big
print(sys.builtin_module_names)                # ('_abc', '_ast', '_bisect', '_blake2', '_codecs' ...
print(sys.getsizeof())                         # ... bytes
print(sys.getrecursionlimit())                 # 1000
#sys.setrecursionlimit(1001)