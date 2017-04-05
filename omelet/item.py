# definitions for item objects

import room

class Item(object):
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        
    def Use(self):
        print("you used " + self.name)
        return True

class SharkBook(Item):
    def Use(self):
        super(SharkBook, self).Use()
        print("sharks hunt prey with electrocmagnetism!")
        return True

class Omelet(Item):
    def Use(self):
        print("you eat the " + self.description)
        print("You ate an omelet! You win!!")
        return False

class Stove(Item):
    
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        self.placeditem = None

    def Use(self):
        if self.placeditem != None:
            print(self.placeditem.name + " was burnt to a crisp")

            room.currentroom.RemoveItem(self.placeditem)

            if(self.placeditem == omelet or self.placeditem == burntOmelet):
                room.currentroom.AddItem(burntOmelet)

            else:
                room.currentroom.AddItem(ash)
        
    def Useon(self, Item):
        self.placeditem = Item
        return "drop"
    
blankItem = Item("nothing", "there is nothing there", False)
ash = Item("Ash", "A pile of burnt something or other", True)
book = SharkBook("Book", "Rad Shark Facts", True)
omelet = Omelet("Omelet", "tasty omelet", True)
burntOmelet = Omelet("Burntomelet", "nasty, gross omelet", True)
stove = Stove("Stove", "A great way to cook eggs", False)
