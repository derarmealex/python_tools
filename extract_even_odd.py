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
