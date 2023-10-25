class Dog: #dog class

    def __init__(self, name): #initializes dog
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick): #dog learns trick
        self.tricks.append(trick)
