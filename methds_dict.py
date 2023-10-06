# .format()
# .update()
# .keys()
# .fromkeys()
# .items()
# .get()
# .values()
# .clear()
# .pop()
# .popitem()
# .copy()
# .setdefault()
# len()
# type()
# min()
# max()
# del
# |
# merge

# SORT
dct = {"name": "Alex", "surname": "Green", "2": "X", "Y": "3", "y": "/"}
print(dct)                  # {'name': 'Alex', 'surname': 'Green', '2': 'X', 'Y': '3', 'y': '/'}
print(sorted(dct))          # ['2', 'Y', 'name', 'surname', 'y']
print(sorted(dct.items()))  # [('2', 'X'), ('Y', '3'), ('name', 'Alex'), ('surname', 'Green'), ('y', '/')]
# MAPPING
my_dict = {"name": "Mike", "address": "123 Happy Way"}

#print(my_dict[0])                            # KeyError
#print(my_dict['Mike'])                       # KeyError
print(my_dict['surname'])                     # Brown

for x in my_dict:                             # name
    print(x)                                  ##address
for x in my_dict.keys():                      # name
    print(x)                                  ##address
for x in my_dict:                             # Mike
    print(my_dict[x])                         ##123 Happy day
for x in my_dict.values():                    # Mike
    print(x)                                  ##123 Happy day
for x in my_dict.items():                     # ('name', 'Mike')
    print(x)                                  ##('address', '123 Happy Way')
for x, y in my_dict.items():                  # name Mike
    print(x, y)                               ##address 123 Happy Way
# REPLACE
dct["surname"] = "Brown"    # {'name': 'Alex', 'surname': 'Brown', '2': 'X', 'Y': '3', 'y': '/'}
# UPDATE
employees = {}
employee01 = {}
employee01.update({"Name": "Marek"})
employee01.update({"Surname": "Parek"})
employee01.update({"Email": "marek.parek@gmail.com"})
employees["employee01"] = employee01
print(employees)        # {'employee01': {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}}
print(employee01)       # {'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}

employee02 = dict(Name="Matous", Surname="Svatous", Email="matous.svatous@gmail.com")
employees["employee02"] = employee02

employee03 = dict()
employee03["Name"] = "Anna"
employee03["Surname"] = "Rana"
employee03["Email"] = "anna.rana@gmail.com"
employees["employee03"] = employee03

employee04 = {}
employee04 |= {"Name": "Alex"}
employee04 |= {"Surname": "Brown"}
employee04 |= {"Email": "alex.brown@rhosgobel.com"}
employees["employee04"] = employee04

print("All the keys:", employees.keys())      # All the keys: dict_keys(['employee01', 'employee02', 'employee03', 'employee04'])
print("All the values:", employees.values())  # dict_values([{'Name': 'Marek', 'Surname': 'Parek', 'Email': 'marek.parek@gmail.com'}, {'Name': 'Matous' ...
print("All the details to the last employee:", employees["employee04"].items())
# dict_items([('Name', 'Alex'), ('Surname', 'Brown'), ('Email', 'alex.brown@rhosgobel.com')])

# BOOL
print("name" in my_dict)                      # True
print("Mike" in my_dict)                      # False
print(my_dict.get("name"))                    # Mike
print(my_dict["name"])                        # Mike

print("state" in my_dict)                     # False
print(my_dict.get("state"))                   # None
print(my_dict.get("state", "Catastrophe"))    # Catastrophe
#print(my_dict["state"])                       # KeyError

if "name" in my_dict:
    print("name")                             # name
    print(my_dict["name"])                    # Mike

if "state" in my_dict:
    print("state")                            # pass
    print(my_dict["state"])                   # pass

if "Mike" in my_dict:
    print("Mike")                             # pass

if "Mike" in my_dict.values():
    print("Mike")                             # Mike

print(my_dict | dct)
# {'name': 'Alex', 'address': '123 Happy Way', 'surname': 'Green', '2': 'X', 'Y': '3', 'y': '/'}
print(dct | my_dict)
# {'name': 'Mike', 'surname': 'Green', '2': 'X', 'Y': '3', 'y': '/', 'address': '123 Happy Way'}
# SUM
nums = {'a': 100, 'b': 200, 'c': 300, 'd': 120}
print(sum([0 + y for x, y in nums.items()]))       # 720
print(''.join(['' + x for x, y in nums.items()]))  # abcd
