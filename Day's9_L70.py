bid ={}
user_again = True

while user_again:
    User_name = input("Enter your name: ")
    User_bid = int(input("Enter you bid amount:💲"))

    bid[User_name] = User_bid

    user_want = input("Would you like to bid again y/n?: ").lower()
    if user_want == "y":user_again = True
    else:user_again = False


maxi=0
name=""
for key in bid:
    if bid[key] > maxi:
        maxi = bid[key]
        name=key
    else:
        maxi = maxi
print(f"Maximum bid is 💲{maxi} by {name} ")