print(bool(False and False == True))        #False
print(bool(False and False == False))       #False sic!

print(bool(False and True == True))         #False
print(bool(False and True == False))        #False sic!

print(bool(True and False == True))         #False
print(bool(True and False == False))        #True

print(bool(True and True == True))          #True
print(bool(True and True == False))         #False

print(bool(False or False == True))         #False
print(bool(False or False == False))        #True

print(bool(False or True == True))          #True
print(bool(False or True == False))         #False

print(bool(True or False == True))          #True
print(bool(True or False == False))         #True sic!

print(bool(True or True == True))           #True
print(bool(True or True == False))          #True sic!
