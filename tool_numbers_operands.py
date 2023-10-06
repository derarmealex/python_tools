# { }Скобки (объединение)
# f(args…)	Вызов функции
# x[index:index]
# x[index]
# x.attribute	Ссылка на атрибут
# ** = pow(x, y)
# *, /, %
# +, —
# <<, >>	Сдвиг влево/вправо
# &	Побитовое И
# ^	Побитовое ИЛИ НЕ
# |	Побитовое ИЛИ
# ~xПобитовое НЕТ
# in, not in, is, is not, <, <=, >, >=, <>, !=, ==
# not
# and
# or
# lambda

x = 2.8
y = 7.839999999999999

print(x ** 2)                   # 7.839999999999999
print(pow(x, 2))                # 7.839999999999999
print(y ** 0.5)                 # 2.8
print(y ** 0.5)                 # 2.8

print(complex("3"))             # (3+0j)
print(complex(3))               # (3+0j)
print(complex(3, 4))            # (3+4j)

print(type(x))                  # int
print(type(y))                  # float
print(type((3+4j)))             # complex

a = 35e3                        # float
b = 12E4                        # float
c = -87.7e100                   # float

print(float(a))                 # 35000.0
print(float(b))                 # 120000.0
print(float(c))                 # -8.77e+101
# COMMON FRACTIONS
import fractions
x = fractions.Fraction(6, 8)    # 3/4
y = fractions.Fraction(1, 3)    # 1/3
print(x + y)                    # 13/12
# MEMORY LOCATION
x = 35
x2 = 35
x3 = '35'
print(hex(id(x)))               # 0x7ff9d2bbe768
print(hex(id(x2)))              # 0x7ff9d2bbe768
print(hex(id(x3)))              # 0x1e72711a7b0
print(id(x))                    # 140710959114088
print(id(x2))                   # 140710959114088
print(id(x3))                   # 2092304541616
