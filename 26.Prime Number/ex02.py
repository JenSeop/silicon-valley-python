# is prime checker
def is_prime_number(num: int):
    if num > 1:
        is_divisible = False
        for n in range(2, num):
            if num % n == 0:
                print(f"{num} can be cleanly divided by {n}")
                is_divisible = True
                break
        if is_divisible:
             print("Snap! it is not the prime number")
        else:
            print(f"Congrat! {num} is a prime number")
    else:
        print(f"{num} is not the prime number")
# send number to prime checker
number = int(input("input number => "))
is_prime_number(number)