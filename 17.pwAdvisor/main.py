import random

# 0 ~ 25
alphabetLowercase = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
alphabetUpercase = [
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
# 0 ~ 9
demicals = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
# 0 ~ 7
symbols = [
    '!', '@', '#', '$', '*', '+', '(', ')'
]
pwAdvise = []

length = int(input("set pw length =>"))

for i in range(length):
    pwCase = random.randint(0,3)
    if pwCase == 0: pwAdvise.append(alphabetLowercase[random.randint(0,25)])
    if pwCase == 1: pwAdvise.append(alphabetUpercase[random.randint(0,25)])
    if pwCase == 2: pwAdvise.append(demicals[random.randint(0,9)])
    if pwCase == 3: pwAdvise.append(symbols[random.randint(0,7)])
random.shuffle(pwAdvise)

print("What about this pw? =>", "".join(pwAdvise))