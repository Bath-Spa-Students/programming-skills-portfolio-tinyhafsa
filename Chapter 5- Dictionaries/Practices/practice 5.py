''' Practice 5 - 
Write a Python program to merge two dictionaries into one.'''

#creating two dictionaries
one = {"The Book Thief": "Markus Zusak",
       "Good Omens": "Neil Gaiman, Terry Prachet",}
two = {"Hitchhiker's Guide to the Galaxy": "Douglas Adams",
       "The Dream Thieves": "Maggie Stiefvater"}

#merging one to two
one.update(two)

#printing merged dictionary
print("Books:", one)
