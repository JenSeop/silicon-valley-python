# is prime?
def isPrime(ranges: int):
    if ranges == 1: # demi 1 pass
        return True
    checker = 2 # is prime check rule
    while checker != ranges:
        if ranges % checker == 0:
            return False
        else: checker+=1
    return True # prime return

# set prime range
ranges = ""
while ranges == "":
    ranges = input("set prime range => ")
if ranges != "":
    ranges = int(ranges)
# print prime numbers
num = 1
for num in range(ranges + 1):
    if isPrime(num): print(num)