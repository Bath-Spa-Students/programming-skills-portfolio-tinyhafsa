# Exercise 4: Rivers

#storing rivers and countries as keys and values in a dictionary
rivers= {"eel" : "united states" , #1
         "li" : "china" , #2
          "yenisei" : "mongolia" , #3
          "verdon" : "france" , #4
          "katsura" : "japan" #5
          }

#displaying the rivers and the countries they run through with for loop
for river,country in rivers.items():
    print (f"The {river.title()} river runs through {country.title()}.")

#displaying the rivers with for loop
print ("\nRivers:")
for river in rivers.keys():
    print (f"The {river.title()} river")

#displaying the countries with for loop
print ("\nCountries:")
for country in rivers.values():
    print (f"{country.title()}")