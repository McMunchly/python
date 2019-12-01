# definitions for item

import room

class Item(object):
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        
    def Use(self):
        print("can't use " + self.name + " by itself")
        return True

class Book(Item):
    def __init__(self, name, description, pickup, text):
        self.name = name
        self.description = description
        self.pickup = pickup
        self.text = text
        
    def Use(self):
        print(self.text)
        return True

class Bowl(Item):
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        self.placeditem = None
        self.haseggs = False
        self.haswater = False
        self.mixed = False
        
    def Useon(self, item):
        if item == eggs:
            self.haseggs = True
            return "remove"
        if item == whisk:
            if self.haseggs == True and self.haswater == True:
                self.mixed = True
                return "drop"

class Omelet(Item):
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        self.placeditem = None
        self.fluffy = False
        self.filling = False
    
    def Use(self):
        if self.fluffy == True:
            if self.filling == True:
                print("You win! The omelet is exquisite")
            else:
                print("You win! But the omelet is pretty bland") 
        else:
            if self.filling:
                print("You win! The omelet is stuffed, but it's all kind of flat")
            else:
                print("You lose...These eggs are well-cooked, but it's not whisked or filled")
        return False

    def Useon(self, item):
        if item == filling:
            self.filling = True
            return "remove"
        return ""

class Stove(Item):
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        self.placeditem = None

    def Use(self):
        if self.placeditem != None:
            print(self.placeditem.name + " was cooked to perfection")

            if self.placeditem == omelet:
                omelet.state = 3
            elif self.placeditem == bowl:

                if bowl.haseggs == False:
                    print("You've begun boiled water in the pan")
                    return
                else:
                    omelet.fluffy = bowl.mixed

                room.currentroom.RemoveItem(self.placeditem)
                room.currentroom.AddItem(omelet)
        
    def Useon(self, item):
        self.placeditem = item
        return "drop"

class Sink(Item):
    def Useon(self, item):
        if item == bowl:
            bowl.haswater = True
    
blankItem = Item("nothing", "there is nothing there", False)
ash = Item("ash", "A pile of burnt something or other", True)
book = Book("sharkbook", "101 Rad Shark Facts", True, "sharks hunt prey with electrocmagnetism!")
cookbook = Book("cookbook", "How to cook an omelet", True, "Whisk eggs and water and cook on a stoptop for 5 minutes. Add filling and enjoy")
eggs = Item("eggs", "a carton of eggs", True)
whisk = Item("whisk", "a utinsel for mixing ingredients", True)
bowl = Bowl("bowl", "a bowl for mixing", True)
filling = Item("filling", "fresh veggies for the omelet", True)
omelet = Omelet("omelet", "tasty omelet", True)
sink = Sink("sink", "Delivers cold, clean water", False)
stove = Stove("stove", "A great way to cook eggs", False)

items = [blankItem, ash, book, cookbook, eggs, bowl, whisk, filling, omelet, stove, sink]

def FindItem(itemname):
    for theitem in items:
        if(itemname == theitem.name):
            return theitem

    print("Saved item not found")
