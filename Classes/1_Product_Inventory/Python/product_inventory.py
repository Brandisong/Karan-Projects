"""
**Product Inventory Project**
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an *inventory* class which keeps track of various products 
    and can sum up the inventory value.
"""

# Product class: has a price, id, and stock-on-hand
class Product:
    def __init__(self, name, price, id, soh):
        self.name = str(name)
        self.price = price
        self.id = id
        self.soh = soh

    
    def __str__(self):
        return f"{self.name} ({self.id}) | SOH:{self.soh} | ${self.price}"


# Inventory: represents a store's inventory, contains a list of product instances
class Inventory:
    def __init__(self, name):
        self.name = str(name)
        self.products = []

    
    def __str__(self):
        return self.name
    

    def AddProduct(self, product):
        if product not in self.products:
            self.products.append(product)

    
    def SumValue(self):
        total = 0
        for item in self.products:
            total += item.price * item.soh
        
        return total


# Example products
apple = Product("Apple", 2, "000APL", 21)
banana = Product("Banana", 3, "000BNN", 6)
cucumber = Product("Cucumber", 1.5, "000CCB", 28)

digitalWatch = Product("Digital watch", 120, "000DWT", 4)
electricClock = Product("Electric clock", 20, "000ECL", 5)

# Example inventory
groceries = Inventory("Grocery section")
groceries.AddProduct(apple)
groceries.AddProduct(banana)
groceries.AddProduct(cucumber)

electronics = Inventory("Electronics section")
electronics.AddProduct(digitalWatch)
electronics.AddProduct(electricClock)


# Testing
print(apple)
print(groceries)
print(groceries.SumValue())
print(electronics)
print(electronics.SumValue())