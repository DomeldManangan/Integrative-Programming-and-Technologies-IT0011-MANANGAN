class Item:
    def __init__(self, item_id, name, description, price):
        if not name or not description:
            raise ValueError("Name and description cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class ItemManager:
    def __init__(self):
        self.items = {}
        self.next_id = 1
    
    def create_item(self, name, description, price):
        try:
            item = Item(self.next_id, name, description, price)
            self.items[self.next_id] = item
            self.next_id += 1
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self, item_id, name, description, price):
        if item_id not in self.items:
            print("Item not found.")
            return
        
        try:
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item not found.")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management Menu:")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            try:
                price = float(input("Enter item price: "))
                manager.create_item(name, description, price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new item name: ")
                description = input("Enter new item description: ")
                price = float(input("Enter new item price: "))
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter valid values.")
        elif choice == '4':
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input. Please enter a valid ID.")
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()