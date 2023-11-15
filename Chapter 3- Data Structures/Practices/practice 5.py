''' Practice 5 - 
You have given a Python list. Write a program to find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of an item.
Work with the given list:
 list1 = [5, 10, 15, 20, 25, 50, 20]'''

#given list to be modified
list1 = [5, 10, 15, 20, 25, 50, 20]
#check if 20 is in the list
if 20 in list1:
    #first occurance of 20 in list1
    first_20 = list1.index(20)
    #raplcing the first 20 with 200
    list1[first_20] = 200
    #printing the updated list
    print("New list:", list1)
#if 20 is not found
else:
    #printing error statement
    print("20 is not found.")
