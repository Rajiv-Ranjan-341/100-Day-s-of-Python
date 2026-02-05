print("Welcome to rollercoaster")
height= float(input("Enter your height in cm: "))

if height >= 120:
    print("you can ride")
    age = int(input("Enter your age in years: "))
    if age <=12:
        print("you wil pay 50")
    elif age <=18:
        print("you will pay 100")
    else:
        print("you will pay 200")

else:
    print("you can't ride")