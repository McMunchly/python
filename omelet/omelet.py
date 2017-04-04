# main file for omelet game

import room
import item

def game():
    print("---")

    game = True
    action = ""

    currentroom = room.bedroom
    currentitem = item.blankItem
    
    while game == True:
        print("You are standing in " + currentroom.description + " holding " + currentitem.name)
        action = input("action: ")

        action = action.split(" ")
        
        if action[0] == "help":
            print("actions:")
            print("--------")
            print("enter <room> - enter the chosen room")
            print("look - observe your surroundings")
            print("take <item> - pick up the chosen item")
            print("use - use the item you are holding")
            print("drop - put down the item you are holding")
            print("quit - exit the game")

        elif action[0] == "enter":
            if len(action) == 1:
                print("You must specify which room to enter")
            else:
                for place in room.rooms:
                    if place.name == action[1]:
                        currentroom = place
        elif action[0] == "look":
            currentroom.DisplayItems()
        elif action[0] == "take":
            if len(action) == 1:
                print("You must specify which item to take")
            else:
                for thing in currentroom.items:
                    if thing.name == action[1]:
                        if currentitem != item.blankItem:
                            currentroom.AddItem(currentitem)
                            
                        currentitem = thing
                        currentroom.RemoveItem(thing)
        elif action[0] == "use":
            game = currentitem.Use()
        elif action[0] == "drop":
            currentroom.AddItem(currentitem)
            currentitem = item.blankItem
        elif action[0] == "quit":
            game = False
            quit()
def quit():
    print("K bye")

print("")
print ("Omelet Quest: The Quest for the Perfect Omelet")
print("---------------by Samuel Dassler---------------")
choice = input("\n Are you ready? (y to play, n to quit): ")

if choice == "y":
    game()
else:
    quit()
