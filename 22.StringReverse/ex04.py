string = "HelloWorld!"
stringList = list(string)
revString = []

while len(stringList) > 0:
    revString.append(stringList.pop())

print("origin =>", string)
print("reverse =>", "".join(revString))