def a():
    x = 10
    def b():
        nonlocal x
        x = 20
    b()
    print(x)
# nonlocal function access inclosing value
a()