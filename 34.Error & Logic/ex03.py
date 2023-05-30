import math

num_lst = [1, 2, 3, 4, 5]
minimum = math.inf
for n in num_lst:
    if n < minimum:
        minimum = n

# better solution
# minimum = min(num_lst)
# maximum = max(num_lst)

print(minimum)