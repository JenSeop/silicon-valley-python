import datetime

current = datetime.datetime.now()
# print(current)

# print(current.year)
# print(current.month)
# print(current.day)
# print(current.hour)
# print(current.minute)
# print(current.second)
# print(current.microsecond)

# day_of_week = current.weekday()
# print(day_of_week)

# custom_date = datetime.datetime(
#     year = 2022,
#     month = 1,
#     day = 1
# )
# print(custom_date)

# string to datetime object
# datetime_object = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
# print(type(datetime_object))

# datetime object to string
# datetime_object = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
# datetime_str = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
# print(type(datetime_str))
# print(datetime_str)

# timedelta
# from datetime import timedelta

# datetime_object = datetime.datetime.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
# print(datetime_object + timedelta(days=1))