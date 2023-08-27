#import <library>
#import <library> as <alias>
#from <library> import *
#from <library> import <object>
#from <library> import <object> as <alias>
import math
#print(pi)                                          # NameError
print(math.pi)                                      # 3.141592653589793
from math import *
print(pi)                                           # 3.141592653589793
print(math.pi)                                      # 3.141592653589793

import sys
print(sys.version)                                  # 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)]
print(sys.platform)                                 # win32

import os
print(os.name)                                      # nt

import platform
print(platform.python_version())                    # 3.11.5
print(platform.system())                            # Windows
print(platform.release())                           # 10
print(platform.machine())                           # AMD64
print(platform.architecture())                      # ('64bit', 'WindowsPE')
print(platform.architecture()[0])                   # 64bit

import os.path
print(os.path.isfile('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) # True/False
print(os.path.exists('Bob Kerrey-The Band Played Waltzing Matilda.mp3')) #True/False

import site
print(site.getsitepackages())                       # ['C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.11...
