class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

def sumItems(items):
    print("TOTAL COST\n")
    grand_total = 0.0
    for item in items:
        item.print_item_cost()
        print()
        grand_total += (item.item_price * item.item_quantity)
    
    print(f"Total: ${grand_total:.2f}")

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


if __name__ == "__main__":
    items = []
    
    while True:
        print(f"\nItem {len(items) + 1}")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name: ")
        item.item_price = validFloat("Enter the item price: ")
        item.item_quantity = validInt("Enter the item quantity: ")
        items.append(item)
        
        response = input("Do you have another item? (y/n): ")
        if response.lower() != 'y':
            break

    sumItems(items)