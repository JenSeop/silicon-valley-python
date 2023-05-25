my_score = 50 # global scope

def inside_value_function():
    my_score = 80 # local scope, new name space
    print(f"my score inside is {my_score}")

# global != local
inside_value_function()
print(f"my score outside is {my_score}")