oreoCake_recpie = {
  "time" : {
    "portion" : 90,
    "metric" : "minutes",
  },
  "ingredients for biscuit" : {
    "egg" : 6,
    "sugar" : {
      "portion" : 300,
      "metric" : "grams",
      "alternative" : {
        "name" : "powedered sugar",
        "portion" : 400,
        "metric" : "grams"
      }
    },
    "cacao" : {
      "portion" : 50,
      "metric" : "grams"
    },
    "oil" : {
      "portion" : 100,
      "metric" : "grams"
    },
    "vanila" : {
      "portion" : 1,
      "metric" : "pinch"
    },
    "baking powder" : {
      "portion" : 10,
      "metric" : "grams",
      "alternative" : {
        "name" : "soda",
        "portion" : 10,
        "metric" : "grams"
      },
    },
    "flour" : {
      "portion" : 150,
      "metric" : "grams"
    },
  },
  "ingredients for cream" : {
    "cream cheese" : {
      "portion" : 550,
      "metric" : "grams",
      "alternative" : {
         "name" : "cottage cheese",
         "portion" : 550,
         "metric" : "grams"
      }
    },
    "heavy cream" : {
      "portion" : 500,
      "metric" : "milliliters"
    },
    "powdered sugar" : {
      "portion" : 150,
      "metric" : "grams"
    },
    "oreo cookies" : {
      "portion" : 20,
      "metric" : "pieces"
    },
    "dark chocolate" : {
      "portion" : 50,
      "metric" : "grams"
    },
  },
}

dataToPrint = oreoCake_recpie ["ingredients for cream"] ["cream cheese"] ["alternative"] ["name"]
print(dataToPrint)
