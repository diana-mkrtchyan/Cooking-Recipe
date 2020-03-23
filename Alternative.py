oreoCake_recpie = {
  "time" : "90",
  "ingrediants for biscuit" : {
    "egg" : 6,
    "sugar" : {
      "sugar" : "300 gram",
      "alternative" : ["powdered sugar 400 gram" ]
    },
    "cacao" : "50 gram",
    "oil" : "100 gram",
    "vanila" : "1 pinch",
    "baking powder" : {
      "baking powder" : "10 gram",
      "alternative" : "soda 10 gram"
    },
    "flour" : "150 gram"
   },
   "ingrediants for cream" : {
     "cream cheese" : {
       "cream cheese" : "500-600 gram",
       "alternative" : "cottage cheese 500-600 gram"
      },
     "heavy cream" : "500 ml",
     "powdered sugar" : "150 gram",
     "oreo cookies" : "20 pieces",
     "dark chocolate" : "50 gram"
   },
}

dataToPrint = oreoCake_recpie["ingrediants for cream"]["cream cheese"]["alternative"]
print(dataToPrint)
