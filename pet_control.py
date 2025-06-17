class Pet():
    def __init__(self, name, pet_type):
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")

        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.alive = True
        self.age = 1
        self.date_create = date
        self.name = name
        self.pet_type = pet_type

    def feed(self):
        self.hunger -= 4

    def rest(self):
        self.energy += 2
        self.hunger += 1

    def play(self):
        self.happiness += 4
        self.energy -= 2
        self.hunger += 1

    def tick(self):
        self.happiness -= 1
        self.hunger += 1

    def status(self):
        stats = [self.hunger, self.energy, self.happiness, self.age, self.alive]
        return stats

    def give_status(self, stats):
        self.hunger = max(0, min(stats[0], 10))
        self.energy = max(0, min(stats[1], 10))
        self.happiness = max(0, min(stats[2], 10))
