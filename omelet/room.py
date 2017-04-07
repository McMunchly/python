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
                print(stuff.name)

    def InsertItems(self, itemlist):
        names = itemlist.split(" ")
        self.items = []
        for name in names:
            for theitem in item.items:
                if name == theitem.name:
                    self.AddItem(theitem)
                    
bedroom = Room("Bedroom", "your low-rent bedroom", [item.book])
kitchen = Room("Kitchen", "your smelly kitchen", [item.eggs, item.bowl, item.stove])

rooms = [bedroom, kitchen]

currentroom = bedroom

def FindRoom(roomname):
    for theroom in rooms:
        if(roomname == theroom.name):
            return theroom

    print("saved room not found!")
