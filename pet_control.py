class Pet():
    def __init__(self, name, pet_type):
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")

        self.hunger = 10
        self.energy = 10
        self.happiness = 10
        self.alive = True
        self.age = 1
        self.date_create = date
        self.name = name
        self.pet_type = pet_type

    def feed(self):
        self.hunger += 4

    def rest(self):
        self.energy += 2
        self.hunger -= 1

    def play(self):
        self.happiness += 4
        self.energy -= 2
        self.hunger -= 1

    def tick(self):
        self.happiness -= 1
        self.age += 1
        if self.hunger < 10:
            self.hunger -= 1

    def status(self):
        stats = [self.hunger, self.energy, self.happiness, self.age, self.alive]
        return stats

    def give_status(self, stats):
        self.hunger = max(0, min(stats[0], 10))
        self.energy = max(0, min(stats[1], 10))
        self.happiness = max(0, min(stats[2], 10))

    def to_dict(self):
        return {
            'hunger': self.hunger,
            'energy': self.energy,
            'happiness': self.happiness,
            'alive': self.alive,
            'age': self.age,
            'date_create': self.date_create,
            'name': self.name,
            'pet_type': self.pet_type
        }

    @classmethod
    def from_dict(cls, data):
        pet = cls(data['name'], data['pet_type'])
        pet.hunger = data.get('hunger', 0)
        pet.energy = data.get('energy', 10)
        pet.happiness = data.get('happiness', 10)
        pet.alive = data.get('alive', True)
        pet.age = data.get('age', 1)
        pet.date_create = data.get('date_create', '')
        return pet
