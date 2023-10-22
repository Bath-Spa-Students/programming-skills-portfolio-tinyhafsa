##Exercise 7: Seeing the World

#make a list about countries i want to visit
countries = ["Japan" , "Turkey" , "Germany" , "Luxemberg" , "Greece"]
#print the list
print ("Original list:", countries)

#sort list alphabetically without changing the original list
print ("\nAlphabetical list:" , sorted (countries))
#prove that original list is unchanged
print ("Original list:" , countries)

#sort list reverse alphabetically without changing the original list
print ("\nReverse alphabetical list:" , sorted (countries, reverse=True))
#prove that original list is unchanged
print ("Original list:" , countries)

#reverse order of list
countries.reverse ()
#print reversed list
print ("\nReversed list:" , countries)

#reverse order again to change back to original
countries.reverse ()
#print list reversed back to original
print ("Original list:", countries)

#print list sorted alphabetically
countries.sort ()
#print alphabetically sorted list
print ("\nAlphabetical sort:" , countries)

#print list sorted reverse alphabetically
countries.sort(reverse=True)
#print alphabetically sorted list
print ("Reverse alphabetical sort:" , countries)