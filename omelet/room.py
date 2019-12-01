# definitions for rooms

import item

class Room(object):
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def AddItem(self, item):
        self.items.append(item)
        
    def RemoveItem(self, item):
        self.items.remove(item)
        
    def DisplayItems(self):
        if len(self.items) == 0:
            print("Nothing looks interesting")
        else:
            for stuff in self.items:
                print("You see", end = " ")
                print(stuff.name, end = " ")
                print()
        
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

rooms = [bedroom, kitchen, fridge]

currentroom = bedroom

def Display(room, item):
        print("You are " + room.description + " holding " + item)
        room.DisplayItems()
        
def FindRoom(roomname):
    for theroom in rooms:
        if(roomname == theroom.name):
            return theroom

    print("saved room not found!")
