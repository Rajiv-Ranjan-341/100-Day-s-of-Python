from sympy.codegen.ast import continue_

resource = {
    "water": 200,
    "milk": 200,
    "coffee": 260,
}
coffee =  {
    "espresso":{
        "ingredients": {
           "water": 50,
           "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 250,
        },
        "cost": 400,
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "milk": 200,
            "coffee": 250,
        },
        "cost": 250,
    },
}

def coffee_resource(flavour):
    for key in resource:
        if coffee[flavour]["ingredients"][key] <= resource[key] :
            resource[key] -= coffee[flavour]["ingredients"][key]

        else:
            print(f"Sorry, We don't have enough [{key} level = {resource[key]}]")
            exit()

# def ready_coffee(new_flavour):
#     print(f"Your {new_flavour} is now ready!")
run_once = 0
payment = 0
def coffee_prep(flavour):
    global run_once

    while True:
        global payment
        if run_once == 0:

            payment = int(input(f"Total Bill-{coffee[flavour]['cost']}💲 :"))
            run_once = 1

        if payment == coffee[flavour]['cost']:
            print("Preparing🍵......")
            print(f"Your {flavour} is now ready!")
            exit()
        elif payment > coffee[flavour]['cost']:
            extra = payment - coffee[flavour]['cost']
            print(f"You pay {extra}💲 extra for {flavour} which is cost {coffee[flavour]['cost']}💲")
            print(f"We will refund the extra amount {extra}💲")
            payment-=extra

        else:
            print("!!Bill is not clear yet!!")
            print("!!Try again later!!")
            exit()


user_input = input("What would you like? (Espresso/latte/cappuccino):☕ ").lower()
if user_input == "espresso":
    coffee_resource("espresso")
    coffee_prep(user_input)
elif user_input == "latte":
    coffee_resource("latte")
    coffee_prep(user_input)
elif user_input == "cappuccino":
    coffee_resource("cappuccino")
    coffee_prep(user_input)
else:
    print(f"Sorry, I didn't understand that.{user_input}")






