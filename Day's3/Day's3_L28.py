print('''
                                    ,'^--__
                                   /     / ^^--_
                                  /    ./     ,'^-.
                                 /`.  / ^-_ ,'     `.               ,--.
                                 |   /     ^-_     _-\           ,--^--^-.
                                 \   \        \_-     \         /         \
                                 .>  /    `.-_|        \        | ,--^^^-- \
                            ,.-^^ \,'     / `.`.       ~\       |/        ' \
                            `'--~~'       |   `.`.      `._-^>  |           |
                                          |     `.\     ,'_-^   |           |
                                          \       \\   /,' /    \           |
                                           \O      \`.'/  /      \   ,-^^-_ |
                                            \       / \O_/        \ (__--\ \/
                                             \,'^`.     |          `,^--_ \ \
                                             / i . `-___\         ,^--_. ^^--_.
                                            (+-+-+-+-+-\         '_',-:.^-_ >  \
                                             \ l '_-''^~/'         |   |   >   |
                                              `.,'    ,'           |   |       |
                                              /     ,'             |   |      /
                                             /    ,' __--__         \_/      /
                                      __---^/   ,'_-^      ^-_       |      |
                         ,--,--^^^--,'     /    ,'            `.     \      |
                       ,'  /     ,':^-__----^^^/                \     |    /
                     ,'        ,' ,'`^--^^,','/          _-^^^-_|     |    |
                    /         / ,'      ,','  |        ,'       `.    |    |
                   /   /     / /      ,','            (           \  /      \
                   |  /     / /     ,','               \           \'        i
                   |  |.   / /    ,','                 |          /          |
                   /  \ ^-_| |  ,','                   |         /\          |
                  i    \   | |,','-___               _-^\       i  `.        |
                  |    /   \ ','      ^^^^---____--^^    \      \    ^-_     |
                  |   /    / <                   /        `.     `.     ^^--_l
                  \  /    / /\`.               ,'           `.     ^-_      /
             ,-^^-J  |   / /  \ \           _-^               `.      ^^--_/
._-^~~^.   ,'  `.`.   \ / /    \ \        ,'                    `-_      ,'
|`---'  ^v^      \ \   Y /      \ \     :'                         ^-__.'
|-_____)          \ \ / /        \ \     |
|-_____)          | /| /          \ i    /
\=___)___---^^^^---J '/           | |__-^l
  `^^'             i`-------------^^^   ,'
                   `._________________-'
                   |                  \
                   /                   |
                 ,'                    |
               ,'      ,-__-.         /
             ,'      ,'      `>      |
           ,'      ,'        /       |
          /       /          |       |

''')

print('''
Welcome to treasure Island
your mission is to find treasure
''')

choice1 = input('Would you like to go "left" or "Right" ?: ').lower()

if choice1 == "left":
    choice2 = input('Now we reach a island. these is a river would you like to "Wait" or "swim" ').lower()

    if choice2 == "wait":

        choice3 = input("These is three door 'red', 'blue' or 'green'. Only one door is safe . choice the door: ").lower()
        if choice3 == "red":
            print("Game Over")
        elif choice3 == "blue":
            print("you win the game")
        elif choice3 == "green":
            print("Game over")

    elif choice2 == "swim":
        print("Game Over")

elif choice1 == "right":
     print("Game Over")

else:
    print("Game Over")