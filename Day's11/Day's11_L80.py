import random

def sum_calculation(list):
    """"
    This function is used to calculate the sum of all the numbers in list
    """
    sum_of_list =0
    for i in list:
        sum_of_list += int(i)#Our main list is String That's why we need to convert this to int for addition
    return sum_of_list


print("!!Let's goo!!")
card_list =['11','2','3','4','5','6','7','8','9','10','10','10','10']

computer= []
user = []

for card in range(2):

      computer.append(random.choice(card_list))

      user.append(random.choice(card_list))


print(f"Dealer card :['{computer[0]}', 'X']")
print(f"Player card :{user}")


user_hit =  input("\nDo you want to Hit? (y/n) ").lower()

if user_hit == 'y':
    user.append(random.choice(card_list))

    if sum_calculation(computer) < 19:
        computer.append(random.choice(card_list))

print(f"Player card :{user}")
print(f"Dealer card :{computer}")


if sum_calculation(user)>21:
    if sum_calculation(computer) > 21:
        print("!!Out!!")
elif sum_calculation(user)>21:
    print("!!You Loss!!")
elif sum_calculation(computer) == sum_calculation(user):
    print("!!Draw!!")
elif sum_calculation(computer) < sum_calculation(user):
    print("!!You Won!!")

else:
    print("!!You Loss!!")
