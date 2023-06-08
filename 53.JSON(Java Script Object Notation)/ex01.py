# JSON(Java Script Object Notation)
import json

path = "./53.JSON(Java Script Object Notation)/"

with open(path + "sample.json", mode = "r") as f:
    data = json.loads(f.read())
    print(data)
    data['type'] = "drink"
    with open(path + "sample.json", mode = "w") as w:
        w.write(json.dumps(data))

print(type(data))
print(data)