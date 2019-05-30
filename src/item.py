class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def onTake(self):
        print(
            f"\033[0;32mYou took the {self.name} and put it in your bag\033[0m\n")

    def onDrop(self):
        print(
            f"\033[0;32mYou took the {self.name} out of your bag and dropped it in the room.\033[0m\n")
