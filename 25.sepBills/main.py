peopleCount = 0
howMuch = 0

def nullCheck(peopleCount: int, howMuch: int):
    if(peopleCount > 0 and howMuch > 0):
        print(f"people => {peopleCount} price => {howMuch}$")
        return 0
    else:
        return 1

def sepBills(peopleCount: int, howMuch: int):
    return howMuch / peopleCount

while nullCheck(peopleCount, howMuch):
    peopleCount = int(input("How many people? => "))
    howMuch = int(input("How much? => "))

sepPrice = int(sepBills(peopleCount, howMuch))
print(f"total price is {howMuch}$, so sep bills {sepPrice}$")