# definitions for item objects

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def Use(self):
        print("you used " + self.name)
        return True

class SharkBook(Item):
    def Use(self):
        print("sharks hunt prey with electrocmagnetism!")
        return True

class Omelet(Item):
    def Use(self):
        print("you eat the omelet and it was pretty amazing!")
        return False
    
blankItem = Item("nothing", "there is nothing there")
book = SharkBook("Book", "Rad Shark Facts")
omelet = Omelet("Omelet", "A tasty omelet")
