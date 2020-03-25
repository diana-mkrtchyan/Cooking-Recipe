import json
# read file
with open("data.json") as file:
  calories = json.load(file)


dataToPrint = calories["grilled salmon"]["calories"]
print(dataToPrint)
