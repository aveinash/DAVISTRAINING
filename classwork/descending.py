# create list of 10 numbers
nums = [12, 5, 9, 21, 3, 15, 7, 18, 1, 10]

# length of list 
n = len(nums)

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] < nums[j]:   # swap for descending
            nums[i], nums[j] = nums[j], nums[i]

print("Sorted list (Descending):", nums)