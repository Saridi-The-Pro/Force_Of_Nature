from random import *
class Character:
    def __init__(self, health, damage, weapon, special_power):
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.special_power = special_power
    def info(self):
        print(f"""Weapon: {self.weapon}
        Special Power: {self.special_power}
        Health; {self.health}""")
weapons = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger"]
special_powers = ["Fire", "Water", "Ice"]
repetition = "yes"
while repetition != "no":
    hero_health = randint(15,20)
    hero_weapon = choice(weapons)
    hero_special_power = choice(special_powers)

    enemy_health = randint(15,25)
    enemy_weapon = choice(weapons)
    enemy_special_power = choice(special_powers)
    hero = Character(hero_health, hero_weapon, hero_special_power)
    enemy = Character(enemy_health, enemy_weapon, enemy_special_power)
    declaration = input("Attack the enemy?\n")
    declaration_2 = declaration.lower()
    if declaration_2 == "attack":
        print("\nHero Stats:")
        hero.info()
        print("\nEnemy Stats:")
        enemy.info()
        hero_action = input("'Attack' or 'dodge' next enemy upcoming attack?")
        hero_action_2 = hero_action.lower()
        if hero_action_2 == "attack":
            enemy_health -= 10
    else:
        print("\nHero Stats:")
        hero.info()
        print("\nEnemy Stats:")
        enemy.info()
        print("You let the enemy escaped!!")
    repetition = input("\nDo you want to restart the game? (yes/no): ").lower()