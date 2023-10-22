## Exercise 5: Change Guest List

#people i would invite to dinner
guests = ["Alishba", "Amna", "Rabiya", "Mariam"]

#print message to each person inviting them to dinner
#first message
print (f"Hey, {guests [0]}. Do you want to get dinner together?")
#second message
print (f"Hey, {guests [1]}. Let's have dinner at my place and watch a movie together.")
#third message
print (f"Hey, {guests [2]}. It's been a while. Do you catch up over dinner?")
#fourth message
print (f"Hey, {guests [3]}. I'm inviting you to dinner at my place.")

#name of frined who won't be able to attend dinner
print (f"\n{guests [2]} will not be able to attend")
#replace the name of friend who can't attend dinner
guests [2] = "Khadeeja"
#print name of friend who will attend instead
print (f"Let's invite {guests [2]} instead.")

#invitation messages
print (f"\nHey, {guests [0]}. Do you want to get together for dinner?")
#invitation message
print (f"Hey, {guests [1]}. We are getting together for dinner. Do you want to join us?")
#new invitation message
print (f"Hey, {guests [2]}. It's been a while. Do you want to catch up over dinner?")
#invitation message
print (f"Hey, {guests [3]}. I'm inviting you to dinner at my place.")