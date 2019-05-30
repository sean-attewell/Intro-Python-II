# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def listInventory(self):
        output = "\033[0;32mYou rummage through your bag and see the following items:\033[0m"
        if len(self.inventory) < 1:
            output = "\033[31mYou can't see any items in your bag...\033[m\n"
        for item in self.inventory:
            output += "\n" + str(item.name) + ": " + str(item.description)

        return print(output + "\n")

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        self.inventory.remove(item)
