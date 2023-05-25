# Assignment Operator(=)
# Assignment with an = on lists does not make a copy.
# Instead, assignment make the two variables point to the one list in memory.

colors = ['red', 'blue', 'green']
b = colors # colors adress copy => b = colors adr
b.append("white")
print(b)
print(colors)