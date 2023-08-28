import clss
print(clss.f3.func())

import clss as cs
print(cs.f3.func())

#from methds_class import f1
#print(f1.func())
#print(methds_class.f1.func())                   # NameError
#print(f3.func())                                # NameError

print(cs.__doc__)
print(dir(cs))                                   # ['Movies', '__builtins__', '__cached__', '_ ...
help(cs)

print(cs.__name__)                               # clss
