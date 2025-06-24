def welcome_message(name):
   return "Hello(name) welcome to your world of Games"
name =input("insert name")
print("Hello",name," welcome to your World of Games")
print("Here you can find many cool games go play", name)

def print_game_option():
   print("Please press the following option to World Of Games", name)
   print("1 Memory_Game")
   print("2 Guess_Game")
   print("3 Currency_Roulette")
while True:
    choice=input("Select a game(1/2/3):")
    if choice in ("1","2","3"):
        try:
            print("Game loading")
        except valueError:
            print("Invalid input")
            continue
    if choice == "1":
         print("Welcome to your Memory_Game",name)
         print( "Please select your level", name)
         print("level 1")
         print("level 2")
         print("level 3")
         print("level 4")
         print("level 5")

         while True:
             choice=input("select your level(1/2/3/4/5):")
             if choice=="1":
                print("level 1 Memory_Game loading")
             elif choice=="2":
                print("level 2 Memory_Game loading")
             elif choice == "3":
                print("level 2 Memory_Game loading")
             elif choice == "4":
                print("level 4 Memory_Game loading")
             elif choice == "5":
                print("level 5 Memory_Game loading")
                break
    elif choice == "2":
         print("Welcome to your Guess_Game", name)
         print("Please select your level", name)
         print("level 1")
         print("level 2")
         print("level 3")
         print("level 4")
         print("level 5")

         while True:
             choice = input("select your level(1/2/3/4/5):")
             if choice == "1":
                print("level 1 Guess_Game loading")
             elif choice == "2":
                print("level 2 Guess_Game loading")
             elif choice == "3":
                print("level 2 Guess_Game loading")
             elif choice == "4":
                print("level 4 Guess_Game loading")
             elif choice == "5":
                print("level 5 Guess_Game loading")
                break

    elif choice == "3":
         print("Welcome to your Currency_Roulette", name)
         print("Please select your level", name)
         print("level 1")
         print("level 2")
         print("level 3")
         print("level 4")
         print("level 5")

         while True:
             choice = input("select your level(1/2/3/4/5):")
             if choice == "1":
                print("level 1 Currency_Roulette loading")
             elif choice == "2":
                print("level 2 Currency_Roulette loading")
             elif choice == "3":
                print("level 2 Currency_Roulette loading")
             elif choice == "4":
                print("level 4 Currency_Roulette loading")
             elif choice == "5":
                print("level 5 Currency_Roulette loading")
                break