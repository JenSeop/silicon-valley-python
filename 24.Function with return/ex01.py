def getName(firstName, lastName):
    if firstName == "":
        return 1
    if lastName == "":
        return 1
    if firstName and lastName:
        return 0

firstName = ""
lastName = ""

while getName(firstName, lastName):
    firstName = input("first name => ")
    lastName = input("last name => ")

print(f"ur full name => {firstName}{lastName}")