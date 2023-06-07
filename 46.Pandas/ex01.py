import pandas as pd

path = "./46.Pandas/sample.csv"
data = pd.read_csv(path)

# DataFrame : General 2D labeled, size-mutable tabular structure
# with potentitally heterogeneously-typed column
# print(type(data))
# print(data.to_dict())

# Series : 1D labeled homogeneously-typed array
# print(type(data['country']))
# print(data['country'].to_list())

# sum / max
# print(sum(data['population'].to_list()))
# print(data['population'].max())

# differct way to access to the column
# print(data.population)

# row data
# print(data[data.country == "USA"])
# print(data[data.population == data.population.max()])

# from scratch
# grade = {
#     "students": ["A", "B", "C"],
#     "scores": [90, 80, 85]
# }
# data = pd.DataFrame(grade)
# print(data)
# data.to_csv("./46.Pandas/grade.csv")