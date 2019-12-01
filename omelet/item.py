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

    def Description(self):
        print(self.description)

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
        self.haseggs = False
        self.haswater = False
        self.mixed = False

    def SetVars(self, haseggs, haswater, mixed):
        self.haseggs = haseggs
        self.haswater = haswater
        self.mixed = mixed
        
    def Description(self):
        if self.haseggs == True:
            if self.haswater == True:
                if self.mixed == True:
                    print("It's a perfect mixture of eggs and just enough water for maximum fluffiness")
                else:
                    print("The eggs and water are in perfect proportion, but it's not mixed")
            else:
                if self.mixed == True:
                    print("It's a bunch of whisked eggs")
                else:
                    print("It's a bunch of eggs in a bowl") 
        else:
            if self.haswater == True:
                print("It's filled with water")
            else:
                print("It's just an empty bowl")
                
    def Useon(self, item):
        if item == eggs:
            self.haseggs = True
            print("You crack the eggs into the bowl")
            return "remove"
        if item == whisk:
            if self.haseggs == True and self.haswater == True:
                print("You whisk up the eggs and water")
                self.mixed = True
                return "drop"

class Omelet(Item):
    def __init__(self, name, description, pickup):
        self.name = name
        self.description = description
        self.pickup = pickup
        self.fluffy = False
        self.filling = False

    def SetVars(self, fluffy, filling):
        self.fluffy = fluffy
        self.filling = filling
        
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
                print("You lose...These are just eggs, burnt to a crisp")
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
            if self.placeditem == bowl:

                if bowl.haseggs == False:
                    print("Water begins to boil")
                    return True
                else:
                    omelet.fluffy = bowl.mixed

                print("Your creation is cooked to perfection")
                room.currentroom.RemoveItem(self.placeditem)
                room.currentroom.AddItem(omelet)
                return True
            else:
                print("You lose...A fire starts and burns down the building")
                return False
        else:
            print("You turn the stove on but there's nothing in the pan on the burner")
        
    def Useon(self, item):
        print("You place the " + item.name + " into the pan on the stove")
        self.placeditem = item
        return "drop"

class Sink(Item):
    def Useon(self, item):
        if item == bowl:
            print("You pour some water into the bowl")
            bowl.haswater = True
    
blankItem = Item("nothing", "there is nothing there", False)
ash = Item("ash", "a pile of burnt something or other", True)
book = Book("sharkbook", "101 Rad Shark Facts", True, "sharks hunt prey with electrocmagnetism!")
cookbook = Book("cookbook", "How to cook an omelet", True, "whisk eggs and water and cook on a stovetop. Add filling and enjoy")
eggs = Item("eggs", "a carton of eggs", True)
whisk = Item("whisk", "a utensil for mixing ingredients", True)
bowl = Bowl("bowl", "a bowl for mixing", True)
filling = Item("filling", "fresh veggies for the omelet", True)
omelet = Omelet("omelet", "delicious and filling", True)
sink = Sink("sink", "delivers cold, clean water", False)
stove = Stove("stove", "a great way to cook eggs", False)

items = [blankItem, ash, book, cookbook, eggs, bowl, whisk, filling, omelet, stove, sink]

def FindItem(itemname):
    for theitem in items:
        if(itemname == theitem.name):
            return theitem

    print("Saved item not found")
