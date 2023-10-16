## Exercise 5: USB Shopper

#variable to store total money
total_money = 50
#price of each USB
each_usb = 6

#arithmetic operation to find number of USB the girl can buy
number_of_usb = (total_money//each_usb)
#arithmetic operation to calculate money remaining
money_left = (total_money%each_usb)

#print statement to reveal number of USB the girl can buy
print (f"She can buy {number_of_usb} USB sticks")
#print statement to reveal money remaining
print (f"She will have {money_left} pounds left.")