string = "HelloWorld!"
revString = []

for i in range(len(string)-1, -1, -1):
    revString.append(string[i])

print("origin =>", string)
print("reverse =>", "".join(revString))