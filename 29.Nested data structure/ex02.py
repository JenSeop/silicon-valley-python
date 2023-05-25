usa = {
    "name" : "USA",
    "continent" : "North America"
}

korea = {
    "name" : "Republic of Korea",
    "continent" : "East Asia"
}

countries = [
   usa, korea
]

for country in countries:
    print(country["name"])
    print(country)