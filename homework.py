class Item:
    def __init__(self, name):
        self.name = name
        

class ShoppingList:
    def __init__(self):
        self.shop_cart = []
        
    def add_items(self, name):
        new_item = Item(name)
        self.shop_cart.append(new_item)
    
    def remove_items(self, del_name):
        # remd_item = Item( name) # This is instantiating a new Item object

        print(f'self.shop_cart: {self.shop_cart}')

        for item in self.shop_cart:
            if item.name.lower() == del_name.lower():
                self.shop_cart.remove(item)
        
    def print_shop_cart(self):
        print("=~" * 15)
        print("SHOPPING LIST:")
        
        for item in self.shop_cart:
            print(item.name)
        
        print("=~" * 15)
        
    def run(self):
        while True:
            question = input("What would you like to do (Add/Remove/Show/Check Out)? ")

            if question == "Add":
                name = input("Add item to list: ")
               
                self.add_items(name)

            elif question == "Remove":
                name = input("Remove item from list: ")

                self.remove_items(name)

            elif question == "Show":
                self.print_shop_cart()
                                
            elif question == "Check Out":
                break
                
        self.print_shop_cart()

shop_cart = ShoppingList()
shop_cart.run()