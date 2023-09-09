names = ["John", "Jane", "Doe"]

#enumNames = enumerate(names, 10)

#print(list(enumNames))                                 # [(10, 'John'), (11, 'Jane'), (12, 'Doe')]

enumNames = enumerate(names)
#print(enumerate(names))                                # <enumerate object>
#print(enumNames)                                       # <enumerate object at 0x0000022DAE05E520>
#print(list(enumNames))                                 # [(0, 'John'), (1, 'Jane'), (2, 'Doe')]
#print(dict(enumerate(names)))                          # {0: 'John', 1: 'Jane', 2: 'Doe'}
print(next(enumNames))                                  # (0, 'John')
print(next(enumNames))                                  # (1, 'Jane')
print(next(enumNames))                                  # (2, 'Doe')
#print(next(enumNames))                                  # StopIteration
#print([n for n in names])                               # ['John', 'Jane', 'Doe']
#print([n for n in enumNames])                           # [(0, 'John'), (1, 'Jane'), (2, 'Doe')]
for n, x in enumNames:
    print(f"№ {n} ==> {x}")                             # (0, 'John')
                                                        ##(1, 'Jane')
                                                        ##(2, 'Doe')
#EXTRACTION AND PROCESSING INDEXES
lst = [10, 20, 30, 40]

ix = 0
for number in lst:
    lst[ix] = number + 5 
    ix += 1
print(lst)                                              # [15, 25, 35, 45]
#or
for number in range(len(lst)):
    lst[number] += 5
print(lst)                                              # [15, 25, 35, 45]
#or
print([lst[number] + 5 for number in range (len(lst))]) # [15, 25, 35, 45]
#or
for ix, number in enumerate(lst):
    lst[ix] = number + 5
print(lst)                                              # [15, 25, 35, 45]
#or
print([number + 5 for ix, number in enumerate(lst)])    # [15, 25, 35, 45]