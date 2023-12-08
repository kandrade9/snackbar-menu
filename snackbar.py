class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def get_item_name(self):
        return self.item_name

    def get_item_price(self):
        return self.item_price

    def set_item_name(self, new_item):
        self.item_name = new_item

    def set_item_price(self, new_price):
        self.item_price = new_price

    def __repr__(self):
        return self.item_name + ": $" + f"{self.item_price:.2f}"


class Menu(MenuItem):
    def __init__(self):
        self.menu_list = []
        self.items = []

    def add_item(self, *args):
        for arg in args:
            self.menu_list.append(arg)
            item_name = arg.get_item_name()
            self.items.append(item_name)

    def order(self, *args):
        total_price = 0.0
        for arg in args:
            if arg in self.items:
                index = self.items.index(arg)
                menu_item = self.menu_list[index]
                item_price = menu_item.get_item_price()
                total_price += item_price
            else:
                print(f'{arg} NOT in menu')
        return total_price

    def __repr__(self):
        menu = ""
        for item in self.menu_list:
            menu += str(item) + "\n"
        return menu


item_1 = MenuItem("Burger", 9.50)
item_2 = MenuItem("Pizza", 7.0)
item_3 = MenuItem("Empanadas", 2)
item_4 = MenuItem("Chaufa", 12)

menu = Menu()
menu.add_item(item_1, item_2, item_3, item_4)
print(menu)

add_item = input("Would you like to add an item to the menu? (y/n): ")
if add_item == "y":
    user_item = input("What item would you like to add?: ").title()
    user_item_price = float(input("What would the price be?: "))
    new_item = MenuItem(user_item, user_item_price)
    menu.add_item(new_item)
    print(menu)

user_order = input("What would you like to order?: ")
users_items = user_order.split(", ")
total_price = 0
for item in users_items:
    total_price += menu.order(item.title())
print(f"Your total is {total_price}")
