# main file for omelet game

def game():
    print("YAY!")

    game = True
    action = ""
    
    while game == True:
        action = input("action: ")

        if action == "help":
            print("actions:")
            print("--------")
            print("enter <room> - enter the chosen room")
            print("look - observe your surroundings")
            print("take <item> - pick up the chosen item")
            print("use - use the item you are holding")
            print("quit - exit the game")

        elif action == "quit":
            game = False
            quit()
def quit():
    print("K bye")

print ("Omelet Quest: The Quest for the Perfect Omelet")
print("by Samuel Dassler")
choice = input("\n Are you ready? (y to play, n to quit): ")

if choice == "y":
    game()
else:
    quit()
