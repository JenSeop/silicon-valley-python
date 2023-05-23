# input data
data = (float)(input("Plz input : "))

# condition & print
if isinstance(data,str):
    print(f"input data {data} is str")
elif isinstance(data,int):
    print(f"input data {data} is int")
elif isinstance(data,float):
    print(f"input data {data} is float")