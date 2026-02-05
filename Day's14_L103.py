import random
from Day14_L103_ import youtube_channels
score=0

while True:

    rand_num_A = random.randint(1,20)
    print(f"Compare A:{youtube_channels[rand_num_A]["name"]},a {youtube_channels[rand_num_A]["description"]} from {youtube_channels[rand_num_A]["country"]}")
    print("!!*******************V/S*******************!!")
    rand_num_B = random.randint(1,20)
    print(f"Compare B:{youtube_channels[rand_num_B]["name"]},a {youtube_channels[rand_num_B]["description"]} from {youtube_channels[rand_num_B]["country"]}")
    user_input = input("Who has more subscribers?, Type 'A' or 'B': ").lower()



    if user_input == "a":
        if youtube_channels[rand_num_A]["subscribers"] > youtube_channels[rand_num_B]["subscribers"]:
            score+=1
            print(f"You are right!! Current score:{score} ")
        else:
            print(f"Game Over!! Current score:{score} ")
            exit()

    elif user_input == "b":
        if youtube_channels[rand_num_B]["subscribers"] > youtube_channels[rand_num_A]["subscribers"]:
            score += 1
            print(f"You are right!! Current score:{score} ")
        else:
            print(f"Game Over!! Current score:{score} ")
            exit()
    else:
        print("Invalid input")
        exit()
