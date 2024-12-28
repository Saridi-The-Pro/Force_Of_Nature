# Import modules from the standard library
import random
from random import randint, choice
from time import sleep
"""This file contains the source code for the Force of Nature game.
It includes a class for representing characters, a class for representing
weapons, a class for representing special powers, and a function for
running the game."""
# Constants
# A list of all the weapons available in the game
WEAPONS = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger", "Staff", "TREBUCHET"]
# A list of all the special powers available in the game
SPECIAL_POWERS = ["Fire", "Water", "Ice", "Lightning", "Earth", "Wind"]
# The amount of time to sleep between each output in the game
SLEEP_DURATION = 2
class Character:
    def __init__(self, name, health, weapon, special_power_1, special_power_2):
        """Character constructor
        :param name: Name of the character
        :param health: Initial health of the character
        :param weapon: Weapon that the character is using
        :param special_power_1: First special power of the character
        :param special_power_2: Second special power of the character
        """
        # Set the name of the character
        self.name = name
        # Set the initial health of the character
        self.health = health
        # Set the weapon that the character is using
        self.weapon = weapon
        # Set the damage range of the weapon
        # The damage range is a tuple of two integers, where the first integer is the minimum damage
        # and the second integer is the maximum damage
        self.weapon_damage = self.set_weapon_damage()
        # Set the first special power of the character
        self.special_power_1 = special_power_1
        # Set the second special power of the character
        self.special_power_2 = special_power_2
        # Set the dodge chance of the character
        # The dodge chance is an integer between 0 and 100, where 0 is 0% and 100 is 100%
        self.dodge_chance = 50
        # Set a flag to indicate whether the character is frozen or not
        self.is_frozen = False
    def calculate_attack_speed(self, min_damage, max_damage):
        # Define a threshold for minimum and maximum damage
        min_threshold = 10
        max_threshold = 50
        # Calculate the damage range
        damage_range = max_damage - min_damage
        # Calculate the attack speed based on the damage range
        if damage_range < min_threshold:
            attack_speed = 4  # Fast attack speed for low damage weapons
        elif damage_range < max_threshold:
            attack_speed = 2  # Medium attack speed for medium damage weapons
        else:
            attack_speed = 1  # Slow attack speed for high damage weapons
        return attack_speed
    def set_weapon_damage(self):
        # Define a dictionary mapping weapon names to their respective damage ranges (min, max)
        # and their critical damage values.
        # The critical damage value is the maximum damage that a weapon can deal.
        # If the damage dealt by the weapon is equal to its critical damage value,
        # the weapon lands a critical hit.
        weapon_damage = {
            "Long Sword": ((7, 10),10),         # Long Sword deals damage between 7 and 10, and has a critical damage of 10
            "Katana": ((8, 11),11),             # Katana deals damage between 8 and 11, and has a critical damage of 11
            "Bow": ((5, 9),9),                 # Bow deals damage between 5 and 9, and has a critical damage of 9
            "Throwable Knife": ((3, 6),6),     # Throwable Knife deals damage between 3 and 6, and has a critical damage of 6
            "Axe": ((9, 12),12),                # Axe deals damage between 9 and 12, and has a critical damage of 12
            "Mace": ((8, 10),10),               # Mace deals damage between 8 and 10, and has a critical damage of 10
            "Spear": ((6, 10),10),              # Spear deals damage between 6 and 10, and has a critical damage of 10
            "Dagger": ((4, 7),7),              # Dagger deals damage between 4 and 7, and has a critical damage of 7
            "Staff": ((5, 8),8),               # Staff deals damage between 5 and 8, and has a critical damage of 8
            "TREBUCHET": ((15, 15),15)         # TREBUCHET deals a fixed damage of 15, and has a critical damage of 15
        }
        # Return the damage range for the character's weapon,
        min_damage, max_damage = weapon_damage.get(self.weapon, ((5, 8),8))[0]  # Get the damage range tuple
        attack_speed = self.calculate_attack_speed(min_damage, max_damage)
        hit_count = 0
        for _ in range(attack_speed):
            # Calculate the damage dealt
            damage = randint(min_damage, max_damage)
            # Increment the hit count
            hit_count += 1
        # Defaulting to a range of (5, 8) if the weapon is not found in the dictionary
        return ((min_damage, max_damage), attack_speed, hit_count)
    def weapon_critical_damage(self, damage_dealt, weapon_damage):
        """This function is used to determine whether a weapon lands a critical hit or not.
        The function takes two parameters: the damage dealt by the weapon and the weapon's damage range.
        If the damage dealt is equal to the critical damage listed in the weapon's damage range,
        the function prints a critical hit message to the console and returns True.
        Otherwise, it returns False."""
        # Unpack the weapon's damage range into the critical damage variable
        damage_range, attack_speed, hit_count = weapon_damage
        min_damage, max_damage = damage_range
        critical_damage = max_damage
        # Check if the damage dealt is equal to the critical damage
        if damage_dealt == critical_damage:
            # If the damage is critical, print a message to the console and return True
            print("\nWEAPON CRITICAL HIT!!\n")
            return True
        # If the damage is not critical, return False
        return False
    def dodge(self, attacker, defender):
        """This function is used to determine whether the character dodges an attack or not.
        The function works by generating a random number between 1 and 100 (inclusive).
        If the generated number is less than or equal to the character's dodge chance,
        the function returns True, indicating that the character dodged the attack.
        Otherwise, it returns False."""
        # Generate a random number between 1 and 100 (inclusive)
        roll = randint(1, 100)
        # Check if the generated number is less than or equal to the character's dodge chance
        if roll <= self.dodge_chance:
            # If the character dodged the attack, print a success message and return True
            print(f"\n{attacker.name} successfully dodged and skip {defender.name} next attack!")
            defender.is_frozen = True
            return True
        else:
            # If the character failed to dodge the attack, print a failure message and return False
            print(f"\nYou failed to dodge the enemy's attack!")
            return False
# Call the function on both the hero and enemy
    def info(self):
        # This method returns a string representation of the character's information.
        # It includes the character's current health, weapon, and their two special powers.
        # Create a formatted string that displays the character's health.
        health_info = f"Health: {self.health}\n"
        # Append the character's weapon to the information string.
        weapon_info = f"Weapon: {self.weapon}\n"
        # Append the character's first special power to the information string.
        special_power_1_info = f"Special Power 1: {self.special_power_1}\n"
        # Append the character's second special power to the information string.
        special_power_2_info = f"Special Power 2: {self.special_power_2}"
        # Return the full string containing all the information.
        return health_info + weapon_info + special_power_1_info + special_power_2_info
def apply_special_power(attacker, defender, power):
    """This function applies the special power of the attacker to the defender. 
    The special power is based on the element of the attacker's special power."""
    print(f"Applying special power: {power}")
    # If the special power is Fire, apply the Fire element's special abilities to the defender.
    if power == "Fire":
        # Fire is a special power that deals extra damage to the defender.
        # The amount of extra damage that the Fire power deals is 2.
        # However, if the defender's special power 1 or 2 is Ice or Earth,
        # the Fire power deals 4 extra damage to the defender instead.
        burn_damage = 2
        if defender.special_power_1 in ["Ice", "Earth"] or defender.special_power_2 in ["Ice", "Earth"]:
            # If the defender is weak to Fire, increase the damage dealt to 4.
            burn_damage = 4
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
        # Apply the damage to the defender's health.
        defender.health -= burn_damage
        # Ensure that the defender's health is not less than 0.
        defender.health = max(defender.health, 0)
        # Print a message indicating how much damage was dealt to the defender.
        print(f"{attacker.name}'s fire power burns {defender.name} for {burn_damage} extra damage!")
    # If the special power is Water, apply the Water element's special abilities to the defender.
    elif power == "Water":
        # Water is a special power that heals the attacker and deals damage to the defender.
        # The amount of health that the water power heals is 2.
        # The amount of damage that the water power deals to the defender is 2.
        # However, if the defender's special power 1 or 2 is Fire, Lightning, or Earth,
        # the water power deals 4 damage to the defender and heals the attacker for 4 health instead.
        heal = 2
        water_damage = 2
        if defender.special_power_1 in ["Fire", "Lightning", "Earth"] or defender.special_power_2 in ["Fire", "Lightning", "Earth"]:
            # If the defender's special power 1 or 2 is Fire, Lightning, or Earth,
            # increase the amount of damage that the water power deals to the defender to 4.
            # Also, increase the amount of health that the water power heals the attacker for to 4.
            heal = 4
            water_damage = 4
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
        # Apply the healing and damage to the attacker and defender.
        attacker.health += heal
        defender.health -= water_damage
        # Ensure that the defender's health does not go below 0.
        defender.health = max(defender.health, 0)
        # Print a message to the user about the water power's effects.
        print(f"{attacker.name}'s water power heals {attacker.name} for {heal} health and deals {water_damage} damage to {defender.name}!")
    elif power == "Ice":
        # Initialize the amount of extra damage that the ice power will deal
        freezing_damage = 2
        # Check if the defender's special power 1 or 2 is Water
        # If it is, the ice power makes the defender hypothermic and deals 2 extra damage
        # and has a 50% chance of freezing the defender
        if defender.special_power_1 == "Water" or defender.special_power_2 == "Water":
            # Apply the extra damage to the defender's health
            defender.health -= freezing_damage
            # Ensure that the defender's health does not go below 0
            defender.health = max(defender.health, 0)
            # Print a message to the user about the extra damage
            print(f"{attacker.name}'s ice power makes {defender.name} hypothermic for {freezing_damage} extra damage!")
            # Generate a random number between 1 and 2
            # If the number is 2, the defender is frozen
            if randint(1,2) == 2:
                # Set the defender's status to frozen
                defender.is_frozen = True
                # Print a message to the user about the defender being frozen
                print(f"{attacker.name}'s ice power freezes {defender.name}!")
        else:
            # If the defender's special power is not Water, the ice power just deals 2 extra damage
            # and has a 25% chance of freezing the defender
            defender.health -= freezing_damage
            # Ensure that the defender's health does not go below 0
            defender.health = max(defender.health, 0)
            # Print a message to the user about the extra damage
            print(f"{attacker.name}'s ice power makes {defender.name} hypothermic for {freezing_damage} extra damage!")
            # Generate a random number between 1 and 4
            # If the number is 2, the defender is frozen
            if randint(1,4) == 2:
                # Set the defender's status to frozen
                defender.is_frozen = True
                # Print a message to the user about the defender being frozen
                print(f"{attacker.name}'s ice power freezes {defender.name}!")
    elif power == "Lightning":
        # Initialize the base damage dealt by the lightning power
        burn_damage = 2
        # Check if the defender's special power 1 or 2 is Ice or Water
        # If it is, the lightning power deals 4 damage and has a 50% chance of shocking the defender
        if defender.special_power_1 in ["Ice", "Water"] or defender.special_power_2 in ["Ice", "Water"]:
            burn_damage = 4
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
            if randint(1, 2) == 2:
                # Set the defender's status to frozen if the defender is not already shocked
                defender.is_frozen = True
                print(f"{attacker.name}'s lightning power shocks {defender.name}!")
        else:
            # If the defender's special power 1 or 2 is not Ice or Water,
            # the lightning power deals 2 damage and has a 25% chance of shocking the defender
            if randint(1, 4) == 2:
                # Set the defender's status to shocked if the defender is not already shocked
                defender.is_frozen = True
                print(f"{attacker.name}'s lightning power shocks {defender.name}!")
        # Subtract the burn damage from the defender's health
        defender.health -= burn_damage
        # Ensure the defender's health does not drop below zero
        defender.health = max(defender.health, 0)
        # Print message indicating the damage dealt by the lightning power
        print(f"{attacker.name}'s lightning power creates burns {defender.name} for {burn_damage} extra damage!")
    elif power == "Earth":
        # Initialize the base damage dealt by the earth power
        earth_damage = 2
        # Subtract the earth damage from the defender's health
        defender.health -= earth_damage
        # Ensure the defender's health does not drop below zero
        defender.health = max(defender.health, 0)
        # Print message indicating the damage dealt by the earth power
        print(f"{attacker.name}'s earth power impales {defender.name} for {earth_damage} extra damage!")
        # Generate a random number between 1 and 4 to determine if a barrier is created
        if randint(1, 4) == 2:
            defender.is_frozen = True  # Set defender's status to frozen, indicating a barrier is created
            # Print message indicating a barrier is created
            print(f"{attacker.name}'s earth power creates barrier!")
            # Generate another random number between 1 and 2 to check for a critical hit
            if randint(1, 2) == 2:
                # Print message indicating a critical hit
                print("\nSPECIAL POWER CRITICAL HIT!!\n")
                defender.is_frozen = True  # Reinforce the defender's frozen status
                earth_damage += 4  # Increase the damage for critical hit
                # Subtract the additional critical hit damage from the defender's health
                defender.health -= earth_damage
                # Print message indicating the total damage dealt by the earth power with critical hit
                print(f"{attacker.name}'s earth power makes {defender.name} bounce for {earth_damage} extra damage!")
        # Wind deals 2 damage to the defender if the defender's special power 1 or 2 is not Fire or Lightning.
        # If the defender's special power 1 or 2 is Fire or Lightning, wind deals 4 damage.
    # If the attacker's special power is Wind, calculate the damage dealt based on the defender's special power.
    elif power == "Wind":
        # Initialize the base damage dealt by the wind power to 2.
        wind_damage = 2
        # Check if the defender's special power 1 or 2 is Fire or Lightning.
        if defender.special_power_1 in ["Fire", "Lightning"] or defender.special_power_2 in ["Fire", "Lightning"]:
            # If the defender's special power 1 or 2 is Fire or Lightning, increase the damage to 4.
            wind_damage = 4
            # Print message indicating a critical hit.
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
        # Subtract the wind damage from the defender's health.
        defender.health -= wind_damage
        # Ensure the defender's health does not drop below zero.
        defender.health = max(defender.health, 0)
        # Print message indicating the damage dealt by the wind power.
        print(f"{attacker.name}'s wind power blows {defender.name} for {wind_damage} extra damage!")
def main():
    """This function is the main entry point of the game.
    It initializes some of the game's variables and prints the game's intro."""
    # This variable keeps track of the player's level.
    level = 0
    # This variable keeps track of the additional health that the player has.
    additional_health = 0
    # This variable keeps track of the player's score.
    score = 0
    # This variable keeps track of whether the game should repeat or not.
    repetition = "yes"
    # Print the game's intro.
    print("Game created by Saridi and Nicander!!")
    sleep(4)
    print("FORCE OF NATURE!!")
    sleep(4)
    print("V.1.2.3")
    sleep(4)
    print("Don't forget to follow our Instagram account!!")
    sleep(4)
    # Print the URLs of the game creators' Instagram accounts.
    print("Saridi: https://www.instagram.com/s4r_m4l3z_404/")
    print("Nicander: https://www.instagram.com/nicander_arif/")
    sleep(4)
    # This loop will repeat until the user chooses to stop playing.
    while repetition == "yes":
        # Create a new hero and enemy for the current round.
        # The hero and enemy's stats will be randomly generated.
        hero = Character(
            name="Hero",
            health=randint(40, 50),  # The hero's health is randomly set between 40 and 50.
            weapon=choice(WEAPONS),  # The hero's weapon is randomly chosen from the list of weapons.
            special_power_1=choice(SPECIAL_POWERS),  # The hero's first special power is randomly chosen from the list of special powers.
            special_power_2=choice(SPECIAL_POWERS)  # The hero's second special power is randomly chosen from the list of special powers.
        )
        enemy = Character(
            name="Enemy",
            health=randint(40, 50),  # The enemy's health is randomly set between 40 and 50.
            weapon=choice(WEAPONS),  # The enemy's weapon is randomly chosen from the list of weapons.
            special_power_1=choice(SPECIAL_POWERS),  # The enemy's first special power is randomly chosen from the list of special powers.
            special_power_2=choice(SPECIAL_POWERS)  # The enemy's second special power is randomly chosen from the list of special powers.
        )
        # Ensure that the hero and enemy's special powers are not the same.
        while hero.special_power_1 == hero.special_power_2:
            hero.special_power_2 = choice(SPECIAL_POWERS)
        while enemy.special_power_1 == enemy.special_power_2:
            enemy.special_power_2 = choice(SPECIAL_POWERS)
        # Add the additional health to the hero's health.
        hero.health += additional_health
        # Print a message to the console indicating that a new enemy has approached.
        print("\nA new enemy approaches!")
        # Ask the user if they want to attack the enemy.
        declaration = input("Attack the enemy? (yes/no): ").lower()
        # Keep asking the user until they enter "yes" or "no".
        # Keep asking the user until they enter "yes" or "no".
        while declaration not in ["yes", "no"]:
            declaration = input("Attack the enemy? (yes/no): ").lower()
        # If the user wants to attack the enemy,
        if declaration == "yes":
            # Ensure that the hero and enemy's health are not negative.
            # This is a failsafe to prevent the game from crashing if the hero or enemy's health somehow becomes negative.
            if hero.health <= 0:
                hero.health = 0
            if enemy.health <= 0:
                enemy.health = 0
            # Print the hero and enemy's stats to the console.
            print("\nHero Stats:")
            print(hero.info())
            print("\nEnemy Stats:")
            print(enemy.info())
            # This while loop will keep running until either the hero or the enemy runs out of health.
            # Inside the loop, we'll first check if the hero is frozen.
            # If the hero is not frozen, we'll ask the user to choose an action.
            # The user can choose to either attack or dodge.
            # We'll keep asking the user for input until they enter either "attack" or "dodge".
            while hero.health > 0 and enemy.health > 0:
                if not hero.is_frozen:
                    # Ask the user to choose an action.
                    hero_action = input("Choose action: 'attack' or 'dodge': ").lower()
                    # Keep asking the user until they enter either "attack" or "dodge".
                    while hero_action not in ["attack", "dodge"]:
                        hero_action = input("Choose action: 'attack' or 'dodge': ").lower()
                    # If the user chooses to attack,
                    if hero_action == "attack":
                        # Ask the user which special power they want to use.
                        # The user can choose between the hero's first and second special powers.
                        # We'll keep asking the user for input until they enter either 1 or 2.
                        hero_special_power_choice = int(input(f"What special power do you want to use? {hero.special_power_1} or {hero.special_power_2}? (1/2): "))
                        while hero_special_power_choice not in [1,2]:
                            hero_special_power_choice = int(input(f"What special power do you want to use? {hero.special_power_1} or {hero.special_power_2}? (1/2): "))
                        # Get the name of the hero's weapon.
                        weapon_name = hero.weapon
                        # Generate a random amount of damage between the minimum and maximum damage of the hero's weapon.
                        hero_damage_range, hero_attack_speed, hero_hit_count = hero.set_weapon_damage()
                        hero_damage = random.randint(*hero_damage_range)
                        hero_damage += randint(hero.weapon_damage[0][0], hero.weapon_damage[0][1])                        
                        # Subtract the damage from the enemy's health.
                        enemy.health = max(enemy.health - hero_damage, 0)
                        # Print a message to the console indicating that the hero attacked the enemy.
                        sleep(SLEEP_DURATION)
                        print(f"\nYou attacked the enemy and dealt {hero_damage} damage using your {hero.weapon} ({hero_hit_count} hits)!")
                        # Check if the hero's attack was a critical hit.
                        hero.weapon_critical_damage(hero_damage, hero.weapon_damage)
                        # If the hero's attack was a critical hit,
                        # apply the special power to the enemy.
                        if hero_special_power_choice == 1:
                            # Apply the hero's first special power.
                            apply_special_power(hero, enemy, hero.special_power_1)
                        else:
                            # Apply the hero's second special power.
                            apply_special_power(hero, enemy, hero.special_power_2)
                    # Check if the hero's action is to dodge an attack
                    elif hero_action == "dodge":
                        # Call the dodge function on the hero object to determine if the dodge is successful
                        # If the hero successfully dodges, skip the rest of this iteration and start the next loop iteration
                        if hero.dodge(hero, enemy):
                            continue
                else:
                    # If the hero's dodge action fails,
                    # print a message to the console indicating that the hero's turn is skipped.
                    # This is because the hero is frozen for the current turn.
                    sleep(SLEEP_DURATION)
                    print(f"\nYou're turn is skipped!")
                    # Set the hero's frozen flag to False.
                    # This is so that the hero can take their turn again in the next loop iteration.
                    hero.is_frozen = False
                # Check if the enemy's health is less than or equal to 0
                if enemy.health <= 0:
                    # If the enemy's health is 0 or less, break out of the loop
                    # This indicates that the enemy has been defeated and the battle ends
                    break
                # If the enemy is not frozen, they can attack the hero.
                if not enemy.is_frozen:
                    # Generate a random amount of damage between the minimum and maximum damage of the enemy's weapon.
                    enemy_damage_range, enemy_attack_speed, enemy_hit_count = enemy.set_weapon_damage()
                    enemy_damage = random.randint(*enemy_damage_range)
                    enemy_damage += randint(enemy.weapon_damage[0][0], enemy.weapon_damage[0][1])
                    # Subtract the damage from the hero's health.
                    hero.health = max(hero.health - enemy_damage, 0)
                    # Get the name of the enemy's weapon.
                    enemy_weapon_name = enemy.weapon
                    # Check if the enemy's attack was a critical hit.
                    enemy.weapon_critical_damage(enemy_damage, enemy.weapon_damage)
                    # Print a message to the console indicating that the enemy attacked the hero.
                    sleep(SLEEP_DURATION)
                    print(f"\nThe enemy attacked and dealt {enemy_damage} damage using their {enemy.weapon} ({enemy_hit_count} hits)!")
                    # Randomly select which special power to use.
                    # The special power choice is either 1 or 2.
                    enemy_special_power_choice = randint(1, 2)
                    # Apply the special power based on the randomly selected choice.
                    if enemy_special_power_choice == 1:
                        # Apply the enemy's first special power.
                        apply_special_power(enemy, hero, enemy.special_power_1)
                    else:
                        # Apply the enemy's second special power.
                        apply_special_power(enemy, hero, enemy.special_power_2)
                else:
                    # If the enemy is unable to make an attack.
                    sleep(SLEEP_DURATION)
                    # Set the enemy's frozen flag to False.
                    # This is so that the enemy can attack again in the next loop iteration.
                    enemy.is_frozen = False
                sleep(SLEEP_DURATION)
                if hero.health <= 0:
                    hero.health = 0
                if enemy.health <= 0:
                    enemy.health = 0
                # Make sure that the hero's health and the enemy's health are not negative.
                # This is because health cannot be negative in the game.
                hero.health = max(hero.health, 0)
                enemy.health = max(enemy.health, 0)
                # Print the current health of both the hero and the enemy.
                # This is so that the user can see how much health the hero and the enemy have.
                print(f"\nHero Health: {hero.health}")
                print(f"Enemy Health: {enemy.health}")
            # If the hero's health is greater than 0, then the hero has defeated the enemy.
            if hero.health > 0:
                # Print a message to the console indicating that the hero has defeated the enemy.
                print("\nYou defeated the enemy!")
                score += 1
                # Increase the hero's score by 1.
                level += 1
                # Increase the hero's additional health by 1.
                additional_health += 1
                # Make sure that the hero's health and the enemy's health are not negative
                if hero.health <= 0:
                    hero.health = 0
                if enemy.health <= 0:
                    enemy.health = 0
                # Print the hero's level, health, and the enemy's health.
                # This is so that the user can see how much health the hero and the enemy have.
                print(f"\nHero Level: {level}")
                print(f"Hero Health: {hero.health}")
                print(f"Enemy Health: {enemy.health}")
            # If the hero's health is 0 or less, then the hero has been defeated by the enemy.
            else:
                # Print a message to the console indicating that the hero has been defeated by the enemy.
                print("\nYou have been defeated by the enemy!")
                # Break out of the loop.
                break
        else:
            # If hero's action is "no" the enemy has escaped.
            # Print a message to the console indicating that the enemy has escaped.
            print("\nYou let the enemy escape!")
        # Ask the user if they want to restart the game.
        # The user can enter either "yes" or "no".
        repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()
        # Keep asking the user for input until they enter either "yes" or "no".
        while repetition not in ["yes", "no"]:
            # Ask the user for input again.
            repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()
    # Print a message to the console indicating that the game is over.
    print("\nGame Over!\n")
    sleep(4)
    # Print the hero's last level to the console.
    print(f"Hero last Level: {level}")
    sleep(4)
    # Print the number of enemies that the hero has defeated.
    print(f"Enemies Defeated: {score}\n")
    sleep(4)
    # Print a message to the console thanking the user for playing.
    print("Thanks for playing!")
# If the script is being run directly (i.e. not being imported), call the main function
if __name__ == "__main__":
    main()
