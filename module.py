import methds_class
print(methds_class.f3.func())

import methds_class as cs
print(cs.f3.func())

#from methds_class import f1
#print(f1.func())
#print(methds_class.f1.func())                   # NameError
#print(f3.func())                                # NameError

print(cs.__doc__)
help(cs)