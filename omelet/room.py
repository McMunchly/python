# definitions for room objects

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
        
bedroom = Room("Bedroom", "your low-rent bedroom", [item.book])
kitchen = Room("Kitchen", "your smelly kitchen", [item.omelet, item.stove])

rooms = [bedroom, kitchen]

currentroom = bedroom
