# # map function -------
def square(num):
    return num ** 2

# print(square(3))

number_list = [1, 2, 3, 4, 5]
# print(map(square, number_list))

# for i in map(square, number_list):
#     print(i)

# # or -------

# print(list(map(square, number_list)))

# # How about multiple arguments? -------
# def sum(a, b):
#     return a + b

# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7, 9]
# print(list(map(sum, list1, list2)))

# # filter function -------
def is_even(num):
    return num % 2 == 0

# print("Is number Even?", is_even(3))

number_list = [1, 2, 3, 4, 5]
print(list(filter(is_even, number_list)))