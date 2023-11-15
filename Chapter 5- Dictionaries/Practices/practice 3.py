''' Practice 3 - 
Write a Python program to iterate through the values of a dictionary and print them.'''

#creating a dictionary of book titles and authors
books = {"The Book Thief" : "Markus Zusak" , 
         "Good Omens" : "Neil Gaiman, Terry Prachet" , 
         "Hitchhiker's Guide to the Galaxy" : "Douglas Adams" , 
         "The Dream Thieves" : "Maggie Stiefvater"}
#iterating through the values of the dictionary
for author in books.values():
    #printing the values
    print (author)
