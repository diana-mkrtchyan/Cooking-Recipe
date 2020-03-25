import json
# read file
with open("data.json") as file:
  oreoCake_recpie = json.load(file)


dataToPrint = oreoCake_recpie ["ingredients for cream"] ["cream cheese"] ["alternative"] ["name"]
print(dataToPrint)
