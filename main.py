# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    pass;
  
  if extra_cheese == "Y":
    bill = bill + 1
  else:
    pass;
  print("Your bill is $" + str(bill))
elif size == "M":
  bill = 20

  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    pass;  

  if extra_cheese == "Y":
    bill = bill + 1
  else:
    print("Your bill is $" + str(bill))
elif size == "S":
  bill = 15

  if add_pepperoni == "Y":
    bill = bill + 3
  else:
    pass;

  if extra_cheese == "Y":
    bill = bill + 1
  else:
    print("Your bill is $" + str(bill))
else:
  print("Your bill is $" + str(bill))
