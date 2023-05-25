# A deep copy constructs a new compound object and then,
# recursively, inserts copies into it of the objects
# found in the original.

a = [[1, 2], [2, 4]]
import copy
b = copy.deepcopy(a) # deep copy
b[0].append(4)
print(b)
print(a)

a[0].append(5)
print(b)
print(a)
# => totaly different object