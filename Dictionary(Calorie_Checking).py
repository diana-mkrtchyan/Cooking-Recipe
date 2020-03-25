calories_100gram = {
  "fruits" : {
    "apple" : 50,
    "apricots" : 51.6,
    "banana" : 95,
    "blackberry" :  25.25,
    "blueberry" : 57,
    "cherry" : 39,
    "figs" : 45,
    "grapefruit" : 30,
    "grapes" : 65,
    "kiwi" : 49
  },
  "dairy" : {
    "egg" : 131,
    "milk" : 149,
    "cheese" : 404,
    "cottage cheese" : 163,
    "sour cream" : 214,
    "heavy cream" : 345
  },
}

dataToPrint = calories_100gram ["fruits"]["blackberry"]
print(dataToPrint)
