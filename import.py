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
print(platform.python_version())
print(platform.system())

input()