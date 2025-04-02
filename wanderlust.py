class Room:
    def __init__(self, name, description, exits=None):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}

    def describe(self):
        print(self.description)

    def get_exit(self, direction):
        return self.exits.get(direction, None)