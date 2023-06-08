# path = "./52.Try except/"
# with open(path + "sample-01.txt") as f:
#     data = f.read()
# print(data)

# File Not Found Error
# path = "./52.Try except/"
# try:
#     with open(path + "sample-02.txt") as f:
#         f.read()
# except FileNotFoundError:
#     print("FileNotFoundError occurs")

# Key Error
# try:
#     dict = {"k": "v"}
#     print(dict['no'])
# except KeyError as error_message:
#     print("KeyError occurs")
#     print(error_message)

# Index Error
# try:
#     country_list = ["USA", "South Korea", "Japan"]
#     pick_country = country_list[3]
# except IndexError:
#     print("IndexError occurs")

# Type Error
try:
    print(1 + "a")
    dict = {"K": "v"}
    print(dict['no'])
except TypeError:
    print("TypeError occurs")
else:
    print("this got triggered due to no error found")
finally:
    print("always running this")

# try : something may go wrong
# except : catch the error if there is an exception
# else : do this if no exception happens
# finally : always run either you have error or not

# if there is first exception, the rest does not move forward