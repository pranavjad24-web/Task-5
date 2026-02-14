class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with sword, Power:", self.power)

class Mage(Character):
    def attack(self):
        print("Mage casts spell, Power:", self.power)

w = Warrior(100, 50)
w.attack()
