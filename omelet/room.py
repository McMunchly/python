# definitions for rooms

import item

class Room(object):
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.connections = []

    def AddItem(self, item):
        self.items.append(item)
        
    def RemoveItem(self, item):
        self.items.remove(item)
        
    def DisplayItems(self):
        if len(self.items) == 0:
            print("Nothing in the room looks interesting")
        else:
            for stuff in self.items:
                print("You see", end = " ")
                print(stuff.name + ", " + stuff.description, end = " ")
                print()

    def AddConnection(self, room):
        self.connections.append(room)

    def DisplayConnections(self):
        for stuff in self.connections:
            print("You see a door leading to the", end = " ")
            print(stuff.name)
                
    def InsertItems(self, itemlist):
        names = itemlist.split(" ")
        self.items = []
        for name in names:
            for theitem in item.items:
                if name == theitem.name:
                    self.AddItem(theitem)
                    
bedroom = Room("bedroom", "standing in your low-rent bedroom", [item.book, item.cookbook])
kitchen = Room("kitchen", "standing in your dirty kitchen", [item.bowl, item.whisk, item.stove, item.sink])
fridge = Room("fridge", "looking in your smelly fridge", [item.eggs, item.filling])

bedroom.AddConnection(kitchen)
kitchen.AddConnection(bedroom)
kitchen.AddConnection(fridge)
fridge.AddConnection(kitchen)

rooms = [bedroom, kitchen, fridge]

currentroom = bedroom

def Display(room, item):
        print("You are " + room.description + " holding " + item)
        room.DisplayItems()
        room.DisplayConnections()
        
def FindRoom(roomname):
    for theroom in rooms:
        if(roomname == theroom.name):
            return theroom

    print("saved room not found!")
