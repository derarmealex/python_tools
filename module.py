import clss
print(clss.f3.func())

import clss as cs
print(cs)                                   # <module 'clss' from 'C:\\Users\\alexa\\Desktop\\.py\\python_tools\\clss.py'>
print(cs.f3.func())                         # 1995, La Haine, black&white, director: Mathieu Kassovitz, actors: ...

#from methds_class import f1
#print(f1.func())
#print(methds_class.f1.func())              # NameError
#print(f3.func())                           # NameError

print(cs.__doc__)
print(dir(cs))                              # ['Movies', '__builtins__', '__cached__', '_ ...
print(sorted(cs.__dict__.keys()))           # ['Movies', '__builtins__', '__cached__', '_ ...
help(cs)                                    # Help on module clss: NAME clss CLASSES builtins.object Movies ...

print(cs.__name__)                          # clss
