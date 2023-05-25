# A shallow copy constructs a new compound object and then
# (to the extent possible) inserts references into it to the objects
# found in the original.

a = [[1, 2], [2, 4]]
b = a[:] # shallow copy
b.append([3, 6])
print(b)
print(a)

b[0].append(3)
print(b)
print(a)