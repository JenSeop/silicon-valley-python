import random

alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# make answer
answer = list()
answerLen = int(input("answer lenght => "))
inputLen = answerLen
while answerLen != 0:
    answer.append(alphabet[random.randint(0,25)])
    answerLen-=1

# guess answer
space = 0
while inputLen != 0:
    if input("guess => ") == answer[space]:
        inputLen-=1
        space+=1
        print("ok!")
    else:
        print("no!")

# print answer
print("answer => ", "".join(answer))