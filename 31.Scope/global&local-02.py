my_score = 50 # global scope

def inside_value_function():
    global my_score # if u use global, u can touch it.
    my_score = 80
    print(f"my score inside is {my_score}")

inside_value_function()
print(f"my score outside is {my_score}")