import random

class Warrior:

    health = None
    armor = None
    endurance = None

    def __init__(self):
        print("Воин готов!")
        self.health = 100
        self.armor = 100
        self.endurance = 100

    def gethp(self):
        return self.health

    def attack(self, other, wardef):
        if self.endurance > 0:
            self.endurance -= 10
            if other.defense():
                if other.defense > 0:
                    dmg = random.randint(0, 10)
                    if dmg < other.armor:
                        other.defense -= dmg
                        other.health -= random.randint(0, 20)
                    else:
                        dmg -= other.armor
                        other.health = other.health - random.randint(0, 20) - dmg
                else:
                    other.health -= random.randint(0, 30)
            else:
                other.health -= random.randint(0, 30)
        else:
            other.health -= (random.randint(0, 30) - random.randint(0, 10))

    def defense():
        return True

    def __del__(self):
        print("Воин пал!")

warrior1 = Warrior()
warrior2 = Warrior()
hp1 = warrior1.gethp()
hp2 = warrior2.gethp()
while (hp1 > 10) or (hp2 > 10):
    wardef = False
    action1 = random.randint(1, 2)
    action2 = random.randint(1, 2)
    if action1 == 1 and action2 == 2:
        wardef = warrior2.defense()
        warrior1.attack(warrior2, wardef)
        print("Первый воин атакует, а второй защищается!")
    elif action1 == 2 and action2 == 1:
        wardef = warrior1.defense()
        warrior2.attack(warrior1, wardef)
        print("Первый воин защищается, а второй атакует!")
    elif action1 == 1 and action2 == 2:
        warrior1.attack(warrior2)
        warrior2.attack(warrior1)
        print("Оба воина атакуют!")
    else:
        print("Оба воина защищаются!")
else:
    if (hp1 > 10) and (hp2 < 10):
        choice = input("Первый воин победил!\n Добить проигравшего?")
        if choice == "Да" or choice == "да":
            del warrior2
        else:
            print("Мудрое решение!")
    else:
        choice = input("Второй воин победил!\n Добить проигравшего?")
        if choice == "Да" or choice == "да":
            del warrior1
        else:
            print("Мудрое решение!")