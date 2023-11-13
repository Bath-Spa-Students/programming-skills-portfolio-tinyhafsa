# Exercise 5: Cities

#defining function with two parameters, one with a default value
def describe_city(city, country="Japan"):
    #message to be printed when function is called
    print(f"{city} is a city in {country}.")
#calling the function with different values for the parameters
describe_city ("Tokyo") #1 - country is default
describe_city ("Seoul", "South Korea") #2
describe_city ("Istanbul", "Turkey") #3