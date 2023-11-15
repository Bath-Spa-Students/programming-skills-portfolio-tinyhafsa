''' Practice 4 - 
Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that
copies the values in numbers1 to numbers2.'''

#assigning 100 elemnents to list1
numbers1 = list(range(1, 101))
#copying list 1 to list 2
numbers2 = numbers1.copy() 

# Printing to verify the copy
print("Original List:", numbers1)
print("Copied List:", numbers2)

