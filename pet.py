class Pet():
    def __init__(self, energy, hunger, age, alive, happiness, date_create):

        import datetime

        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        print("Date:", date)

        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.alive = True
        self.age = 1
        self.date_create = date

    def eat(self):
        self.hunger += 4

    def sleep(self):
        self.energy += 2

    def play(self):
        self.happiness += 2
        self.energy -= 2

    def tick():
        print("Later me")
        pass