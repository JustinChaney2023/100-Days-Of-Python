print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

option1 = input("You come across a crosspath. Will you go left or right?")
option1 = option1.lower()

if option1 == "right":
    print("You walk down the path for hours and start having strong dejavu as if you've been there before. You get trapped in an endless cycle and die of starvation.")
    print('''     _      _                   
    | |    (_)                  
  __| | ___ _  __ ___   ___   _ 
 / _` |/ _ \ |/ _` \ \ / / | | |
| (_| |  __/ | (_| |\ V /| |_| |
 \__,_|\___| |\__,_| \_/  \__,_|
          _/ |                  
         |__/ ''')
    print("GAME OVER")

elif option1 == "left":
    option2 = input(print("You walk down a path and stumble upon a lake with a pier. You see no boats in sight. What do you do? Wait, Swim, Search"))
    option2 = option2.lower()
    if option2 == "wait":
        print("...\n" * 6)
        print("A boat arrives and you safely cross the lake")
        option3 = input("You see a building with 3 doors. Each door is a different color. Which door will you enter? Blue, Red, Yellow")
        option3 = option3.lower()

        if option3 == "red":
            print("You burned to death. Surprise, surprise the red door was dangerous.")
            print('''            (                 ,&&&.
                    )                .,.&&
                 (  (              \=__/
                        )             ,'-'.
                (    (  ,,      _.__|/ /|
                 ) /\ -((------((_|___/ |
              (  // | (`'      ((  `'--|
              _ -.;_/ \\--._      \\ \-._/.
           (_;-// | \ \-'.\    <_,\_\`--'|
              ( `.__ _  ___,')      <_,-'__,'
              `'(_ )_)(_)_)')''')
            print("GAME OVER.")
        elif option3 == "blue":
            print("You drowned to death. How? No clue honestly you just dropped dead.")
            print('''                   __.............__
                   .--""```                 ```""--.
                    ':--..___             ___..--:'
                     \      ```"""""""```      /
                   .-`  ___.....-----.....___  '-.
                .:-""``     ~          ~    ``""-:.
                /`-..___ ~        ~         ~___..-'\
                /  ~    '`""---.........---""`        \
               ;                                       ;
              ; '::.   '          _,           _,       ;
              |   ':::    '     .' (    ~   .-'./    ~  |
              |~  .:'   .     _/..._'.    .'.-'/        |
              | .:'       .-'`      ` '-./.'_.'         |
              |  ':.     ( o)   ))      ;= <_           |
              ; '::.      '-.,\\__ __.-;`\'. '.  .      ;
               ;    ':         \) |`\ \)  '.'-.\       ;
                \.:'.:':.         \_/       '-._\     /
                 \ ':.     ~                    `    /
                  '. '::..  _ . - - -- .~ _      ~ .'
                    '-._':'                 `'-_.-'
                       (``''--..._____...--''``)
                        `"--...__     __...--"`
                                 `````)''')
            print("GAME OVER.")
        elif option3 == "yellow":
            print("YOU FOUND THE TREASURE!!!!!!!!")
        else:
            print("You tried treading a new path and died. Maybe being a trailblazer isn't always a good thing")

    elif option2 == "swim":
        print("You have drowned to death. Guess you weren't as good at swimming than you thought")

    elif option2 == "search":
        print("You find a schedule and find out the next boat arrives soon and wait.")
        print("...\n" * 3)
        print("A boat arrives and you safely cross the lake")
        option3 = input("You see a building with 3 doors. Each door is a different color. Which door will you enter? Blue, Red, Yellow")
        option3 = option3.lower()

        if option3 == "red":
            print("You burned to death. Surprise, surprise the red door was dangerous.")
            print('''            (                 ,&&&.
                    )                .,.&&
                 (  (              \=__/
                        )             ,'-'.
                (    (  ,,      _.__|/ /|
                 ) /\ -((------((_|___/ |
              (  // | (`'      ((  `'--|
              _ -.;_/ \\--._      \\ \-._/.
           (_;-// | \ \-'.\    <_,\_\`--'|
              ( `.__ _  ___,')      <_,-'__,'
              `'(_ )_)(_)_)')''')
            print("GAME OVER.")
        elif option3 == "blue":
            print("You drowned to death. How? No clue honestly you just dropped dead.")
            print('''                   __.............__
                   .--""```                 ```""--.
                    ':--..___             ___..--:'
                     \      ```"""""""```      /
                   .-`  ___.....-----.....___  '-.
                .:-""``     ~          ~    ``""-:.
                /`-..___ ~        ~         ~___..-'\
                /  ~    '`""---.........---""`        \
               ;                                       ;
              ; '::.   '          _,           _,       ;
              |   ':::    '     .' (    ~   .-'./    ~  |
              |~  .:'   .     _/..._'.    .'.-'/        |
              | .:'       .-'`      ` '-./.'_.'         |
              |  ':.     ( o)   ))      ;= <_           |
              ; '::.      '-.,\\__ __.-;`\'. '.  .      ;
               ;    ':         \) |`\ \)  '.'-.\       ;
                \.:'.:':.         \_/       '-._\     /
                 \ ':.     ~                    `    /
                  '. '::..  _ . - - -- .~ _      ~ .'
                    '-._':'                 `'-_.-'
                       (``''--..._____...--''``)
                        `"--...__     __...--"`
                                 `````)''')
            print("GAME OVER.")
        elif option3 == "yellow":
            print("YOU FOUND THE TREASURE!!!!!!!!")
        else:
            print("You tried treading a new path and died. Maybe being a trailblazer isn't always a good thing")
else:
    print("You tripped over a pebble doing something stupid and died")