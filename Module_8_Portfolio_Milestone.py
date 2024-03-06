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
        for names in self.cart_items:
            if names.item_name == item_to_remove:
                self.cart_items.remove(names)
            else:
                print("Item not found in cart. Nothing removed.")
 
    def modify_item(self, item: ItemToPurchase):
        if item in self.cart_items:
            if (item.item_name == "none") and (item.item_price == 0) and (item.item_quantity == 0):
                print("Item has default values")
            else:
                print("Update item information for item \"{}\":".format(item.item_name))
                item.updateValues()
        else:
            print("Item not found in cart. Nothing modified.")
 
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
        for individual_items in self.cart_items:
            print(individual_items.item_name, "|", end="")
        change_item_quantity = input("Enter the item name:\n")
        for individual_items in self.cart_items:
            if individual_items.item_name == change_item_quantity:
                individual_items.updateQuantity()
            elif individual_items.item_name != change_item_quantity:
                print("Invalid selection: item not in cart.")
   
    ##IM NOT SURE HOW TO USE THIS METHOD WITHIN OTHER METHODS, BUT IF IT WORKS FUCKIN GREAT
    ##OTHERWISE COPY-PASTE THIS AFTER TESTING
    def names_in_cart_list():
        list_for_names = []
        for named_items in self.cart_items:
            list_for_names.append(named_items.item_name)
        print(list_for_names)
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
    print("\n-------------\nCustomer Shopping Cart")
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
            if selection == "a":
                print("Items that can be added to the cart: {}, {}".format(item1.item_name, item2.item_name))
                add_choice = input("Enter name of item to add to cart:\n")
                if add_choice == item1.item_name:
                    x.add_item(item1)
                elif add_choice == item2.item_name:
                    x.add_item(item2)
                else:
                    print("Item not found. Would you like to add a new item?")
                    addchoice = input("Enter yes or no")
                    if addchoice == "yes":
                        newitem = ItemToPurchase()
                        newitem.updateValues()
                        x.add_item(newitem)
                        print("Item added.")
                    else:
                        print("Nothing added.")
                       
            elif selection == "c":
                x.change_quantity()
 
            elif selection == "r":
                item_for_removal = input("Enter the name of the item to be removed:")
                x.remove_item(item_for_removal)
 
            elif selection == "m":
                print("Modify item:", item1.item_name, item2.item_name)
                ##MAKE THE ABOVE LINE MORE LIKE IN THE V SECTION - THIS ONLY INCLUDED ITEMS 1 AND 2
                ##SEE ABOVE COMMENT
                ##SERIOUSLY DONT MISS IT
                mod_choice = input("Enter name of item to modify:\n")
                if mod_choice == item1.item_name:
                    x.modify_item(item1)              
                elif mod_choice == item2.item_name:
                    x.modify_item(item2)
                else:
                    item3 = ItemToPurchase
                    x.modify_item(item3)
 
            elif selection == "i":
                x.print_description()
 
            elif selection == "o":
                x.print_total()
               
            elif selection == "v":
                print("Items in cart:")
                print("|", end=" ")
                for individual_items in x.cart_items:
                    print(individual_items.item_name, "|", end="")
                seeiteminfo = input("\nEnter the item name from the above list to see item details:")
                for individual_items in x.cart_items:
                    if individual_items.item_name == seeiteminfo:
                        print("Name:", individual_items.item_name)
                        print("Description:", individual_items.item_description)
                        print("Price: ${:.2f}".format(individual_items.item_price))
                        print("Quantity:", individual_items.item_quantity)
                        print("Item total price: ${:.2f}".format(individual_items.item_price * individual_items.item_quantity))
                    elif individual_items.item_name != seeiteminfo:
                        print("Invalid selection: item not in cart.")
 
            else:
                print("Enter a valid selection")
 
            selection = input("Choose an option:\n")
 
       
            
 
    print_menu(customer_cart)
       
        
 
if __name__ == "__main__":
    main()