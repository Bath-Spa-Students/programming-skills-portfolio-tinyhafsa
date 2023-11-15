''' Practice 3 - 
Write a python program with nested decision structures that perform the following: 
If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2. '''

#assigning values to amount 1 and 2
amount1 = 14
amount2 = 45
#nested decision structures
#if amount 1 is more than 10
if amount1 > 10 :
    #if amount 2 is less than 100
    if amount2 < 100 :
        #if amount 1 is greater than amount 2
        if amount1 > amount2 :
            #printing greater value
            print (f"Greater value: {amount1}")
        #if amount 2 is greater than amount 1
        else:
            #printing greater value
            print (f"Greater value: {amount2}")
    #if amount 2 is more than 100
    else:
        print ("Amount 2 is greater thean 100")
#if amount 1 is less than 10
else:
    print ("Amount 1 is less than 10.")