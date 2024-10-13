'''class Item:
    def __init__(self, item_id, name, category, unit_price, stock_quantity, stock_threshold):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
        self.stock_threshold = stock_threshold
    def total_value(self):
        return self.unit_price * self.stock_quantity



class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        for item in self.items:
            print(f"ID: {item.item_id}, Name: {item.name}, Category: {item.category}, "
                  f"Unit Price: {item.unit_price}, Quantity: {item.stock_quantity}, "
                  f"Min Threshold: {item.stock_threshold}")

    def find_item(self, search_term):
        found_items = [item for item in self.items if search_term.lower() in item.name.lower() or
                       search_term.lower() in item.category.lower()]
        return found_items

    def update_stock(self, item_name, quantity_change):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.stock_quantity += quantity_change
                print(f"Updated {item_name}. New Quantity: {item.stock_quantity}")
                return
        print(f"Item '{item_name}' not found.")

    def list_below_threshold(self):
        low_stock_items = [item for item in self.items if item.stock_quantity < item.stock_threshold]
        if low_stock_items:
            print("\nItems below Minimum Stock Threshold:")
            for item in low_stock_items:
                Required_stock = item.stock_threshold - item.stock_quantity
                print(f"Name: {item.name}, Current Quantity: {item.stock_quantity}, "
                      f"Min Threshold: {item.stock_threshold}, Required_stock: {Required_stock}")
        else:
            print("No items are below the minimum stock threshold.")

    def generate_report(self):
        if not self.items:
            print("Inventory is empty. No report to generate.")
            return

        print("\nInventory Report:")
        print(f"{'Item ID':<10} {'Item Name':<20} {'Category':<15} {'Unit Price':<12} "
              f"{'Stock Qty':<15} {'Total Value':<15}")
        print("-" * 95)  
        for item in self.items:
            total_value = item.total_value()
            print(f"{item.item_id:<10} {item.name:<20} {item.category:<15} "
                  f"{item.unit_price:<12} {item.stock_quantity:<15} {total_value:<15}")

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
            item_id = len(self.inventory.items) + 1  
            name = input("Enter Item Name (or 'stop' to finish): ")
            if name.lower() == 'stop':
                break
            category = input("Enter Category: ")
            unit_price = float(input("Enter Unit Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))
            stock_threshold = int(input("Enter Stock Threshold: "))

            item = Item(item_id, name, category, unit_price, stock_quantity, stock_threshold)
            self.inventory.add_item(item)

        while True:
            print("\nInventory Management Menu:")
            print("1. Display Inventory")
            print("2. Search Item")
            print("3. Update Stock Quantity")
            print("4. List Items Below Minimum Stock Threshold")
            print("5. Generate Inventory Report")
            print("6. Exit")

            choice = input("Choose an option (1-6): ")
            if choice == '1':
                self.inventory.display_inventory()
            elif choice == '2':
                search_term = input("Enter item name or category to search: ")
                found_items = self.inventory.find_item(search_term)
                if found_items:
                    print("\nSearch Results:")
                    for item in found_items:
                        print(f"ID: {item.item_id}, Name: {item.name}, Category: {item.category}, "
                              f"Unit Price: {item.unit_price}, Quantity: {item.stock_quantity}, "
                              f"Min Threshold: {item.stock_threshold}")
                else:
                    print("No items found.")
            elif choice == '3':
                item_name = input("Enter item name to update: ")
                quantity_change = int(input("Enter quantity to add (positive) or subtract (negative): "))
                self.inventory.update_stock(item_name, quantity_change)
            elif choice == '4':
                self.inventory.list_below_threshold()
            elif choice == '5':
                self.inventory.generate_report()
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.run()





'''

import matplotlib.pyplot as plt  # Correct import statement

class Item:
    def __init__(self, item_id, name, category, unit_price, stock_quantity, stock_threshold):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
        self.stock_threshold = stock_threshold

    def total_val(self):
        return self.unit_price * self.stock_quantity


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        for item in self.items:
            print(f"ID: {item.item_id}, Name: {item.name}, Category: {item.category}, "
                  f"Unit Price: {item.unit_price}, Quantity: {item.stock_quantity}, "
                  f"Min Threshold: {item.stock_threshold}")

    def find_item(self, search_term):
        found_items = [item for item in self.items if search_term.lower() in item.name.lower() or
                       search_term.lower() in item.category.lower()]
        return found_items

    def update_stock(self, item_name, quantity_change):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.stock_quantity += quantity_change
                print(f"Updated {item_name}. New Quantity: {item.stock_quantity}")
                return
        print(f"Item '{item_name}' not found.")

    def list_below_threshold(self):
        low_stock_items = [item for item in self.items if item.stock_quantity < item.stock_threshold]
        if low_stock_items:
            print("\nItems below Minimum Stock Threshold:")
            for item in low_stock_items:
                Required_stock = item.stock_threshold - item.stock_quantity
                print(f"Name: {item.name}, Current Quantity: {item.stock_quantity}, "
                      f"Min Threshold: {item.stock_threshold}, Required_stock: {Required_stock}")
        else:
            print("No items are below the minimum stock threshold.")

    def generate_report(self):
        if not self.items:
            print("Inventory is empty. No report to generate.")
            return

        print("\nInventory Report:")
        print(f"{'Item ID':<10} {'Item Name':<20} {'Category':<15} {'Unit Price':<12} "
              f"{'Stock Qty':<15} {'Total Value':<15}")
        print("-" * 95)  
        for item in self.items:
            total_val = item.total_val()
            print(f"{item.item_id:<10} {item.name:<20} {item.category:<15} "
                  f"{item.unit_price:<12} {item.stock_quantity:<15} {total_val:<15}")

    def generate_stock_level_chart(self):
        if not self.items:
            print("No items in inventory to generate a chart.")
            return

        item_names = [item.name for item in self.items]
        stock_levels = [item.stock_quantity for item in self.items]
        colors = ['red' if item.stock_quantity < item.stock_threshold else 'skyblue' for item in self.items]
        plt.figure(figsize=(10, 6))
        plt.bar(item_names, stock_levels, color=colors)
        plt.xlabel('Items')
        plt.ylabel('Stock Quantity')
        plt.title('Stock Levels of Items')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = Inventory()

    def run(self):
        while True:
            item_id = len(self.inventory.items) + 1  
            name = input("Enter Item Name (or 'stop' to finish): ")
            if name.lower() == 'stop':
                break
            category = input("Enter Category: ")
            unit_price = float(input("Enter Unit Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))
            stock_threshold = int(input("Enter Stock Threshold: "))

            item = Item(item_id, name, category, unit_price, stock_quantity, stock_threshold)
            self.inventory.add_item(item)

        while True:
            print("\nInventory Management Menu:")
            print("1. Display Inventory")
            print("2. Search Item")
            print("3. Update Stock Quantity")
            print("4. List Items Below Minimum Stock Threshold")
            print("5. Generate Inventory Report")
            print("6. Generate Stock Level Chart")  # New option for chart generation
            print("7. Exit")

            choice = input("Choose an option (1-7): ")
            if choice == '1':
                self.inventory.display_inventory()
            elif choice == '2':
                search_term = input("Enter item name or category to search: ")
                found_items = self.inventory.find_item(search_term)
                if found_items:
                    print("\nSearch Results:")
                    for item in found_items:
                        print(f"ID: {item.item_id}, Name: {item.name}, Category: {item.category}, "
                              f"Unit Price: {item.unit_price}, Quantity: {item.stock_quantity}, "
                              f"Min Threshold: {item.stock_threshold}")
                else:
                    print("No items found.")
            elif choice == '3':
                item_name = input("Enter item name to update: ")
                quantity_change = int(input("Enter quantity to add (positive) or subtract (negative): "))
                self.inventory.update_stock(item_name, quantity_change)
            elif choice == '4':
                self.inventory.list_below_threshold()
            elif choice == '5':
                self.inventory.generate_report()
            elif choice == '6':
                self.inventory.generate_stock_level_chart()  # Call the new function to generate the chart
            elif choice == '7':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.run()
