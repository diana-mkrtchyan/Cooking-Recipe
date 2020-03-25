import json
# read file
with open("data.json") as file:
  price_list = json.load(file)


dataToPrint = price_list["oreoCake"]["price"]
print(dataToPrint)
