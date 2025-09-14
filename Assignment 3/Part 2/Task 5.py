# 5. List operations
nums = [32, 54, 66, 11, 77, 10, 90]

# a. Remove items < 20
nums = [n for n in nums if n >= 20]
print("After removing <20:", nums)

# b. Sort ascending and descending
asc = sorted(nums)
desc = sorted(nums, reverse=True)
print("Ascending:", asc)
print("Descending:", desc)

# c. Compute average
average = sum(nums) / len(nums)
print("Average:", average)
