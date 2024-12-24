from random import choice, randint
from time import sleep

class Character:
    def __init__(self, health, weapon, special_power_1, special_power_2):
        self.health = health
        self.weapon = weapon
        self.special_power_1 = special_power_1
        self.special_power_2 = special_power_2
        self.is_frozen = False  # For Ice effect
        self.weapon_damage = self.set_weapon_damage()
        self.dodge_chance = 50  # Default dodge chance (percent)

    def set_weapon_damage(self):
        weapon_damage = {
            "Long Sword": (7, 10),
            "Katana": (8, 11),
            "Bow": (5, 9),
            "Throwable Knife": (3, 6),
            "Axe": (9, 12),
            "Mace": (8, 10),
            "Spear": (6, 10),
            "Dagger": (4, 7),
            "Staff": (5, 8),
            "TREBUCHET": (15, 15)  # Fixed damage for TREBUCHET
        }
        return weapon_damage.get(self.weapon, (5, 8))  # Default damage for unknown weapons
    
    def dodge(self):
        # Dodge chance with failure possibility
        if randint(1, 100) <= self.dodge_chance:
            print("\nYou successfully dodged the enemy's attack!")
            return True
        else:
            print("\nYou failed to dodge the enemy's attack!")
            return False

    def info(self):
        return f"""
        Weapon: {self.weapon}
        Special Powers: {self.special_power_1}, {self.special_power_2}
        Health: {self.health}
        Dodge Chance: {self.dodge_chance}%
        """

def calculate_damage(min_damage, max_damage, special_power_1, special_power_2):
    base_damage = randint(min_damage, max_damage)
    
    # Special power interactions for hero
    if special_power_1 == "Fire":
        if special_power_2 == "Ice" or special_power_2 == "Earth":
            base_damage += 3  # Fire deals more damage to Ice and Earth
    elif special_power_1 == "Water":
        if special_power_2 == "Fire":
            base_damage += 2  # Water can reduce Fire's damage
    elif special_power_1 == "Ice":
        if special_power_2 == "Water":
            base_damage += 4  # Ice can damage Water more
    # Other element interactions can be added here...

    return base_damage

# List of weapons and powers
weapons = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger", "Staff", "TREBUCHET"]
special_powers = ["Fire", "Water", "Ice", "Lightning", "Earth", "Wind"]

# Level player from 0
level = 0
additional_health = 0

# Main game loop
repetition = "yes"
score = 0  # Track the number of enemies defeated
print("Game created by Saridi and Nicander!!")
sleep(4)
print("FORCE OF NATURE!!")
sleep(4)
print("V.1.2.1")
sleep(4)
print("Don't forget to follow our Instagram account!!")
sleep(4)
print("Saridi: https://www.instagram.com/s4r_m4l3z_404/")
print("Nicander: https://www.instagram.com/nicander_arif/")
sleep(4)

while repetition == "yes":
    # Initialize Hero and Enemy with two special powers each
    hero = Character(randint(40, 50), choice(weapons), choice(special_powers), choice(special_powers))
    hero.health += additional_health
    enemy = Character(randint(40, 50), choice(weapons), choice(special_powers), choice(special_powers))
    
    print("\nA new enemy approaches!")
    declaration = input("Attack the enemy? (yes/no): ").strip().lower()
    while declaration != "yes" and declaration != "no":
        declaration = input("Attack the enemy? (yes/no): ").strip().lower()

    if declaration == "yes":
        print("\nHero Stats:")
        print(hero.info())
        print("\nEnemy Stats:")
        print(enemy.info())
        
        while hero.health > 0 and enemy.health > 0:
            # Hero's turn
            hero_action = input("Choose action: 'attack' or 'dodge': ").strip().lower()
            while hero_action != "attack" and hero_action != "dodge":
                hero_action = input("Choose action: 'attack' or 'dodge': ").strip().lower()
            
            if hero_action == "attack":
                damage = calculate_damage(*hero.weapon_damage, hero.special_power_1, hero.special_power_2)
                enemy.health -= damage
                sleep(2)
                print(f"\nYou attacked the enemy and dealt {damage} damage using your {hero.weapon}!")
            
            elif hero_action == "dodge":
                if hero.dodge():
                    continue
            
            # Check if enemy is still alive
            if enemy.health <= 0:
                break
            
            # Enemy's turn (skipped if frozen)
            if not enemy.is_frozen:
                damage = calculate_damage(*enemy.weapon_damage, enemy.special_power_1, enemy.special_power_2)
                hero.health -= damage
                sleep(2)
                print(f"The enemy attacked and dealt {damage} damage using their {enemy.weapon}!")
                
            else:
                sleep(2)
                enemy.is_frozen = False  # Reset frozen state after one turn

            # Show updated health
            sleep(2)
            if hero.health < 0:
                hero.health = 0
            if enemy.health < 0:
                enemy.health = 0
            print(f"\nHero Health: {hero.health}")
            print(f"Enemy Health: {enemy.health}")
        
        # Determine winner
        if hero.health > 0:
            print("\nYou defeated the enemy!")
            score += 1
            level += 1  # Increase hero's level
            additional_health += 1
            print(f"\nHero Level: {level}")
            print(f"Hero Health: {hero.health}")
            print(f"Enemy Health: {enemy.health}")
        else:
            print("\nYou have been defeated by the enemy!")
            break
    
    else:
        print("\nYou let the enemy escape!")
    
    repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()
    while repetition != "yes" and repetition != "no":
        repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()

# Endgame summary
print("\nGame Over!\n")
sleep(4)
print(f"Hero last Level: {level}")
sleep(4)
print(f"Enemies Defeated: {score}\n")
sleep(4)
print("Thanks for playing!")
