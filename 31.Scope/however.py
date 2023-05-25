country = ["Republic of Korea"]

def inside_list_function():
    country.append("usa") # append use global name space
    # country = ["usa"] if u use redefine, that is local name space

inside_list_function()
print(country)