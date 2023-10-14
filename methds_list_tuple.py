# .copy()
# .deepcopy()
# .extend()
# .append()
# .insert()
# .clear()
# .remove()
# .pop()
# .union()
# .reverse()
# .copy()
# .count()
# .index()
# .sort()
# reversed()
# sorted()
# sum()
# min()
# max()
# len()

# SORT
lst = ["wood", "0.35", "12", "Partei", "partei"]
print(sorted(lst))                                  # ['0.35', '12', 'Partei', 'partei', 'wood']
print(lst.sort())  									# None
lst.sort()
print(lst)                                          # ['0.35', '12', 'Partei', 'partei', 'wood']

lst2 = ["wood", 0.35, 12, "Partei", "partei"]
#print(sorted(lst2))                                 # TypeError
#print(lst2.sort())  								 # TypeError
#lst2.sort()										 # TypeError

tpl = ("wood", "0.35", "12", "Partei", "partei")
print(sorted(tpl))                                  # ['0.35', '12', 'Partei', 'partei', 'wood']
#print(tpl.sort())  								 # AttributeError
#tpl.sort()                                          # AttributeError

tpl2 = ("wood", 0.35, 12, "Partei", "partei")
#print(sorted(tpl2))                                 # TypeError
#print(tpl2.sort())  								 # AttributeError
#tpl2.sort()                                         # AttributeError

# MAP
print(tpl2[0])										# wood
print(tpl2[::2])                                    # ('wood', 12, 'partei')
print(tpl2[3::])                                    # ('Partei', 'partei')
print(tpl2[:-1])                                    # ('wood', 0.35, 12, 'Partei')
print(tpl2.index("partei"))                         # 4
print(tpl2.count('o'))                              # 0
print(tpl2.count('wood'))                           # 1
print(len(tpl2))                                    # 5
# REPLACE
lst[0] = 99
print(lst)                                          # [99, '0.35', '12', 'Partei', 'partei']
# or
numbers = list(range(1, 11))                        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    numbers[i] = 99
print(numbers)                                      # [99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
# EXTEND
#lst.add(100)										 # AttributeError
#print(lst.append(100))                              # None
lst.append(100)
print(lst)											# [99, '0.35', '12', 'Partei', 'partei', 100]

#print(lst + 100)                                    # TypeError
print(lst + [100])                                  # [99, '0.35', '12', 'Partei', 'partei', 100, 100]

#lst.extend(100)                                     # TypeError
#lst.extend('10')                                    # [99, '0.35', '12', 'Partei', 'partei', 100, 100, '1', '0']
lst.extend([10])
print(lst)                                          # [99, '0.35', '12', 'Partei', 'partei', 100, 100, 10]

lst2.insert(-2, "Wald")
print(lst2)                                         # ['wood', 0.35, 12, 'Wald', 'Partei', 'partei']
lst2.insert(3, "here we go")
print(lst2)                                         # ['wood', 0.35, 12, 'here we go', 'Wald', 'Partei', 'partei']
# REDUCE
lst2.pop(-2)
print(lst2)                                         # ['wood', 0.35, 12, 'partei']
print(lst2.pop(1))                                  # 0.35
print(lst2)											# ['wood', 12, 'partei']

lst2.remove(12)
print(lst2)                                         # ['wood', 'partei']

del lst2[0]
print(lst2)                                         # ['partei']

lst2.clear()
print(lst2)                                        	# []
del lst2
print(lst2)                                          # NameError

lst3 = list(range(7))                               # [0, 1, 2, 3, 4, 5, 6]
del lst3[1:5]
print(lst3)                                         # [0, 5, 6]

print(lst3.pop())                                   # 6
print(lst3)                                         # [0, 5]
# REVERSE
lst3.reverse()
print(lst3)                                         # [5, 0]
# or
print(list(reversed(lst3)))                         # [5, 0]
# or
print(lst3[::-1])                                   # [5, 0]
# CONCATENATE
x = ["a", "b"]
y = [1, 2]
print([x, y])                                       # [['a', 'b'], [1, 2]]  # list
print(x, y)                                         # ['a', 'b'] [1, 2]	 # tuple
print(x + y)                                        # ['a', 'b', 1, 2]

# ZIP
employee_numbers = [2, 9, 18, 28]
employee_names = ["Dan", "Mary", "Andrew", "Pat"]

zipped_values = zip(employee_names, employee_numbers)
print(zipped_values)                                # <zip object at 0x000002B13DF71B40>
zipped_values = list(zipped_values)
print(zipped_values) 	                            # [('Dan', 2), ('Mary', 9), ('Andrew', 18), ('Pat', 28)]
# or
for name, number in zip(employee_names, employee_numbers):
    print(f"{name}: {number}", end=' ')             # Dan: 2 Mary: 9 Andrew: 18 Pat: 28
# UNZIP
employee_names, employee_numbers = zip(*zipped_values)
print(employee_names)                               # ('Dan', 'Mary', 'Andrew', 'Pat')
print(employee_numbers)                             # (2, 9, 18, 28)
