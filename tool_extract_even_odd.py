# EXTRACT EVEN/ODD
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd = []
even = []
for number in numbers:
    if number % 2 != 0:
        odd.append(number)
    else:
        even.append(number)
print("Odds :", ", ".join([str(num) for num in odd]))               # Odds : 1, 3, 5, 7, 9
print("Evens:", ", ".join([str(num) for num in even]))              # Evens: 2, 4, 6, 8
# or
odd = [number for number in range(1, 10) if number % 2 != 0]
even = [number for number in range(1, 10) if number % 2 == 0]
print("Odds :", ", ".join([str(num) for num in odd]))               # Odds : 1, 3, 5, 7, 9
print("Evens:", ", ".join([str(num) for num in even]))              # Evens: 2, 4, 6, 8
# or
print("Odds :", ", ".join([str(number) for number in range(1, 10) if number % 2 != 0]))
                                                                    # Odds : 1, 3, 5, 7, 9
print("Evens:", ", ".join([str(number) for number in range(1, 10) if number % 2 == 0]))
                                                                    # Evens: 2, 4, 6, 8
# EXTRACT EVEN/ODD AND COUNT THE DIFFERENCE
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd = 0
even = 0
for number in numbers:
    if number % 2 != 0:
        odd += number                                               # odd = odd + number
    else:
        even += number                                              # even = even + number
final = abs(even - odd)
print("Difference is:", final)                                      # Difference is: 5
# or
odd = [0 + number for number in range(1, 10) if number % 2 != 0]
even = [0 + number for number in range(1, 10) if number % 2 == 0]
print("Difference is:", abs(sum(even) - sum(odd)))                  # Difference is: 5
# BOOL EVEN/ODD
nums = range(0, 11)
# Odd - True
# Even - False
for x in nums:
    if x & 1:
        print(x, ": True", end=" ")
    else:
        print(x, ": False", end=" ")
# 0 : False 1 : True 2 : False 3 : True 4 : False 5 : True 6 : False 7 : True 8 : False 9 : True 10 : False
# or
for x in nums:
    if x % 2 != 0:
        print(x, ": True", end=" ")
    else:
        print(x, ": False", end=" ")
# 0 : False 1 : True 2 : False 3 : True 4 : False 5 : True 6 : False 7 : True 8 : False 9 : True 10 : False
# or
for x in nums:
    if not x & 1:
        print(x, ": False", end=" ")
    else:
        print(x, ": True", end=" ")
# 0 : False 1 : True 2 : False 3 : True 4 : False 5 : True 6 : False 7 : True 8 : False 9 : True 10 : False
# or
for x in nums:
    if x % 2 == 0:
        print(x, ": False", end=" ")
    else:
        print(x, ": True", end=" ")
# 0 : False 1 : True 2 : False 3 : True 4 : False 5 : True 6 : False 7 : True 8 : False 9 : True 10 : False
