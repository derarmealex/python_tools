def func():
    return "Hi, I'm Func"                                          # ...


func()                                                             # ...


def func():
    print("Hi, I'm Func")                                          # Hi, I'm Func


func()                                                             # ...


# or
def func():
    return "Hi, I'm Func"                                          # ...


print(func())                                                      # Hi, I'm Func


def func(origin):
    print("Its origin is " + origin)


func("Sun")                                                        # Its origin is Sun
func("Moon")                                                       # Its origin is Moon
func("Mars")                                                       # Its origin is Mars
func()                                                             # TypeError


def func(origin='Earth'):
    print("Its origin is " + origin)


func("Sun")                                                        # Its origin is Sun
func("Moon")                                                       # Its origin is Moon
func("Mars")                                                       # Its origin is Mars
func()                                                             # Its origin is Earth


def func(origin='Earth', when='a long ago'):                       
    return origin, when


print(func())                                                      # ('Earth', 'a long ago')
print(func("a long ago", "Earth"))                                 # ('a long ago', 'Earth')
print(func("Its origin is "))                                      # ('Its origin is ', 'a long ago')
print(func("Its origin is Mars"))                                  # ('Its origin is Mars', 'a long ago')


def func(when='a long ago', origin='Earth'):
    return origin, when


print(func())                                                      # ('Earth', 'a long ago')
print(func("a long ago", "Earth"))                                 # ('Earth', 'a long ago')
print(func("Its origin is "))                                      # ('Earth', 'Its origin is ')
print(func("Its origin is Mars"))                                  # ('Earth', 'Its origin is Mars')


def func(origin='Earth', when='a long ago'):
    return when, origin


print(func())                                                      # ('a long ago', 'Earth')
print(func("a long ago", "Earth"))                                 # ('Earth', 'a long ago')
print(func("Its origin is "))                                      # ('a long ago', 'Its origin is ')
print(func("Its origin is Mars"))                                  # ('a long ago', 'Its origin is Mars')


def func(x):
    print(5 * x)


func(3)                                                            # 15
func(5)                                                            # 25
func(9)                                                            # 45


def func(x=0):
    return 5 * x


print(func(1))                                                     # 5
print(func(3.5))                                                   # 17.5
print(func(-5))                                                    # -25
print(func())                                                      # 0


def func(x=0):
    return x


print(func(1))                                                     # 1
print(func(3.5))                                                   # 3.5
print(func(-5))                                                    # -5
print(func())                                                      # 0
