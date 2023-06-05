# file management
# write => w, read => r
# path = "./44.FILE IO/README.txt"
# file = open(path, 'r')
# print(file.read())
# file.close()

# memory management
# early days
# 1. Forgetting to free your memory
# 2. Freeing your memory too soon
# modern Language
# - GC

# no close any more
# path = "./44.FILE IO/README.txt"
# with open(path, "r") as file:
#     print(file.read())

# path = "./44.FILE IO/WRITEME.txt"
# with open(path, "a") as file:
#     print(file.write("Thanks"))