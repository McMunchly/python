# main file for omelet game

import os.path

import room
import item

def game():
    game = True
    action = ""

    currentroom = room.currentroom
    currentitem = item.blankItem

    # see if a save file exists
    if os.path.isfile("savefile.txt"):
        load = input("Load a save file? (y/n): ")

        # load the save file
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

        print("Your stomach starts to rumble...")
        
    while game == True:
        print()
        action = input("Command? (press help to see actions): ")
        print()
        
        # split action into words for parsing
        action = action.split(" ")
        count = 0

        # make it so commands don't have to be case sensitive
        while count < len(action):
            action[count] = action[count].lower()

            count = count + 1

        # figure out which command was entered
        if action[0] == "help":
            print("actions:")
            print("--------")
            print("enter <room> - enter the chosen room")
            print("take <item> - pick up the chosen item")
            print("use - use the item you are holding")
            print("drop - put down the item you are holding")
            print("examine - look closer at the item you are holding")
            print("useon - use the current item on something else")
            print("look - look around the current room")
            print("save - save your game")
            print("quit - exit the game")

        elif action[0] == "enter":
            if len(action) == 1:
                print("You must specify which room to enter")
            else:
                found = False
                for place in currentroom.connections:
                    if place.name == action[1]:
                        found = True
                        currentroom = place
                        room.currentroom = place
                        room.Display(currentroom, currentitem.name)
                if found == False:
                    print("There is no way to get there from here")
                        
        elif action[0] == "take":
            if len(action) == 1:
                print("You must specify which item to take")
            else:
                found = False
                
                for thing in currentroom.items:
                    if thing.name == action[1]:
                        found = True
                        if thing.pickup == True:
                            if currentitem != item.blankItem:
                                currentroom.AddItem(currentitem)
                                print("you drop " + currentitem.name)
                            
                            currentitem = thing
                            print("you pick up " + currentitem.name)
                            currentroom.RemoveItem(thing)
                        else:
                            print("The " + thing.name + " is too heavy to pickup")

                if found == False:
                    print(action[1] + " not found")
                        
                            
        elif action[0] == "use":
            if len(action) == 1:
                if currentitem != item.blankItem:
                    game = currentitem.Use()
                else:
                    print("You are not holding anything")
            else:
                found = False
                
                for thing in currentroom.items:

                    if thing.name == action[1]:
                        found = True
                        game = thing.Use()
                       
                if found == False:
                    print(action[1] + " not found")
        elif action[0] == "useon":
            if len(action) == 1:
               print("You must specify what to use " + currentitem.name + " on")
            else:
                found = False
                                    
                for thing in currentroom.items:
                   
                    if thing.name == action[1]:
                        print("You use " + currentitem.name + " on the " + action[1])
                        found = True
                        result = thing.Useon(currentitem)

                        if result == "drop":
                           currentroom.AddItem(currentitem)
                           currentitem = item.blankItem
                        elif result == "remove":
                            currentitem = item.blankItem
                            
                if found == False:
                    print(action[1] + " not found")
                            
        elif action[0] == "drop":
            currentroom.AddItem(currentitem)
            currentitem = item.blankItem
        elif action[0] == "examine":
            currentitem.Description()
        elif action[0] == "look":
            room.Display(currentroom, currentitem.name)
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
        else:
            print("Invalid command")
def quit():
    print("K bye")

print("")
print ("Omelet Quest: The Quest for the Perfect Omelet")
print("---------------by Samuel Dassler---------------")

game()
print()
