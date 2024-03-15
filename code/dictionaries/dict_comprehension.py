# Dictionary Comprehension Creation:

# mydict = {new_key:new_value for item in iterable}
# mydict = {new_key:new_value for (key, val) in dict.items()}

# conditional creation:
# mydict = {new_key:new_value for (key, val) in dict.items() if cond}

import random
cities = ["Bridgeport", "Waterbury", "Hartford",
          "New Haven", "Bristol", "Milford"]

city_temps = {city: random.randint(20, 30) for city in cities}
print(city_temps)

# temps_larger_25 = {temps for temps in city_temps if temps >= 25}
temps_larger_25 = {city: temp for (
    city, temp) in city_temps.items() if temp >= 25}
print("NEW: ", temps_larger_25)
