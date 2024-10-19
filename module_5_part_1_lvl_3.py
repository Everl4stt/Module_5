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

    def attack(self, other, defense):
        if self.endurance > 0:
            self.endurance -= 10
            if defense:
                if other.armor > 0:
                    dmg = random.randint(0, 10)
                    if dmg < other.armor:
                        other.armor -= dmg
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

    def defense(self):
        return True

    def __del__(self):
        print("Воин пал!")

warrior1 = Warrior()
warrior2 = Warrior()
turn = 0
while (warrior1.health > 10) and (warrior2.health > 10):
    turn += 1
    print("Ход номер: ", turn)
    defense = False
    action1 = random.randint(1, 2)
    action2 = random.randint(1, 2)
    if action1 == 1 and action2 == 2:
        defense = warrior2.defense()
        warrior1.attack(warrior2, defense)
        print("Первый воин атакует, а второй защищается!")
        print("Здоровье первого: ", warrior1.health, ", здоровье второго: ", warrior2.health)
    elif action1 == 2 and action2 == 1:
        defense = warrior1.defense()
        warrior2.attack(warrior1, defense)
        print("Первый воин защищается, а второй атакует!")
        print("Здоровье первого: ", warrior1.health, ", здоровье второго: ", warrior2.health)
    elif action1 == 1 and action2 == 1:
        warrior1.attack(warrior2, defense)
        warrior2.attack(warrior1, defense)
        print("Оба воина атакуют!")
        print("Здоровье первого: ", warrior1.health, ", здоровье второго: ", warrior2.health)
    else:
        print("Оба воина защищаются!")
        print("Здоровье первого: ", warrior1.health, ", здоровье второго: ", warrior2.health)
else:
    if (warrior1.health > 10) and (warrior2.health < 10):
        choice = input("Первый воин победил!\nДобить проигравшего?\n")
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