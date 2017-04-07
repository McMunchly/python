# main file for omelet game

import os.path

import room
import item

def game():
    print("---")

    game = True
    action = ""

    currentroom = room.currentroom
    currentitem = item.blankItem

    if os.path.isfile("savefile.txt"):
        load = input("Load a save file? (y/n): ")

        if load == "y":
            savefile = open("savefile.txt", "r")
        
            currentroom = room.FindRoom(savefile.readline().rstrip())
            room.currentroom = currentroom
            currentitem = item.FindItem(savefile.readline().rstrip())
        
            for bedroom in room.rooms:
                if bedroom.name == "Bedroom":
                    bedroom.InsertItems(savefile.readline())
            for kitchen in room.rooms:
                if kitchen.name == "Kitchen":
                    kitchen.InsertItems(savefile.readline())

        print("You are standing in " + currentroom.description + " holding " + currentitem.name)
    while game == True:
        action = input("action: ")

        # split action into words for parsing
        action = action.split(" ")
        count = 0

        # make it so commands don't have to be case sensitive
        while count < len(action):
            action[count] = action[count].lower()

            if(count > 0):
                newword = action[count]
                action[count] = newword[0].upper() + newword[1:]
                

            count = count + 1

        # figure out which command was entered
        if action[0] == "help":
            print("actions:")
            print("--------")
            print("enter <room> - enter the chosen room")
            print("look - observe your surroundings")
            print("take <item> - pick up the chosen item")
            print("use - use the item you are holding")
            print("drop - put down the item you are holding")
            print("useon - use the current item on something else")
            print("save - save your game")
            print("quit - exit the game")

        elif action[0] == "enter":
            if len(action) == 1:
                print("You must specify which room to enter")
            else:
                for place in room.rooms:
                    if place.name == action[1]:
                        currentroom = place
                        room.currentroom = place
        elif action[0] == "look":
            print("You are standing in " + currentroom.description + " holding " + currentitem.name)
            currentroom.DisplayItems()
        elif action[0] == "take":
            if len(action) == 1:
                print("You must specify which item to take")
            else:
                for thing in currentroom.items:
                    if thing.name == action[1]:
                        if thing.pickup == True:
                            if currentitem != item.blankItem:
                                currentroom.AddItem(currentitem)
                                print("you drop " + currentitem.name)
                            
                            currentitem = thing
                            print("you pick up " + currentitem.name)
                            currentroom.RemoveItem(thing)
                        else:
                            print("The " + thing.name + " is too heavy to pickup")
                            
        elif action[0] == "use":
            if len(action) == 1:
                if currentitem != item.blankItem:
                    game = currentitem.Use()
            else:
                for thing in currentroom.items:
                    if thing.name == action[1]:
                       thing.Use()
        elif action[0] == "useon":
            if len(action) == 1:
               print("You must specify what to use " + currentitem.name + " on")
            else:
               print("You use " + currentitem.name + " on the " + action[1])
               for thing in currentroom.items:
                    if thing.name == action[1]:
                        result = thing.Useon(currentitem)

                        if result == "drop":
                           currentroom.AddItem(currentitem)
                           currentitem = item.blankItem
                        elif result == "remove":
                            currentitem = item.blankItem
                            
        elif action[0] == "drop":
            currentroom.AddItem(currentitem)
            currentitem = item.blankItem
        elif action[0] == "save":
            savefile = open("savefile.txt", "w")
            savefile.write(currentroom.name + "\n")
            savefile.write(currentitem.name + "\n")

            for theroom in room.rooms:
                itemlist = ""
                for items in theroom.items:
                    itemlist = itemlist + items.name + " "
                print(itemlist)
                savefile.write(itemlist + "\n")
            savefile.close()
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
