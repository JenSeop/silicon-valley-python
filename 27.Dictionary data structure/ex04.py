#dictionary
dict = {
# key : value
    1:{
        "country" : "south korea",
        "local" : "seoul",
    },
    2:{
        "country" : "japan",
        "local" : "tokyo",
    },
    3:{
        "country" : "china",
        "local" : "Beijing",
    },
    4:{
        "country" : "united states of america",
        "local" : "Washington D.C",
    },
    5:{
        "country" : "united states of kingdom",
        "local" : "London",
    }
}

for key, value in dict.items():
    print(f"{key}: {value}")