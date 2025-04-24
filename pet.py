# pet.py

class Pet:
    def __init__(self, name, pet_type="Unknown"):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self, food="food"):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} the {self.pet_type} is eating {food}...")

    def sleep(self, duration=1):
        self.energy = min(10, self.energy + duration)
        print(f"{self.name} the {self.pet_type} is sleeping for {duration} hours...")

    def play(self, activity="playing"):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} the {self.pet_type} is {activity}...")
        else:
            print(f"{self.name} the {self.pet_type} is too tired to play.")

    def get_status(self):
        print(f"{self.name} the {self.pet_type}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} the {self.pet_type} learned a new trick: {trick}")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} the {self.pet_type}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} the {self.pet_type} hasn't learned any tricks yet.")