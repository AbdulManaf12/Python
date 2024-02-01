nums = [0, 1, 2, 3, 4]

# print(nums) # [0, 1, 2, 3, 4]
# print(nums[2]) # 2

#print(nums[10]) # IndexError: list index out of range

# for i in nums:
#     print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
    

#iterator
it = iter(nums)
print(it) # <list_iterator object at <index-value>
print(it.__next__()) # 0
print(it.__next__()) # 1

#another way to print the iterator
print(next(it)) # 2

#in order to print the first element again, we need to reinitialize the iterator
it = iter(nums)
print(next(it)) # 0
