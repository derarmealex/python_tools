# .copy()
# .find()
# .add()
# .update()
# .index()
# .clear()
# .remove()
# .discard()
# .pop()
# .reverse()
# .count()
# .union()
# sorted()
# sum()
# min()
# max()
# len()
# .difference()
# .difference_update()
# .intersection()
# .intersection_update()
# .isdisjoint()
# .issubset()
# .issuperset()
# .symmetric_difference()
# .symmetric_difference_update()

# SORT
st = set(["ddark", "dark", "0", "99", ".wood", "0dark"])
#st.sort()                                                # AttributeError
print(sorted(st))                                        # ['.wood', '0', '0dark', '99', 'dark', 'ddark']

st2 = set(("ddark", "dark", 0, 99, ".wood", "0dark"))
#st2.sort()                                               # AttributeError
#print(sorted(st2))                                       # TypeError

# MAP
print("0Dark" in st2)                                    # False
print("0dark" in st2)                                    # True
#print(st2[::2])                                          # TypeError

# EXTEND
st.add("grounds")
print(st)                                                # {'ddark', '99', '0', '.wood', '0dark', 'grounds', 'dark'}

st2.update({666, "ow"})
print(st2)                                               # {0, 99, 'ddark', 'ow', '.wood', '0dark', 666, 'dark'}

#print(st + '100')                                        # TypeError
#print(st + [100])                                        # TypeError

# REDUCE
st2.remove(0)
print(st2)                                               # {'.wood', 99, 'dark', '0dark', 'ddark'}

st2.pop()                                                # - random element

st2.clear()
print(st2)                                        	     # set()

del st
print(st)                                                # NameError

st3 = set(range(7))                                      # [0, 1, 2, 3, 4, 5, 6]
st3.discard(5)
print(st3)                                               # {0, 1, 2, 3, 4, 6}
st3.discard(10)
print(st3)                                               # {0, 1, 2, 3, 4, 6}

# CONCATENATE
st = {0, 1, 2, 3, 0}
st2 = {'99'}
fst = frozenset({2, 3, 4})
lst = [5, 6, 7]
tpl = (7, 8, 9)

print(st.union(st2, fst, lst, tpl))                              # {0, 1, 2, 3, 4, '99', 5, 6, 7, 8, 9}
#print(st & lst)                                                  # TypeError
#print(st & tpl)                                                  # TypeError
print(st & st2)                                                  # set()
print(st & st2 & fst)                                            # set()
print(st & fst)                                                  # {2, 3, 4}
print(fst & st)                                                  # frozenset({2, 3, 4})

#print(st | st2 | fst | lst | tpl)                                # TypeError
print(st | st2 | fst | frozenset(lst) | frozenset(tpl))          # {0, 1, 2, 3, 4, '99', 5, 6, 7, 8, 9}
print(st | st2 | fst | set(lst) | set(tpl))                      # {0, 1, 2, 3, 4, '99', 5, 6, 7, 8, 9}

#print(st | st2 | fst | lst | tpl)                                # TypeError
print(st | st2)                                                  # {0, 1, 2, 3, 4, '99'}
print(st2 | st)                                                  # {0, 1, 2, 3, 4, '99'}
print(st | fst)                                                  # {0, 1, 2, 3, 4, 5}
print(fst | st)                                                  # frozenset({0, 1, 2, 3, 4, 5})
print(st | st2 | fst)                                            # {0, 1, 2, 3, 4, 5, '99'}

a = {2, 3, 4, 5}
b = {1, 4, 5, 6}

print(a - b)                                                     # {2, 3}
# or
x = a.difference(b)
print(x)                                                         # {2, 3}

print(b - a)                                                     # {1, 6}
# or
x = b.difference(a)
print(x)                                                         # {1, 6}

x = a.difference_update(b)
print(x)                                                         # None
x = b.difference_update(a)
print(x)                                                         # None

x = a.intersection(b)
print(x)                                                        # {4, 5}
x = b.intersection(a)
print(x)                                                        # {4, 5}

x = a.intersection_update(b)
print(x)                                                        # None
x = b.intersection_update(a)
print(x)                                                        # None

#print(a + b)                                                     # TypeError
print(a ^ b)                                                     # {1, 2, 3, 4, 5, 6}
# or
x = a.symmetric_difference(b)
print(x)                                                         # {1, 2, 3, 4, 5, 6}

#print(b + a)                                                     # TypeError
print(b ^ a)                                                     # {1, 2, 3, 4, 5, 6}
# or
x = b.symmetric_difference(a)
print(x)                                                         # {1, 2, 3, 4, 5, 6}

x = a.symmetric_difference_update(b)
print(x)                                                        # None
x = b.symmetric_difference_update(a)
print(x)                                                        # None
