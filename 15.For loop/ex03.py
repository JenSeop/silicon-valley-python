# find max val
nums = [1, 3, 5, 4, 2, 8, 6, 7, 9, 10]
ismax = nums[0]
ismin = nums[9]

for num in nums:
    if num > ismax:
        ismax = num
    if num < ismin:
        ismin = num

print("my max => ", ismax)
print("lib max => ",max(nums))

print("my min => ", ismin)
print("lib min => ",min(nums))