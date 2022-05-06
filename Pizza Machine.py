print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
S = 15
M = 20
L = 25

if size == "S":
  bill += S
if size == "M":
  bill += M
if size == "L":
  bill += L

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
else:
  bill

if extra_cheese == "Y":
  bill += 1
else:
  bill

print(f"Your final bill is: ${bill}.")