# using file
# path = "./45.Comma Separated Value/sample.csv"
# file = open(path, "r")
# print(file.read())
# file.close()

# using csv package
# import csv
# path = "./45.Comma Separated Value/sample.csv"
# with open(path, "r") as data_file:
#     sample_data = csv.reader(data_file)
#     for row in sample_data:
#         if row[0] != "country":
#             print(row[0])

# using pandas
# import pandas as pd
# path = "./45.Comma Separated Value/sample.csv"
# data = pd.read_csv(path)
# print(data)

# print(data['country'])