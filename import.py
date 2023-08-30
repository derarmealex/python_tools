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
from math import *
print(pi)                                      # 3.141592653589793
print(math.pi)                                 # 3.141592653589793

import os
print(os.name)                                 # nt
print(os.cpu_count())                          # 4
print(listdir('E:\music\playlist'))            # ['AaRON - Birds in the Storm.flac', 'AaRON - Inner Streets.flac...
#print([f for f in listdir('E:\music\playlist') if isfile(join('E:\music\playlist', f))])
for data in os.environ:
    print(os.environ[data])                    # ...
print(os.path.isfile('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # True/False
print(os.path.exists('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # True/False
print(os.path.abspath('LesDeuxTimides(1928)_movietroll.avi')) # C:\Users\alexa\Desktop\LesDeuxTimides(1928)_movietroll.avi

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("dzagigrow-moon-calendar-2023.pdf")))#Last modified: Mon Jul 31 18:08:48 2023
print("Created: %s" % time.ctime(os.path.getctime("dzagigrow-moon-calendar-2023.pdf")))      #Created: Mon Jul 31 18:08:48 2023

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
