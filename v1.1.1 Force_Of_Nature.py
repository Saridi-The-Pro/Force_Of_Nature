from random import choice, randint
from time import *
class Character:
    def __init__(self, health, weapon, special_power):
        self.health = health
        self.weapon = weapon
        self.special_power = special_power
        self.is_frozen = False  # For Ice effect
    def info(self):
        return f"""
        Weapon: {self.weapon}
        Special Power: {self.special_power}
        Health: {self.health}
        """
# List of weapons and powers
weapons = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger", "Staff"]
special_powers = ["Fire", "Water", "Ice", "Lightning", "Earth", "Wind"]
# Level player from 0
level = 0
# Every increase 1, increase 1 health
additional_health = 0
# Main game loop
repetition = "yes"
score = 0  # Track the number of enemies defeated
print("Game created by Saridi and Nicander!!")
sleep(4)
print("UNTITLED RPG GAME!!")
sleep(4)
print("V2.1.1")
sleep(4)
print("Don't forget to follow our Instagram account!!")
sleep(4)
print("Saridi: https://www.instagram.com/s4r_m4l3z_404/")
print("Nicander: https://www.instagram.com/nicander_arif/")
sleep(4)
while repetition == "yes":
    # Initialize Hero and Enemy
    hero = Character(randin(40,50), choice(weapons), choice(special_powers))
    hero.health += additional_health
    enemy = Character(randint(40,50), choice(weapons), choice(special_powers))
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
                damage = randint(5, 10)  # Randomize damage
                enemy.health -= damage
                sleep(2)
                print(f"\nYou attacked the enemy and dealt {damage} damage!")
                # Hero's special power effect
                if hero.special_power == "Fire":
                    burn_damage = 2
                    if enemy.special_power == "Ice" or enemy.special_power == "Earth":
                        burn_damage = 4
                    enemy.health -= burn_damage
                    sleep(2)
                    print(f"Your fire power burns the enemy for {burn_damage} extra damage!")
                elif hero.special_power == "Water":
                    heal = 2
                    if enemy.special_power == "Fire" or enemy.special_power == "Lightning" or enemy.special_power == "Earth":
                        water_damage = 3
                        heal = 4
                        enemy.health -= water_damage
                        sleep(2)
                        print(f"Your water power make enemy cold for {water_damage} extra damage!")
                    hero.health += heal
                    sleep(2)
                    print(f"Your water power heals you for {heal} health!")
                elif hero.special_power == "Ice":
                    freezing_damage = 2
                    if enemy.special_power == "Water":
                        freezing_damage = 4
                    enemy.health -= freezing_damage
                    sleep(2)
                    print(f"Your ice power make enemy hypothermia for {freezing_damage} extra damage!")
                    if randint(1,4) == 1:
                        enemy.is_frozen = True
                        sleep(2)
                        print("Your ice power freezes the enemy! They lose their next turn!")
                elif hero.special_power == "Lightning":
                    burn_damage = 4
                    enemy.health -= burn_damage
                    sleep(2)
                    print(f"Your lightning power create fire that burn the enemy for {burn_damage} extra damage!")
                    if enemy.special_power == "Water":
                        if randint(1,2) == 1:
                            enemy.is_frozen = True
                            print("Your lightning power make the enemy shock too! They lose their next turn!")
                    if randint(1,3) == 2:
                        enemy.is_frozen = True
                        print("Your lightning power make the enemy shock too! They lose their next turn!")
                elif hero.special_power == "Earth":
                    puncture_damage = 3
                    enemy.health -= puncture_damage
                    sleep(2)
                    print(f"Your earth power impaled the enemy for {puncture_damage} extra damage!")
                    if randint(1,3) == 2:
                        enemy.is_frozen = True
                        sleep(2)
                        print("Your earth power create barrier that holding enemy attack")
                        if randint(1,3) == 2:
                            puncture_damage += 4
                            enemy.is_frozen = True
                            sleep(2)
                            print(f"Your earth power make the enemy is bounced because the attack is below the enemy for {puncture_damage} extra damage!")
                elif hero.special_power == "Wind":
                    wind_damage = 3
                    enemy.health -= wind_damage
                    sleep(2)
                    print(f"Your wind power push enemy for {wind_damage} extra damage!")
                    if enemy.special_power == "Lightning":
                        burn_damage = burn_damage / 2
                        print("Enemy's burn damage have been devided by 2!!")
            elif hero_action == "dodge":
                sleep(2)
                print("\nYou dodged the enemy's attack!")
                continue
            # Check if enemy is still alive
            if enemy.health <= 0:
                break
            # Enemy's turn (skipped if frozen)
            if not enemy.is_frozen:
                damage = randint(5, 8)
                hero.health -= damage
                sleep(2)
                print(f"The enemy attacked and dealt {damage} damage!")
                # Enemy's special power effect
                if enemy.special_power == "Fire":
                    burn_damage = 2
                    if hero.special_power == "Ice" or hero.special_power == "Earth":
                        burn_damage = 4
                    hero.health -= burn_damage
                    sleep(2)
                    print(f"The enemy's fire power burns you for {burn_damage} extra damage!")
                elif enemy.special_power == "Water":
                    heal = 2
                    if hero.special_power == "Fire" or hero.special_power == "Lightning" or hero.special_power == "Earth":
                        water_damage = 3
                        heal = 4
                        hero.health -= water_damage
                        sleep(2)
                        print(f"Enemy's water power make you cold for {water_damage} extra damage!")
                    enemy.health += heal
                    sleep(2)
                    print(f"The enemy's water power heals them for {heal} health!")
                elif enemy.special_power == "Ice":
                    freezing_damage = 2
                    if hero.special_power == "Water":
                        freezing_damage = 4
                    hero.health -= freezing_damage
                    sleep(2)
                    print(f"Enemy's ice power make you hypothermia for {freezing_damage} extra damage!")
                    if randint(1,4) == 1:
                        enemy.is_frozen = True
                        sleep(2)
                        print("Enemy's ice power freezes you! You lose your next turn!")
                elif enemy.special_power == "Lightning":
                    burn_damage = 4
                    hero.health -= burn_damage
                    sleep(2)
                    print(f"The enemy's lightning power create fire that burn you for {burn_damage} extra damage!")
                    if hero.special_power == "Water":
                        if randint(1,2) == "1":
                            hero.is_frozen = True
                            print("The enemy's lightning power make you shock too! You lose your next turn!")
                    if randint(1,3) == 2:
                        hero.is_frozen = True
                        print("The enemy's lightning power make you shock too! You lose your next turn!")
                elif enemy.special_power == "Earth":
                    puncture_damage = 3
                    hero.health -= puncture_damage
                    sleep(2)
                    print(f"The enemy's earth power impaled you for {puncture_damage} extra damage!")
                    if randint(1,3) == 2:
                        hero.is_frozen = True
                        sleep(2)
                        print("The enemy's earth power create barrier that holding your attack")
                        if randint(1,3) == 2:
                            puncture_damage += 4
                            hero.is_frozen = True
                            sleep(2)
                            print(f"The enemy's earth power make you bounced because the attack is below you for {puncture_damage} extra damage!")
                elif enemy.special_power == "Wind":
                    wind_damage = 3
                    hero.health -= wind_damage
                    sleep(2)
                    print(f"Enemy's wind power push you for {wind_damage} extra damage!")
                    if hero.special_power == "Lightning":
                        burn_damage = burn_damage / 2
                        print("Your burn damage have been devided by 2!!")
            else:
                sleep(2)
                enemy.is_frozen = False  # Reset frozen state
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
            if enemy.health < 0:
                enemy.health = 0
            print("\nYou defeated the enemy!")
            sleep(2)
            # Level-up mechanic
            if score >= 5:
                if score % 5 == 0:
                    level += 1
                    additional_health += 1
                    print(f"You leveled up! Now your level is {level}! Your health increased by 1!")
            print(f"\nHero Level: {level}")
            print(f"Hero Health: {hero.health}")
            print(f"Enemy Health: {enemy.health}")
            score += 1
        else:
            if hero.health < 0:
                hero.health = 0
            print("\nYou have been defeated by the enemy!")
            sleep(2)
            print(f"\nHero Level: {level}")
            print(f"Hero Health: {hero.health}")
            print(f"Enemy Health: {enemy.health}")
            break
    else:
        print("\nYou let the enemy escape!")
        sleep(2)
    repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()
    sleep(2)
    while repetition != "yes" and repetition != "no":
        repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()
        sleep(2)
# Endgame summary
print("\nGame Over!\n")
sleep(4)
print(f"Hero last Level: {level}")
sleep(4)
print(f"Enemies Defeated: {score}\n")
sleep(4)
print("Thanks for playing!")
