import random
#frist we make a list of words, then random choice it and print.
word_list = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
ch = random.choice(word_list)
heart_list = ['❤️', '❤️', '❤️', '❤️','❤️','❤️']
print(heart_list)

#Use a loop and the same word fill with blanks "_"
count=0
placeholder = ""
for i in ch:
    placeholder += "- "
    count += 1
print(f"The number of word is :{count}")
print(placeholder)


lives =6

game_over  = False
letter_list= []
while not game_over:

    user_guess = input("Enter your Guess:").lower()
    display = ""
    for letter in ch:
         if letter == user_guess:
            display += letter
            letter_list.append(user_guess)
         elif letter in letter_list:
            display += letter
         else:
            display += "_ "
    print(display)
    # print(letter_list)

    if user_guess not in display:
        lives -=1
        heart_list.pop()
        print(heart_list)
        if lives == 0:
            game_over = True
            print("!!game over!!")

    if "_ " not in display:
        game_over = True
        print("!!You Win!!")




