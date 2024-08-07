"""
**Product Inventory Project**
Create an application which manages an inventory of products.
Create a product class which has a price, id, and quantity on hand.
Then create an *inventory* class which keeps track of various products 
    and can sum up the inventory value.
"""

# Product class: has a price, id, and stock-on-hand
class Product:
    def __init__(self, price, id, soh):
        self.price = price
        self.id = id
        self.soh = soh


# Inventory: represents a store's inventory, contains a list of product instances
class Inventory:
    def __init__(self):
        self.products = []
    

    def AddProduct(self, product):
        if product not in self.products:
            self.products.append(product)


apple = Product(2, "000APL", 21)
banana = Product(3, "000BNN", 6)
cucumber = Product(1.5, "000CCB", 28)

groceries = Inventory()
groceries.AddProduct(apple)

print(groceries.products[0].soh)