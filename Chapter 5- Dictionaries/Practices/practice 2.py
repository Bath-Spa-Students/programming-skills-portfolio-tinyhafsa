''' Practice 2 - 
Write a Python program to iterate through the keys of a dictionary and print them.'''

#creating a dictionary of book titles and authors
books = {"The Book Thief" : "Markus Zusak" , 
         "Good Omens" : "Neil Gaiman, Terry Prachet" , 
         "Hitchhiker's Guide to the Galaxy" : "Douglas Adams" , 
         "The Dream Thieves" : "Maggie Stiefvater"}
#iterating through the keys
for titles in books.keys():
    #printing the keys
    print (titles)
