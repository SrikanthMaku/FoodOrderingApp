# You have to design a Food Ordering app for a restaurant



class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully.")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item updated successfully.")
                return
        print("Food item not found.")

    def view_food_items(self):
        print("Food Items:")
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print("------------------------")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully.")
                return
        print("Food item not found.")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self, food_items):
        ordered_items = []
        total_cost = 0
        for food_id in food_items:
            for food_item in admin.food_items:
                if food_item.food_id == food_id:
                    ordered_items.append(food_item)
                    total_cost += food_item.price
                    break
        if len(ordered_items) == 0:
            print("No food items selected.")
            return
        print("Selected Food Items:")
        for item in ordered_items:
            print(f"Food ID: {item.food_id}")
            print(f"Name: {item.name}")
            print(f"Quantity: {item.quantity}")
            print(f"Price: {item.price}")
            print(f"Discount: {item.discount}")
            print(f"Stock: {item.stock}")
            print("------------------------")
        print(f"Total Cost: {total_cost}")
        place_order = input("Do you want to place the order? (yes/no): ")
        if place_order.lower() == "yes":
            self.order_history.append(ordered_items)
            print("Order placed successfully.")
        else:
            print("Order canceled.")

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No order history.")
            return
        print("Order History:")
        for order_items in self.order_history:
            for item in order_items:
                print(f"Food ID: {item.food_id}")
                print(f"Name: {item.name}")
                print(f"Quantity: {item.quantity}")
                print(f"Price: {item.price}")
                print(f"Discount: {item.discount}")
                print(f"Stock: {item.stock}")
                print("------------------------")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully.")


admin = Admin()
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 Piece", 320, 0, 5)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 8)


user = User("John Doe", "1234567890", "john.doe@example.com", "123 Main St", "password")
user.place_new_order([2, 3])
user.view_order_history()
user.update_profile("John Smith", "9876543210", "john.smith@example.com", "456 Elm St", "newpassword")






