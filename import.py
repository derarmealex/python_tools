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
print(sys.version)

import platform
print(platform.python_version())                    # 3.11.5
print(platform.system())                            # Windows
print(platform.architecture())                      # ('64bit', 'WindowsPE')
print(platform.architecture()[0])                   # 64bit

import os.path
print(os.path.isfile('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
print(os.path.exists('Bob Kerrey-The Band Played Waltzing Matilda.mp3'))
