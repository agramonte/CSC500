from datetime import date, datetime

#From previous module
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    #Remove function. Trying not to modify the list while iterating over it.
    #Took me a while to figure that one out.
    def remove_item(self, item_name):
        original_length = len(self.cart_items)
        self.cart_items = [item for item in self.cart_items if item.item_name != item_name]
        if len(self.cart_items) == original_length:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                found = True
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def validFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def validInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a int.")

def validString(prompt):
    while True:
        userInput = input(prompt)
        if userInput.strip():
            return userInput
        else:
            print("Invalid input. Please enter text.")

def validDate(prompt):
    while True:
        userInput = input(prompt)
        if not userInput.strip():
            today = date.today()
            return today.strftime("%B %d, %Y")
        try:
            # Try to parse the input in a specific format
            parsed_date = datetime.strptime(userInput, "%m/%d/%Y")
            return parsed_date.strftime("%B %d, %Y")
        except ValueError:
            print("Invalid date format. Please enter date as MM/DD/YYYY (e.g., 01/25/2026).")

def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    command = ""
    while command != "q":
        print(menu)
        command = input("Choose an option:\n")
        
        if command == "a":
            print("ADD ITEM TO CART")
            itemName = validString("Enter the item name:\n")
            itemDesc = validString("Enter the item description:\n")
            itemPrice = validFloat("Enter the item price:\n")
            itemQty = validInt("Enter the item quantity:\n")

            # Since this is not allowed when creating an ItemToPurchase, we validate here
            if itemQty <= 0:
                print("Quantity must be more than 0.")
                continue

            if itemPrice <= 0: 
                print("Price must be more than 0.")
                continue
    
            
            newItem = ItemToPurchase(itemName, itemPrice, itemQty, itemDesc)
            cart.add_item(newItem)
            
        elif command == "r":
            print("REMOVE ITEM FROM CART")
            itemName = validString("Enter name of item to remove:\n")
            cart.remove_item(itemName)
            
        elif command == "c":
            print("CHANGE ITEM QUANTITY")
            itemName = validString("Enter the item name:\n")
            itemQty = validInt("Enter the new quantity:\n")

            # Since this is not allowed when creating an ItemToPurchase, we validate here
            if itemQty <= 0:
                print("Quantity must be positive.")
                continue

            itemToModify = ItemToPurchase(item_name=itemName, item_quantity=itemQty)
            cart.modify_item(itemToModify)
            
        elif command == "i":
            cart.print_descriptions()
            
        elif command == "o":
            cart.print_total()
            
        elif command == "q":
            break
            
        else:
            pass


if __name__ == "__main__":
    print("Enter customer's name:")
    customerName = input()
    currentDate = validDate("Enter a date (MM/DD/YYYY or press Enter for today):\n")
    
    my_cart = ShoppingCart(customerName, currentDate)
    print_menu(my_cart)
