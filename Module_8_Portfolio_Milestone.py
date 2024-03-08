###Module 4 Portfolio Milestone
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0
       
    def updateValues(self):
        self.item_name = input("Enter the item name:\n")
        self.item_description = input("Enter the item description:\n")
        self.item_price = float(input("Enter the item price:\n"))
        self.item_quantity = int(input("Enter the item quantity:\n"))
       
    def print_item_cost(self):
        print(self.item_name, end=" ")
        print(self.item_quantity, end=" ")
        print("@ ${:.2f}".format(self.item_price), end=" ")
        self.total = self.item_price * self.item_quantity
        print("= ${:.2f}".format(self.total))
       
    def updateQuantity(self):
        self.item_quantity = int(input("Enter new quantity:\n"))
 
###Module 6 Portfolio Milestone       
class ShoppingCart:
    def __init__(self, customer_name, current_date):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []
 
    def getCustNameDate(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
 
    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)
 
    def remove_item(self, item_to_remove):
        check_if_its_there = []
        for names in self.cart_items:
            check_if_its_there.append(names.item_name)
        if item_to_remove in check_if_its_there:
            self.cart_items.remove(names)
            print("Item removed sucessfully.")
        else:
            print("Item not found. Nothing removed.")
            

 
    def modify_item(self, item: ItemToPurchase):
        if item in self.cart_items:
            if (item.item_name == "none") and (item.item_price == 0) and (item.item_quantity == 0):
                print("Item has default values")
            else:
                print("Update item information for item \"{}\":".format(item.item_name))
                item.updateValues()
 
    def get_num_items_in_cart(self):
        num_items_in_cart = 0
        for items in self.cart_items:
            num_items_in_cart += items.item_quantity
 
    def get_cost_of_cart(self):
        if (items in self.cart_items) == True:
            for items in self.cart_items:
                total += items.item_price()
            print("Total: ${:.2f}".format(total))
        else:
            print("SHOPPING CART IS EMPTY")
 
    def print_total(self):
        total_cart_item_quantity = 0
        total_cart_cost = 0
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        for items in self.cart_items:
            total_cart_item_quantity += items.item_quantity
        print("Number of Items:", total_cart_item_quantity)
        for items in self.cart_items:
            print(items.item_name, end=" ")
            print(items.item_quantity, end=" ")
            print("@ ${:.2f}".format(items.item_price), end=" ")
            items.total = items.item_price * items.item_quantity
            print("= ${:.2f}".format(items.total))
        for items in self.cart_items:
            total_cart_cost += items.item_price * items.item_quantity
        print("Total: ${:.2f}".format(total_cart_cost))
 
    def print_description(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for items in self.cart_items:
            print("{}: {}".format(items.item_name, items.item_description))
           
    def change_quantity(self):
        self.names_in_cart_list()
        change_item_quantity = input("Enter the item name to change quantity:\n")
        if change_item_quantity in self.list_for_names:
            for individual_items in self.cart_items:
                if individual_items.item_name == change_item_quantity:
                    individual_items.updateQuantity()           
                    print("Quantity updated.")
        else:
            print("Item not found. Nothing updated.")

    def view_item_info(self):
        self.names_in_cart_list()
        item_to_view = input("Enter the item to view info for:\n")
        print()
        if item_to_view in self.list_for_names:
            for items in self.cart_items:
                if item_to_view == items.item_name:
                    print("Name:", items.item_name)
                    print("Description:", items.item_description)
                    print("Price: ${:.2f}".format(items.item_price))
                    print("Quantity:", items.item_quantity)
        else:
            print("Not in cart.")

   
    def names_in_cart_list(self):
        self.list_for_names = []
        for named_items in self.cart_items:
            self.list_for_names.append(named_items.item_name)
        print("Items in cart: |", end=" ")
        for names in self.list_for_names:
            print(names, "|", end=" ")
        print()


def main():
 
###Module 4 Portfolio Milestone
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    count = 1
    for x in (item1, item2):
        print("  --ITEM #{}--  ".format(count))
        x.updateValues()
        count +=1
   
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    items_cost_sum = item1.total + item2.total
    print("Total: ${:.2f}".format(items_cost_sum))
 
###Module 6 Portfolio Milestone
    print("\n--------------------\nCustomer Shopping Cart")
    customer_cart = ShoppingCart("Default Name", "Default Date")
    customer_cart.getCustNameDate(input("Enter customer name:\n"), input("Enter current date:\n"))
 
    def print_menu(x):
        print("""MENU
a - Add item to cart
c - Change item quantity
r - Remove item from cart
m - Modify item
v - View an items Details
i - Output items' descriptions
o - Output shopping cart
q - Quit""")
        selection = input("Choose an option: ")
        while selection != "q":
            print()
            if selection == "a":
                print("Items avalible for addition to the cart: {}, {}".format(item1.item_name, item2.item_name))
                print("    (if the item to add is not in the above list you will be prompted to add the item manually)")
                add_choice = input("Enter an item to add:\n")
                if add_choice == item1.item_name:
                    x.add_item(item1)
                    print("Item added.")
                elif add_choice == item2.item_name:
                    x.add_item(item2)
                    print("Item added.")
                else:
                    print("Item not found. Would you like to add a new item?")
                    addchoice = input("Enter \"Yes\" or \"No\":\n")
                    if (addchoice == "Yes") or (addchoice == "yes"):
                        newitem = ItemToPurchase()
                        newitem.updateValues()
                        x.add_item(newitem)
                        print("Item added.")
                    else:
                        print("Nothing added.")
                       
            elif selection == "c":
                x.change_quantity()
 
            elif selection == "r":
                x.names_in_cart_list()
                item_for_removal = input("Enter the name of the item to be removed:\n")
                x.remove_item(item_for_removal)
 
            elif selection == "m":
                x.names_in_cart_list()
                mod_choice = input("Enter name of item to modify:\n")
                if (mod_choice in x.list_for_names) == False:
                    print("Item not found in cart. Nothing modified.")
                else:
                    for names in x.cart_items:
                        if names.item_name == mod_choice:
                            mod_choice = names
                            x.modify_item(mod_choice)
                        
 
            elif selection == "i":
                x.print_description()
 
            elif selection == "o":
                x.print_total()
               
            elif selection == "v":
                x.view_item_info()

            elif selection == "Menu":
                        print("""MENU
a - Add item to cart
c - Change item quantity
r - Remove item from cart
m - Modify item
v - View an items Details
i - Output items' descriptions
o - Output shopping cart
q - Quit""")
 
            else:
                print("Enter a valid selection")
 
            selection = input("\nChoose an option (type \"Menu\" to see list of options):\n")
 
       
            
 
    print_menu(customer_cart)
       
        
 
if __name__ == "__main__":
    main()