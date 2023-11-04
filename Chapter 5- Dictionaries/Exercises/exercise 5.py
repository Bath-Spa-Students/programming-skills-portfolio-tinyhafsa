# Exercise 5: Pets

#storing information of first pet in dictionary
pet1 = {"type": "snake",
        "name": "aoda",
        "owner": "sam",
        "color": "purple",
        "food": "rats"}

#storing information of second pet in a dictionary
pet2 = {"type": "cat",
        "name": "neko",
        "owner": "ken",
        "color": "orange",
        "food": "fish"}

#storing information of third pet in a dictionary
pet3 = {"type": "frog",
        "name": "gumba",
        "owner": "nate",
        "color": "blue",
        "food": "insects"}

#storing dictionaries in a list
pets = [pet1, pet2, pet3]

#using for loop to bring each dictionary from the list
for pet in pets:
    #displaying the introduction to each pet
    print(f"\nHere's what I know about {pet['name'].title()}:")
    #using for loop to bring the keys and values from each dictionary
    for key, value in pet.items():
        #displaying the information of each pet
        print(f"{key}: {value}")