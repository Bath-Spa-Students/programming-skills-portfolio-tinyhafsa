'''Practice 1 -
Given a Python list, write a program to remove all occurrences of item 20.
Given list:
 list1 = [5, 20, 15, 20, 25, 50, 20]'''

#storing values in list
list1 = [5, 20, 15, 20, 25, 50, 20]
#starting a loop to run while the number 20 is in the list
while 20 in list1:
    #loop will run till till 20 is in the list
    list1.remove(20)
#printing list when loop ends and all 20 have been removed
print(list1)