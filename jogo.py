import random

# Character: parent class
# Hero: controlled by the user
# Enemy: user's opponent

class Character:
    def __init__(self, name, health, level):
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_level(self):
        return self.__level
    
    def show_details(self):
        return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"
    
    def receive_attack(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.__health = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)  # based on level
        target.receive_attack(damage)
        print(f"{self.get_name()} attacked {target.get_name()} and dealt {damage} damage")

class Hero(Character):
    def __init__(self, name, health, level, skill):
        super().__init__(name, health, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill
    
    def show_details(self):
        return f"{super().show_details()}\nSkill: {self.get_skill()}\n"
    
    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)  # increased damage
        target.receive_attack(damage)
        print(f"{self.get_name()} used the special skill {self.get_skill()} on {target.get_name()} and dealt {damage} damage")

class Enemy(Character):
    def __init__(self, name, health, level, type_):
        super().__init__(name, health, level)
        self.__type = type_
    
    def get_type(self):
        return self.__type
    
    def show_details(self):
        return f"{super().show_details()}\nType: {self.get_type()}\n"

class Game:
    """ Main game orchestrator class """

    def __init__(self):
        self.hero = Hero(name="Guinga", health=100, level=5, skill="Super Strength")
        self.enemy = Enemy(name="Dssshhhalma", health=80, level=5, type_="Flying")

    def start_battle(self):
        """ Manages the turn-based battle """
        print("Starting the battle!")   
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\nCharacter details:")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("Press ENTER to attack... ")
            choice = input("Choose (1 = Normal Attack, 2 = Special Attack): ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("Invalid choice. Please choose again.")

            if self.enemy.get_health() > 0:
                # Enemy attacks hero
                self.enemy.attack(self.hero)

        if self.hero.get_health() > 0:
            print("\nCongratulations! You won the battle!")
        else:
            print("You were defeated!")

# Create a game instance and start the battle
game = Game()
game.start_battle()


# Example testing code (commented out):
# hero = Hero(name="Guinga", health=100, level=5, skill="Super Strength")
# print(hero.show_details())
# enemy = Enemy(name="Dssshhhalma", health=50, level=3, type_="Flying")
# print(enemy.show_details())
