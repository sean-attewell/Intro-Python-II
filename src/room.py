# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items_in_room):
        self.name = name
        self.description = description
        self.items_in_room = items_in_room

    def __str__(self):
        return f'You find yourself located:\n{self.name}.\n\n{self.description}'

    def listItems(self):
        output = "\033[0;32mYou scour the room and see the following items:\033[0m"
        if len(self.items_in_room) < 1:
            output = "\033[31mYou can't see any items in this room...\033[m\n"
        for item in self.items_in_room:
            output += "\n" + str(item.name) + ": " + str(item.description)

        return print(output + "\n")

    def removeItem(self, item):
        self.items_in_room.remove(item)

    def addItem(self, item):
        self.items_in_room.append(item)
