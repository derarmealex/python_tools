def test(nums, n):
   return(all(x > n for x in nums))      
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(test(nums, 12))                               # False
print(test(nums, 5))                                # True

num = [2, 3, 4, 5]
print(all(x > 1 for x in num))                      # True
print(all(x > 4 for x in num))                      # False