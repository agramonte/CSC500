from datetime import date
from datetime import datetime



# From previous module
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


def sumItemsToPurchase(items):
    print("TOTAL COST\n")
    grand_total = 0.0
    for item in items:
        item.print_item_cost()
        print()
        grand_total += (item.item_price * item.item_quantity)

    print(f"Total: ${grand_total:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
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


def getValidDate():
    print("Enter today's date:")
    while True:
        dateInput = input()
        if not dateInput.strip():
            # Default to today if input is empty
            return date.today().strftime("%B %d, %Y")

        try:
            # Validate format: Month Day, Year (e.g., February 8, 2026)
            validDate = datetime.strptime(dateInput, "%B %d, %Y")
            return validDate.strftime("%B %d, %Y")
        except ValueError:
            print("Invalid date format. Please use 'Month Day, Year' (e.g., February 1, 2020).")
            print("Enter today's date:")


def print_menu(cart):
    items_to_purchase_list = []

    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
apl - Add items to purchase list
ppl - Print items in purchase list
aplC - Add purchase list to cart
rm - Remove items from purchase list
q - Quit
"""
    command = ""
    while command != "q":
        print(menu)
        command = input("Choose an option:\n")

        if command == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = validFloat("Enter the item price:\n")
            item_quantity = validInt("Enter the item quantity:\n")

            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)

        elif command == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif command == "c":
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            qty = validInt("Enter the new quantity:\n")
            item_to_modify = ItemToPurchase(item_name=item_name, item_quantity=qty)
            cart.modify_item(item_to_modify)

        elif command == "i":
            cart.print_descriptions()

        elif command == "o":
            cart.print_total()

        elif command == "apl":
            print("ADD ITEM TO PURCHASE LIST")
            itemName = input("Enter the item name:\n")
            itemDescription = input("Enter the item description:\n")
            itemPrice = validFloat("Enter the item price:\n")
            itemQuantity = validInt("Enter the item quantity:\n")

            newItem = ItemToPurchase(itemName, itemPrice, itemQuantity, itemDescription)

            items_to_purchase_list.append(newItem)
            print(f"\n Item list after adding new item:")
            newItem.print_item_cost()

        elif command == "ppl":
            print("PRINT ITEMS IN PURCHASE LIST")
            if not items_to_purchase_list:
                print("Purchase list is empty.")
            else:
                sumItemsToPurchase(items_to_purchase_list)

        elif command == "aplC":
            print("ADD PURCHASE LIST TO CART")
            if not items_to_purchase_list:
                print("Purchase list is empty. Nothing to add.")
            else:
                for item in items_to_purchase_list:
                    cart.add_item(item)
                print("All items from purchase list added to cart.")
        elif command == "rm":
            items_to_purchase_list.clear()
            print("Purchase list cleared.")

        elif command == "q":
            break

        else:
            pass


if __name__ == "__main__":
    print("Enter customer's name:")
    customer_name = input()
    current_date = getValidDate()
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    my_cart = ShoppingCart(customer_name, current_date)
    print_menu(my_cart)
