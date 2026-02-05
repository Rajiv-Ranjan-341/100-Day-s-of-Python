print("welcome in python pizza shop!")
size = input("Tell me the size of the pizza S/M/L :")
pepperoni = input("you want pepperoni? y/n :")
cheese = input("you want cheese? y/n :")
bill =0
if size =="S" or size =="s":
    bill = 15
    if pepperoni == "y":
        bill +=2
        if cheese == "y": bill +=1

elif size =="M"or size =="m":
    bill =20
    if pepperoni == "y":
        bill +=3
        if cheese == "y":bill += 1

elif size =="L" or size =="l":
    bill =25
    if pepperoni == "y":
        bill += 3
        if cheese == "y": bill += 1

else:
    print("thank you")

print(bill)

