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
SPECIAL_POWERS = ["Lv 0 Fire", "Lv 0 Water", "Lv 1 Ice", "Lv 1 Lightning", "Lv 1 Earth", "Lv 0 Wind", "Lv 2 Metal", "Lv 2 Sound", "Lv 2 Magma"]
weapon_levels = {weapon: 0 for weapon in WEAPONS}
weapon_additional_damage = {weapon: 0 for weapon in WEAPONS}
# The amount of time to sleep between each output in the game
SLEEP_DURATION = 2
class Character:
    """This class represents a character in the game.
    Characters have a name, health, a weapon, a decision related to weapon upgrades,
    and two special powers. The character's weapon damage is set based on the chosen weapon.
    The character also has a base chance of dodging an attack (percentage) and a flag
    indicating whether the character is frozen (unable to move)."""
    def __init__(self, name, health, weapon, upgrade_decision, special_power_1, special_power_2):
        """This is the constructor for the Character class.
        It takes in the character's name, health, weapon, upgrade decision, and two special powers.
        The character's weapon damage is set based on the chosen weapon.
        The character also has a base chance of dodging an attack (percentage) and a flag
        indicating whether the character is frozen (unable to move)."""
        # Initialize the character's name
        self.name = name
        # Set the initial health of the character
        self.health = health
        # Assign the weapon chosen for the character
        self.weapon = weapon
        # List of all available weapons in the game
        self.weapons = WEAPONS
        # Decision related to weapon upgrades
        self.upgrade_decision = upgrade_decision
        self.score = 0
        self.LIGHTENERGY_locker = False
        # Calculate and set the weapon damage based on the chosen weapon
        self.weapon_damage = self.set_weapon_damage()
        # Assign the first special power to the character
        self.special_power_1 = special_power_1
        # Assign the second special power to the character
        self.special_power_2 = special_power_2
        # Set the base chance of dodging an attack (percentage)
        self.dodge_chance = 50
        # Flag indicating whether the character is frozen (unable to move)
        self.is_frozen = False
    def calculate_attack_speed(self, min_damage, max_damage):
        """This function calculates the attack speed of the character based on the damage range of their weapon.
        The attack speed is an integer value that indicates how many times the character can attack in a single turn.
        The value is determined by the damage range of the character's weapon, as follows:
        - If the damage range is less than 10, the attack speed is 4.
        - If the damage range is between 10 and 50 (inclusive), the attack speed is 2.
        - If the damage range is greater than 50, the attack speed is 1."""
        min_threshold = 10
        max_threshold = 50
        # Calculate the damage range
        damage_range = max_damage - min_damage
        if damage_range < min_threshold:
            # If the damage range is less than 10, the attack speed is 4
            attack_speed = 4
        elif damage_range < max_threshold:
            # If the damage range is between 10 and 50 (inclusive), the attack speed is 2
            attack_speed = 2
        else:
            # If the damage range is greater than 50, the attack speed is 1
            attack_speed = 1
        return attack_speed
    def set_weapon_damage(self):
        # This function sets the damage range of the weapon the character is holding.
        # The damage range is a tuple of two integers, where the first integer is the minimum damage
        # that the weapon can deal, and the second integer is the maximum damage that the weapon can deal.
        # The damage range is used to determine the attack speed of the character.
        # The attack speed is the number of times the character can attack in a single turn.
        # The attack speed is determined by the damage range of the weapon, as follows:
        # - If the damage range is less than 10, the attack speed is 4.
        # - If the damage range is between 10 and 50 (inclusive), the attack speed is 2.
        # - If the damage range is greater than 50, the attack speed is 1.
        # Additionally, the function adds the weapon's additional damage to the damage range.
        # The weapon's additional damage is a dictionary that maps the name of the weapon to the additional damage.
        # The additional damage is added to the minimum and maximum damage values of the damage range.
        weapon_damage = {
            # The damage range for each weapon is specified as a tuple of two integers.
            # The first integer is the minimum damage that the weapon can deal, and the second integer is the maximum damage that the weapon can deal.
            "Long Sword": (7, 10),
            "Katana": (8, 11),
            "Bow": (5, 9),
            "Throwable Knife": (3, 6),
            "Axe": (9, 12),
            "Mace": (8, 10),
            "Spear": (6, 10),
            "Dagger": (4, 7),
            "Staff": (5, 8),
            "TREBUCHET": (7,13)
        }
        min_damage, max_damage = weapon_damage.get(self.weapon, (5, 8))
        # Add the weapon's additional damage to the damage range.
        min_damage += weapon_additional_damage[self.weapon]
        max_damage += weapon_additional_damage[self.weapon]
        # Calculate the attack speed based on the damage range.
        attack_speed = self.calculate_attack_speed(min_damage, max_damage)
        # Set the hit count to the attack speed.
        hit_count = attack_speed
        # Return the damage range, attack speed, and hit count as a tuple.
        return ((min_damage, max_damage), attack_speed, hit_count)
    def upgrade_weapon(self):
        """Upgrade the character's weapon by allowing them to choose a weapon
        from the list of available weapons. If the character chooses a valid
        weapon, the weapon's level is increased by 1 and its additional damage
        is increased by 3."""
        print("\nWeapons available for upgrade:")
        # Print out the list of available weapons
        for weapon in WEAPONS:
            print(f"- {weapon}")
        # Ask the user to enter the name of the weapon they want to upgrade
        upgrade_weapon_name = input("Enter the name of the weapon you want to upgrade: ").upper()
        # Check if the user entered a valid weapon
        while upgrade_weapon_name not in [weapon.upper() for weapon in WEAPONS]:
            print("Weapon INVALID")
            # Ask the user to re-enter the name of the weapon they want to upgrade
            upgrade_weapon_name = input("Enter the name of the weapon you want to upgrade: ").upper()
        # Print out a message indicating that the weapon is being upgraded
        for weapon in WEAPONS:
            if weapon.upper() == upgrade_weapon_name:
                original_weapon_name = weapon
                break
        print(f"Upgrading {original_weapon_name}...")
        sleep(2)
        # Increase the weapon's level by 1
        weapon_levels[original_weapon_name] += 1
        # Increase the weapon's additional damage by 3
        weapon_additional_damage[original_weapon_name] += 3
        # Print out a message indicating that the weapon has been upgraded
        print(f"Upgraded!! Level {weapon_levels[original_weapon_name]} {original_weapon_name} now deals {weapon_additional_damage[original_weapon_name]} additional damage")
        # Set the upgrade decision to "Not level 5 yet"
        upgrade_decisions = "Not level 5 yet"
        # Return the upgrade decision
        return upgrade_decisions
    def weapon_critical_damage(self, damage_dealt, weapon_damage):
        """Checks if the character's attack with their weapon resulted in a critical hit.
        A critical hit is when the attack deals the maximum possible damage."""
        # Unpack the attack speed, hit count, and damage range from the weapon damage tuple
        damage_range, attack_speed, hit_count = weapon_damage
        # Unpack the minimum and maximum damage from the damage range tuple
        min_damage, max_damage = damage_range
        # Check if the damage dealt is equal to the maximum possible damage
        if damage_dealt == max_damage:
            # If it is, print a message indicating that the attack was a critical hit
            print("\nWEAPON CRITICAL HIT!!\n")
            # Return True to indicate that the attack was a critical hit
            return True
        # If the attack was not a critical hit, return False
        return False
    def dodge(self, attacker, defender):
        """This function determines if the attacker successfully dodges the defender's attack.
        The dodge chance is based on the attacker's dodge chance attribute.
        If the attacker successfully dodges, the defender is frozen and cannot attack on their next turn."""
        # Generate a random number between 1 and 100
        roll = randint(1, 100)
        # If the random number is less than or equal to the attacker's dodge chance,
        # the attacker successfully dodges the attack.
        if roll <= self.dodge_chance:
            # Print a message indicating that the attacker successfully dodged the attack.
            print(f"\n{attacker.name} successfully dodged and skips {defender.name}'s next attack!")
            # Set the defender's frozen status to True, indicating that they cannot attack on their next turn.
            defender.is_frozen = True
            # Return True to indicate that the attacker successfully dodged the attack.
            return True
        else:
            # Print a message indicating that the attacker failed to dodge the attack.
            print(f"\nYou failed to dodge the enemy's attack!")
            defender.is_frozen = False
            # Return False to indicate that the attacker failed to dodge the attack.
            return False
    def info(self):
        # Create a string containing the character's health information
        health_info = f"Health: {self.health}\n"
        # Create a string containing the character's weapon information
        weapon_info = f"Weapon: {self.weapon}\n"
        # Create a string containing the character's first special power information
        special_power_1_info = f"Special Power 1: {self.special_power_1}\n"
        # Create a string containing the character's second special power information
        special_power_2_info = f"Special Power 2: {self.special_power_2}\n"
        # Concatenate and return all the information strings
        return health_info + weapon_info + special_power_1_info + special_power_2_info
def apply_special_power(attacker, defender, power):
    """This function applies the special power of the attacker to the defender. 
    The special power is based on the element of the attacker's special power."""
    print(f"Applying special power: {power}")
    # If the special power is Fire, apply the Fire element's special abilities to the defender.
    if power == "Lv 0 Fire":
        # Fire is a special power that deals extra damage to the defender.
        # The amount of extra damage that the Fire power deals is 2.
        # However, if the defender's special power 1 or 2 is Ice or Earth,
        # the Fire power deals 4 extra damage to the defender instead.
        burn_damage = 2
        checker = False
        if power == "Lv 0 Fire":
            # Fire is a special power that deals extra damage to the defender.
            # The amount of extra damage that the Fire power deals is 2.
            # However, if the defender's special power 1 or 2 is Ice or Earth,
            # the Fire power deals 4 extra damage to the defender instead.
            burn_damage = 2
            if defender.special_power_1 in ["Lv 1 Ice", "Lv 1 Earth"] or defender.special_power_2 in ["Lv 1 Ice", "Lv 1 Earth"]:
                # If the defender is weak to Fire, increase the damage dealt to 4.
                burn_damage = 4
                print("\nSPECIAL POWER CRITICAL HIT!!\n")
        # Ensure that the defender's health is not less than 0.
        defender.health = max(defender.health, 0)
        # Print a message indicating how much damage was dealt to the defender.
        print(f"{attacker.name}'s fire power burns {defender.name} for {burn_damage} extra damage!")
    # If the special power is Water, apply the Water element's special abilities to the defender.
    elif power == "Lv 0 Water":
        # Water is a special power that heals the attacker and deals damage to the defender.
        # The amount of health that the water power heals is 2.
        # The amount of damage that the water power deals to the defender is 2.
        # However, if the defender's special power 1 or 2 is Fire, Lightning, or Earth,
        # the water power deals 4 damage to the defender and heals the attacker for 4 health instead.
        heal = 2
        water_damage = 2
        if defender.special_power_1 in ["Lv 0 Fire", "Lv 1 Lightning", "Lv 1 Earth", "Lv 2 Metal"] or defender.special_power_2 in ["Lv 0 Fire", "Lv 1 Lightning", "Lv 1 Earth", "Lv 2 Metal"]:
            # If the defender is weak to Water, increase the damage dealt to 4.
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
    elif power == "Lv 1 Ice":
        # Initialize the amount of extra damage that the ice power will deal
        freezing_damage = 2
        # Check if the defender's special power 1 or 2 is Water
        # If it is, the ice power makes the defender hypothermic and deals 2 extra damage
        # and has a 50% chance of freezing the defender
        if defender.special_power_1 == "Lv 0 Water" or defender.special_power_2 == "Lv 0 Water":
            freezing_damage = 4
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
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
    elif power == "Lv 1 Lightning":
        # Initialize the base damage dealt by the lightning power
        burn_damage = 2
        # Check if the defender's special power 1 or 2 is Ice or Water
        # If it is, the lightning power deals 4 damage and has a 50% chance of shocking the defender
        if defender.special_power_1 in ["Lv 1 Ice", "Lv 0 Water", "Lv 2 Metal"] or defender.special_power_2 in ["Lv 1 Ice", "Lv 0 Water", "Lv 2 Metal"]:
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
        print(f"{attacker.name}'s lightning power burns {defender.name} for {burn_damage} extra damage!")
    elif power == "Lv 1 Earth":
        # Initialize the base damage dealt by the earth power
        earth_damage = 2
        # Check if the defender's special power 1 and 2 is Sound
        if defender.special_power_1 == "Lv 2 Sound" and defender.special_power_2 == "Lv 2 Sound":
            # If it is, the earth power deals double damage and impales the defender
            earth_damage = 4
            # Print message indicating a critical hit
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
            # Subtract the earth damage from the defender's health
            defender.health -= earth_damage
            # Ensure the defender's health does not drop below zero
            defender.health = max(defender.health, 0)
            # Print message indicating the damage dealt by the earth power
            print(f"{attacker.name}'s earth power impales {defender.name} for {earth_damage} extra damage!")
            if randint(1, 2) == 1:
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
        else:
            defender.health -= earth_damage
            defender.health = max(defender.health, 0)
            print(f"{attacker.name}'s earth power impales {defender.name} for {earth_damage} extra damage!")
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
    elif power == "Lv 0 Wind":
        # Initialize the base damage dealt by the wind power to 2.
        wind_damage = 2
        # Check if the defender's special power 1 or 2 is Fire or Lightning.
        if defender.special_power_1 in ["Lv 0 Fire", "Lv 1 Lightning"] or defender.special_power_2 in ["Lv 0 Fire", "Lv 1 Lightning"]:
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
    # If the attacker's special power is "Metal", calculate the damage dealt.
    elif power == "Lv 2 Metal":
        # Initialize the base damage dealt by the metal power to 2.
        puncture_damage = 2
        # Check if the defender's special power 1 or 2 is Fire, Ice, or Earth.
        # If it is, increase the damage to 5.
        if defender.special_power_1 in ["Lv 0 Fire","Lv 1 Ice","Lv 1 Earth"] or defender.special_power_2 in ["Lv 0 Fire","Lv 1 Ice","Lv 1 Earth"]:
            # Increase the damage to 5.
            puncture_damage = 5
            # Subtract the increased damage from the defender's health.
            defender.health -= puncture_damage
            # Print a message indicating a critical hit.
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
            # Print a message indicating the total damage dealt by the metal power with critical hit.
            print(f"{attacker.name}'s metal power stab {defender.name} for {puncture_damage} extra damage!")
            # There is a 50% chance that the defender will be frozen.
            if randint(1,2) == 1:
                # Set the defender's frozen status to True.
                defender.is_frozen = True
                # Print a message indicating that the defender is frozen.
                print(f"{attacker.name}'s metal power creates barrier of metal!")
                # There is a 25% chance that the defender will bleed, causing the damage to be doubled.
                if randint(1,4) == 2:
                    # Double the damage.
                    puncture_damage *= 2
                    # Subtract the doubled damage from the defender's health.
                    defender.health -= puncture_damage
                    # Print a message indicating a critical hit.
                    print("\nSPECIAL POWER CRITICAL HIT!!\n")
                    # Print a message indicating the total damage dealt by the metal power with critical hit and bleeding.
                    print(f"{attacker.name}'s metal power have been twice the base damage because {defender.name} is bleeding!")
        else:
            # Subtract the base damage from the defender's health.
            defender.health -= puncture_damage
            # Print a message indicating the damage dealt by the metal power.
            print(f"{attacker.name}'s metal power stab {defender.name} for {puncture_damage} extra damage!")
            # There is a 25% chance that the defender will be frozen.
            if randint(1,4) == 2:
                # Set the defender's frozen status to True.
                defender.is_frozen = True
                # Print a message indicating that the defender is frozen.
                print(f"{attacker.name}'s metal power creates barrier!")
                # There is a 25% chance that the defender will bleed, causing the damage to be doubled.
                if randint(1,4) == 2:
                    # Double the damage.
                    puncture_damage *= 2
                    # Subtract the doubled damage from the defender's health.
                    defender.health -= puncture_damage
                    # Print a message indicating a critical hit.
                    print("\nSPECIAL POWER CRITICAL HIT!!\n")
                    # Print a message indicating the total damage dealt by the metal power with critical hit and bleeding.
                    print(f"{attacker.name}'s metal power twice the base damage because {defender.name} is bleeding!")
    # If the attacker's special power is "Sound", calculate the damage dealt.
    elif power == "Lv 2 Sound":
        # Initialize the base damage dealt by the sound power to 2.
        sound_damage = 2
        # Check if the defender's special power 1 or 2 is Water.
        if defender.special_power_1 == "Lv 0 Water" or defender.special_power_2 == "Lv 0 Water":
            # If the defender's special power 1 or 2 is Water, increase the damage to 4.
            sound_damage = 4
            # Print a message indicating a critical hit.
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
        # Subtract the sound damage from the defender's health.
        defender.health -= sound_damage
        # Print a message indicating the damage dealt by the sound power.
        print(f"{attacker.name}'s sound power make {defender.name}'s ears hurts for {sound_damage} extra damage!")
        # Roll a random number between 1 and 3 (inclusive) to determine if the defender is frozen.
        if randint(1,2) == 1:
            # If the random number is 2, set the defender's frozen status to True.
            defender.is_frozen = True
            # Print a message indicating that the defender is frozen.
            print(f"{attacker.name}'s sound power creates beautiful music sound and make {defender.name} is dancing like in dancing floor!")
    # If the attacker's special power is "Magma", calculate the damage dealt.
    elif power == "Lv 2 Magma":
        # Initialize the base damage dealt by the magma power to 4.
        burn_damage = 4
        # Check if the defender's special power 1 or 2 is Water, Ice, Earth, or Metal.
        # If it is, increase the damage to 6.
        if defender.special_power_1 in ["Lv 0 Water","Lv 1 Ice","Lv 1 Earth","Lv 2 Metal"] or defender.special_power_2 in ["Lv 0 Water","Lv 1 Ice","Lv 1 Earth","Lv 2 Metal"]:
            # Increase the damage to 6.
            burn_damage += 2
            # Subtract the increased damage from the defender's health.
            defender.health -= burn_damage
            # Print a message indicating a critical hit.
            print("\nSPECIAL POWER CRITICAL HIT!!\n")
            # Print a message indicating the total damage dealt by the magma power with critical hit.
            print(f"{attacker.name}'s magma power makes {defender.name}'s body melting for {burn_damage} extra damage!")
            # There is a 50% chance that the defender will be frozen.
            if randint(1,2) == 1:
                # Set the defender's frozen status to True.
                defender.is_frozen = True
                # Print a message indicating that the defender is frozen.
                print(f"{attacker.name}'s magma power creates barrier of obsidian!")
        else:
            # Subtract the base damage from the defender's health.
            defender.health -= burn_damage
            # Print a message indicating the damage dealt by the magma power.
            print(f"{attacker.name}'s magma power makes {defender.name}'s body melting for {burn_damage} extra damage!")
            # There is a 25% chance that the defender will be frozen.
            if randint(1,4) == 2:
                # Set the defender's frozen status to True.
                defender.is_frozen = True
                # Print a message indicating that the defender is frozen.
                print(f"{attacker.name}'s magma power creates barrier of obsidian!")
    elif power == "??? DARK ENERGY":
        if defender.special_power_1 == "??? LIGHT ENERGY":
            DARKENERGY_damage = 8
            defender.health -= DARKENERGY_damage
            print("Hero's DARK ENERGY is weak against enemy's LIGHT ENERGY!")
            if randint(1, 3) == 2:
                print("\nDARK MOVE HAVE BEEN MOVED!!\n")
                attacker.health += attacker.health * 0.5
                attacker.health += attacker.health * 0.3
                print("Hero's health is increased by 50% and healed by 30%!")
                if randint(1, 4) == 2:
                    DARKENERGY_damage = 66
                    defender.health -= DARKENERGY_damage
                    print("\nSPECIAL POWER CRITICAL HIT!!\n")
                    print("Hero's DARK ENERGY is slamming the enemy!")
                if randint(1, 3) == 2:
                    defender.is_frozen == True
                    print("\nHERO's DARK ENERGY SHIELD HAS BEEN ACTIVATED\n")
                    if randint(1, 2) == 1:
                        enemy.is_frozen == False
                        print("\nHERO's DARK ENERGY SHIELD HAS BEEN DESTROY BY ENEMY\n")
        else:
            DARKENERGY_damage = 16
            defender.health -= DARKENERGY_damage
            print("Hero's DARK ENERGY is powerful against enemy!")
            if randint(1, 2) == 1:
                print("\nDARK MOVE HAVE BEEN MOVED!!\n")
                attacker.health += attacker.health * 0.5
                attacker.health += attacker.health * 0.3
                print("Hero's health is increased by 50% and healed by 30%!")
                if randint(1, 3) == 2:
                    DARKENERGY_damage = 66
                    defender.health -= DARKENERGY_damage
                    print("\nSPECIAL POWER CRITICAL HIT!!\n")
                    print("Hero's DARK ENERGY is slamming the enemy!")
            if randint(1,3) == 2:
                defender.is_frozen ==  True
                print("HERO's DARK ENERGY SHIELD HAS BEEN ACTIVATED")
    elif power == "??? LIGHT ENERGY":
        LIGHTENERGY_damage = 16
        if attacker.health <= 50 and attacker.health >= 30:
            LIGHTENERGY_damage *= 2
            defender.health -= LIGHTENERGY_damage
            print("Enemy entering berserk mode!")
            if randint(1, 2) == 1:
                print("\nHOLY MOVE HAVE BEEN MOVED!!\n")
                LIGHTENERGY_damage += LIGHTENERGY_damage / 10  # increase damage by 10%
                defender.health -= LIGHTENERGY_damage
                print("Enemy's LIGHT ENERGY damage is increased by 10%!")
                if randint(1, 3) == 2:
                    defender.health *= 0.65  # Geometrically decrease health by 35%
                    print("\nSPECIAL POWER CRITICAL HIT!!\n")
                    print("Enemy's LIGHT ENERGY is burning the hero's health by a quarter!")
                if randint(1, 3) == 2:
                    DARKENERGY_damage = 8
                    defender.is_frozen == True
                    print("\nENEMY's LIGHT ENERGY SHIELD HAS BEEN ACTIVATED")
                    print("HERO's ATTACK HAS BEEN ABSORBED\n")
                    LIGHTENERGY_damage += DARKENERGY_damage
                    defender.health -= LIGHTENERGY_damage
        elif attacker.health < 30:
            LIGHTENERGY_damage *= 3
            defender.health -= LIGHTENERGY_damage
            print("Enemy entering LAST STAND MODE!")
            print("\nHOLY MOVE HAVE BEEN MOVED!!\n")
            LIGHTENERGY_damage += LIGHTENERGY_damage / 10  # increase damage by 10%
            defender.health -= LIGHTENERGY_damage
            print("Enemy's LIGHT ENERGY damage is increased by 10%!")
            if randint(1, 2) == 1:
                defender.health *= 0.65  # Geometrically decrease health by 35%
                print("\nSPECIAL POWER CRITICAL HIT!!\n")
                print("Enemy's LIGHT ENERGY is burning the hero's health by a quarter!")
            if randint(1, 3) == 2:
                    DARKENERGY_damage = 8
                    defender.is_frozen == True
                    print("\nENEMY's LIGHT ENERGY SHIELD HAS BEEN ACTIVATED")
                    print("HERO's ATTACK HAS BEEN ABSORBED\n")
                    LIGHTENERGY_damage += DARKENERGY_damage
                    defender.health -= LIGHTENERGY_damage
        else:
            defender.health -= LIGHTENERGY_damage
            print("Enemy's LIGHT ENERGY is more powerful against hero's DARK ENERGY!")
            if randint(1, 2) == 1:
                print("\nHOLY MOVE HAVE BEEN MOVED!!\n")
                LIGHTENERGY_damage += LIGHTENERGY_damage / 10  # increase damage by 10%
                defender.health -= LIGHTENERGY_damage
                print("Enemy's LIGHT ENERGY damage is increased by 10%!")
                if randint(1, 3) == 2:
                    defender.health *= 0.65  # Geometrically decrease health by 35%
                    print("\nSPECIAL POWER CRITICAL HIT!!\n")
                    print("Enemy's LIGHT ENERGY is burning the hero's health by a quarter!")
                if randint(1, 3) == 2:
                    defender.is_frozen == True
                    print("\nENEMY's LIGHT ENERGY SHIELD HAS BEEN ACTIVATED")
                    print("HERO's ATTACK HAS BEEN ABSORBED\n")
                    DARKENERGY_damage = 8
                    LIGHTENERGY_damage += DARKENERGY_damage
                    defender.health -= LIGHTENERGY_damage
def main():
    """This function is the main entry point of the game.
    It initializes some of the game's variables and prints the game's intro."""
    # This variable keeps track of the player's level.
    level = 0
    # This variable keeps track of the additional health that the player has.
    additional_health = 0
    # This variable keeps track of the player's score.
    hero_score = 0
    hero_class = "Hero"
    upgrade_decisions = "Not level 5 yet"
    # This variable keeps track of whether the game should repeat or not.
    repetition = "yes"
    # Print the game's intro.
    second_life = 1
    print("Game created by Saridi and Nicander!!")
    sleep(4)
    print("\nFORCE OF NATURE!!")
    sleep(4)
    print("V.1.3.1")
    sleep(4)
    print("\nDon't forget to follow our Instagram account!!")
    sleep(4)
    # Print the URLs of the game creators' Instagram accounts.
    print("Saridi: https://www.instagram.com/s4r_m4l3z_404/")
    print("Nicander: https://www.instagram.com/nicander_arif/")
    # This loop will repeat until the user chooses to stop playing.
    while repetition == "yes":
        # Create a new hero and enemy for the current round.
        # The hero and enemy's stats will be randomly generated.
        # Create a new hero character with the specified attributes
        hero = Character(
            name="Hero",  # Set name of the character to "Hero"
            health=randint(80, 100),  # Randomly assign the hero's health between 80 and 100
            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
            upgrade_decision=upgrade_decisions,  # Set the upgrade decision for the hero's weapon
            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
        )
        print("\nLOADING\n")
        sleep(4)
        for i in range(2):
            while hero.special_power_1 == hero.special_power_2:
                if hero.special_power_1 == "Lv 1 Ice" or hero.special_power_2 == "Lv 1 Ice":
                    if randint(1, 3) == 1:
                        if hero.special_power_1 == "Lv 1 Ice":
                            hero.special_power_1 = "Lv 1 Ice"
                        elif hero.special_power_2 == "Lv 1 Ice":
                            hero.special_power_2 = "Lv 1 Ice"
                    else:
                        hero = Character(
                            name="Hero",
                            health=randint(80, 100),
                            weapon=choice(WEAPONS),
                            upgrade_decision="Not level 5 yet",
                            special_power_1=choice(SPECIAL_POWERS),
                            special_power_2=choice(SPECIAL_POWERS)
                        )
                if hero.special_power_1 == "Lv 1 Lightning" or hero.special_power_2 == "Lv 1 Lightning":
                    if randint(1, 3) == 1:
                        if hero.special_power_1 == "Lv 1 Lightning":
                            hero.special_power_1 = "Lv 1 Lightning"
                        elif hero.special_power_2 == "Lv 1 Lightning":
                            hero.special_power_2 = "Lv 1 Lightning"
                    else:
                        hero = Character(
                            name="Hero",
                            health=randint(80, 100),
                            weapon=choice(WEAPONS),
                            upgrade_decision="Not level 5 yet",
                            special_power_1=choice(SPECIAL_POWERS),
                            special_power_2=choice(SPECIAL_POWERS)
                        )
                if hero.special_power_1 == "Lv 1 Earth" or hero.special_power_2 == "Lv 1 Earth":
                    if randint(1, 3) == 1:
                        if hero.special_power_1 == "Lv 1 Earth":
                            hero.special_power_1 = "Lv 1 Earth"
                        elif hero.special_power_2 == "Lv 1 Earth":
                            hero.special_power_2 = "Lv 1 Earth"
                    else:
                        hero = Character(
                            name="Hero",
                            health=randint(80, 100),
                            weapon=choice(WEAPONS),
                            upgrade_decision="Not level 5 yet",
                            special_power_1=choice(SPECIAL_POWERS),
                            special_power_2=choice(SPECIAL_POWERS)
                        )
                if hero.special_power_1 == "Lv 2 Metal" or hero.special_power_2 == "Lv 2 Metal":
                    if randint(1, 4) == 2:
                        if hero.special_power_1 == "Lv 2 Metal":
                            hero.special_power_1 = "Lv 2 Metal"
                        elif hero.special_power_2 == "Lv 2 Metal":
                            hero.special_power_2 = "Lv 2 Metal"
                    else:
                        hero = Character(
                            name="Hero",
                            health=randint(80, 100),
                            weapon=choice(WEAPONS),
                            upgrade_decision="Not level 5 yet",
                            special_power_1=choice(SPECIAL_POWERS),
                            special_power_2=choice(SPECIAL_POWERS)
                        )
                if hero.special_power_1 == "Lv 2 Sound" or hero.special_power_2 == "Lv 2 Sound":
                    if randint(1, 4) == 2:
                        if hero.special_power_1 == "Lv 2 Sound":
                            hero.special_power_1 = "Lv 2 Sound"
                        elif hero.special_power_2 == "Lv 2 Sound":
                            hero.special_power_2 = "Lv 2 Sound"
                    else:
                        hero = Character(
                            name="Hero",
                            health=randint(80, 100),
                            weapon=choice(WEAPONS),
                            upgrade_decision="Not level 5 yet",
                            special_power_1=choice(SPECIAL_POWERS),
                            special_power_2=choice(SPECIAL_POWERS)
                        )
                if hero.special_power_1 == "Lv 2 Magma" or hero.special_power_2 == "Lv 2 Magma":
                    if randint(1, 4) == 2:
                        if hero.special_power_1 == "Lv 2 Magma":
                            hero.special_power_1 = "Lv 2 Magma"
                        elif hero.special_power_2 == "Lv 2 Magma":
                            hero.special_power_2 = "Lv 2 Magma"
                    else:
                        hero = Character(
                            name="Hero",
                            health=randint(80, 100),
                            weapon=choice(WEAPONS),
                            upgrade_decision="Not level 5 yet",
                            special_power_1=choice(SPECIAL_POWERS),
                            special_power_2=choice(SPECIAL_POWERS)
                        )
            print(".\n")
            sleep(2)
        if level >= 15:
            if level == 30:
                causes = "accept"
            if level > 30:
                causes = "don't accepted"
            while causes == "accept":
                print("\nA portal just appear front the Hero...\n")
                sleep(4)
                print("DEMON: Hey ya! I think I see you are very strong!!")
                sleep(4)
                print("DEMON: I think you will like this things and really need this power to becoming even more powerful!!")
                sleep(4)
                print("DEMON: Do you want to accept and being curse to get this powerful power?")
                hero_decision = input("DEMON: If you accept this power you are agree being curse and sacrifice your main or Special Power 1 forever until your soul are flying out from your body! (yes/no)").lower()
                while hero_decision not in ["yes","no"]:
                    hero_decision = input("DEMON: If you accept this power you are agree being curse and sacrifice your main or Special Power 1 forever until your soul are flying out from your body! (yes/no)").lower()
                if hero_decision == "yes":
                    print("DEMON: Here you go!!")
                    sleep(4)
                    print("ADDED ??? DARK ENERGY PERMANENTLY IN SPECIAL POWER 1!!")
                    # Create a new enemy character with the specified attributes
                    hero = Character(
                        name="Hero",  # Set name of the character to "Enemy"
                        health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                        weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                        upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                        special_power_1="??? DARK ENERGY",  # Randomly select the first special power
                        special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                    )
                    causes = "don't accepted"
                else:
                    print("DEMON: Well...")
                    sleep(4)
                    print("DEMON: Your decision is what you receiving in the future...")
                    causes = "don't accept"
                    # Create a new enemy character with the specified attributes
                    hero = Character(
                        name="Hero",  # Set name of the character to "Enemy"
                        health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                        weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                        upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                        special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                        special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                    )
                    causes = "don't accepted"
            if level > 15:
                if hero_decision == "yes":
                    # Create a new enemy character with the specified attributes
                    hero = Character(
                        name="Hero",  # Set name of the character to "Enemy"
                        health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                        weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                        upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                        special_power_1="??? DARK ENERGY",  # Randomly select the first special power
                        special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                    )
        enemy = Character(
            name="Enemy",  # Set name of the character to "Enemy"
            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
            special_power_1=choice(SPECIAL_POWERS),  # Assign "??? LIGHT ENERGY" to the enemy's special power 1
            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
        )
        for i in range(2):
            while enemy.special_power_1 == enemy.special_power_2:
                if enemy.special_power_1 == "Lv 1 Ice" or enemy.special_power_2 == "Lv 1 Ice":
                    if randint(1,3) == 1:
                        if enemy.special_power_1 == "Lv 1 Ice":
                            enemy.special_power_1 = "Lv 1 Ice"
                        elif enemy.special_power_2 == "Lv 1 Ice":
                            enemy.special_power_2 = "Lv 1 Ice"
                    else:
                        enemy = Character(
                            name="Enemy",  # Set name of the character to "Enemy"
                            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                        )
                if enemy.special_power_1 == "Lv 1 Lightning" or enemy.special_power_2 == "Lv 1 Lightning":
                    if randint(1,3) == 1:
                        if enemy.special_power_1 == "Lv 1 Lightning":
                            enemy.special_power_1 = "Lv 1 Lightning"
                        elif enemy.special_power_2 == "Lv 1 Lightning":
                            enemy.special_power_2 = "Lv 1 Lightning"
                    else:
                        enemy = Character(
                            name="Enemy",  # Set name of the character to "Enemy"
                            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                        )
                if enemy.special_power_1 == "Lv 1 Earth" or enemy.special_power_2 == "Lv 1 Earth":
                    if randint(1,3) == 1:
                        if enemy.special_power_1 == "Lv 1 Earth":
                            enemy.special_power_1 = "Lv 1 Earth"
                        elif enemy.special_power_2 == "Lv 1 Earth":
                            enemy.special_power_2 = "Lv 1 Earth"
                    else:
                        enemy = Character(
                            name="Enemy",  # Set name of the character to "Enemy"
                            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                        )
                if enemy.special_power_1 == "Lv 2 Metal" or enemy.special_power_2 == "Lv 2 Metal":
                    if randint(1,4) == 2:
                        if enemy.special_power_1 == "Lv 2 Metal":
                            enemy.special_power_1 = "Lv 2 Metal"
                        elif enemy.special_power_2 == "Lv 2 Metal":
                            enemy.special_power_2 = "Lv 2 Metal"
                    else:
                        enemy = Character(
                            name="Enemy",  # Set name of the character to "Enemy"
                            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                        )
                if enemy.special_power_1 == "Lv 2 Sound" or enemy.special_power_2 == "Lv 2 Sound":
                    if randint(1,4) == 2:
                        if enemy.special_power_1 == "Lv 2 Sound":
                            enemy.special_power_1 = "Lv 2 Sound"
                        elif enemy.special_power_2 == "Lv 2 Sound":
                            enemy.special_power_2 = "Lv 2 Sound"
                    else:
                        enemy = Character(
                            name="Enemy",  # Set name of the character to "Enemy"
                            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                        )
                if enemy.special_power_1 == "Lv 2 Magma" or enemy.special_power_2 == "Lv 2 Magma":
                    if randint(1,4) == 2:
                        if enemy.special_power_1 == "Lv 2 Magma":
                            enemy.special_power_1 = "Lv 2 Magma"
                        elif enemy.special_power_2 == "Lv 2 Magma":
                            enemy.special_power_2 = "Lv 2 Magma"
                    else:
                        enemy = Character(
                            name="Enemy",  # Set name of the character to "Enemy"
                            health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                            weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                            upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                            special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                            special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                            )
            print(".\n")
            sleep(2)
        if level >= 50:
            if level % 50 == 0:
                print(".\n"*5)
                sleep(4)
                print("LIGHT ENERGY HAS APPEARED IN THE WORLD!!")
                sleep(4)
                print("DARK ENERGY...")
                sleep(4)
                print("CURSE OF THE WORLD, FULL OF SIN AND HEINOUS CRIMES")
                sleep(4)
                print("LIGHT ENERGY...")
                sleep(4)
                print("SAVIOR OF THE WORLD AND THE WORLD'S HEAVEN IS FULL OF GOODNESS")
                sleep(4)
                print("THEY REUNITE AGAIN...")
                sleep(4)
                print("BUT...")
                sleep(4)
                print("THEY FIGHT EACH OTHER...")
                sleep(4)
                print("THE BATTLE WILL BEGUN...")
                sleep(2)
                enemy = Character(
                    name="Enemy",  # Set name of the character to "Enemy"
                    health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                    weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                    upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                    special_power_1="??? LIGHT ENERGY",  # Assign "??? LIGHT ENERGY" to the enemy's special power 1
                    special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
                )
        else:
            enemy = Character(
                name="Enemy",  # Set name of the character to "Enemy"
                health=randint(80, 100),  # Randomly assign the enemy's health between 80 and 100
                weapon=choice(WEAPONS),  # Randomly select a weapon from the available weapons list
                upgrade_decision="Not level 5 yet",  # Set a fixed upgrade decision for the enemy's weapon
                special_power_1=choice(SPECIAL_POWERS),  # Randomly select the first special power
                special_power_2=choice(SPECIAL_POWERS)  # Randomly select the second special power
            )
            enemy.LIGHTENERGY_locker = False
        # Ensure that the enemy's special powers are not the same
        while enemy.special_power_1 == enemy.special_power_2:
            enemy.special_power_2 = choice(SPECIAL_POWERS)
        # Ensure that the hero and enemy's special powers are not the same.
        while hero.special_power_1 == hero.special_power_2:
            hero.special_power_2 = choice(SPECIAL_POWERS)
        while enemy.special_power_1 == enemy.special_power_2:
            enemy.special_power_2 = choice(SPECIAL_POWERS)
        # Add the additional health to the hero's health.
        hero.health += additional_health
        # Print a message to the console to indicate the level of the special power.
        print("\nSPECIAL POWER LEVEL:")
        # Print a message to the console to explain the different levels of special powers.
        print("""\nLv 0 = Common Special Power:
- Fire
- Water
- Wind""")
        # Print a message to the console to explain the different levels of special powers.
        print("""\nLv 1 = Rare Special Power:
- Ice
- Lightning
- Earth""")
        # Print a message to the console to explain the different levels of special powers.
        print("""\nLv 2 = Epic Special Power:
- Metal
- Sound
- Magma""")
        # Print a message to the console to explain the different levels of special powers.
        print("""\nLv 3 = Legendary Special Power:
COMING SOON""")
        # Print a message to the console to explain the different levels of special powers.
        print("""\n??? = Myth Special Power:
- DARK ENERGY, \nNOTE: Used By Hero Only\nHINT: Try to get more than 14 level
- LIGHT ENERGY, \nNOTE: Used By Enemy Only\nHINT UPCOMING: Enemy try to get more than 49 level""")
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
                        # Determine the hero's damage output based on their class.
                        # Each class has a different amount of damage they can deal.
                        # The damage output is determined by adding a certain amount of damage
                        # to the minimum and maximum damage of the hero's weapon.
                        if hero_class == "Hero":
                            # If the hero is a Hero, the damage output is just the damage range of the weapon.
                            hero_damage = random.randint(*hero_damage_range)
                        elif hero_class == "Combative":
                            # If the hero is a Combative, the damage output is the damage range of the weapon plus 5.
                            hero_damage = random.randint(*hero_damage_range) + 5
                        elif hero_class == "Savior":
                            # If the hero is a Savior, the damage output is the damage range of the weapon plus 10.
                            hero_damage = random.randint(*hero_damage_range) + 10
                        elif hero_class == "The Salvation":
                            # If the hero is The Salvation, the damage output is the damage range of the weapon plus 15.
                            hero_damage = random.randint(*hero_damage_range) + 15
                        elif hero_class == "God":
                            # If the hero is a God, the damage output is the damage range of the weapon plus 20.
                            hero_damage = random.randint(*hero_damage_range) + 20
                        elif hero_class == "Unstoppable":
                            # If the hero is Unstoppable, the damage output is the damage range of the weapon plus 25.
                            hero_damage = random.randint(*hero_damage_range) + 25
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
                if hero.special_power_1 == "??? DARK ENERGY":
                    if hero.health == 0:
                        if second_life == 1:
                            sleep(4)
                            print("A portal just appear again front the hero while dying of the hero...")
                            sleep(4)
                            print("DEMON: What happened to you???")
                            sleep(4)
                            print("DEMON:...")
                            sleep(4)
                            print("DEMON: Okay fine...")
                            sleep(4)
                            print("DEMON: I will you give last chance to bring you back to life")
                            sleep(4)
                            print("DEMON: Don't dying again! Because this is your last chance me to bring you back to life!")
                            sleep(4)
                            hero.health = randint(80,100)
                            second_life = 0
                        else:
                            sleep(4)
                            print("You flying up to the sky and see the DEMON...")
                            sleep(4)
                            print("DEMON:...")
                            sleep(4)
                            print("DEMON: You back again?")
                            sleep(4)
                            print("DEMON: Well... WELCOME TO THE HELL!!!")
            if hero.health > 0:
                # Print a message to the console indicating that the hero has defeated the enemy.
                print("\nYou defeated the enemy!")
                hero_score += 1
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
                # Check the hero's level and assign a new class based on predefined milestones
                if level == 10:
                    # At level 10, the hero class is upgraded to "Combative"
                    print("\nYou got new class!!")
                    hero_class = "Combative"
                elif level == 20:
                    # At level 20, the hero class is upgraded to "Savior"
                    print("\nYou got new class!!")
                    hero_class = "Savior"
                elif level == 30:
                    # At level 30, the hero class is upgraded to "The Salvation"
                    print("\nYou got new class!!")
                    hero_class = "The Salvation"
                elif level == 40:
                    # At level 40, the hero class is upgraded to "God"
                    print("\nYou got new class!!")
                    hero_class = "God"
                elif level == 50:
                    # At level 50, the hero class is upgraded to "Unstoppable"
                    print("\nYou got new class!!")
                    hero_class = "Unstoppable"
                # Print out the hero's current class, level, health, and the enemy's health
                print(f"\nClass: {hero_class}")
                print(f"Hero Level: {level}")
                print(f"Hero Health: {hero.health}")
                print(f"Enemy Health: {enemy.health}")
                # Check if the hero's level is greater than 0 and divisible by 5.
                # This is a milestone level, and the hero gets to upgrade their weapon.
                if level > 0 and level % 5 == 0:
                    # Set the upgrade decision to "upgrade".
                    # This tells the hero to upgrade their weapon.
                    upgrade_decisions = "upgrade"
                    # Call the upgrade_weapon() method on the hero object.
                    # This method takes in the list of available weapons, and allows the hero to upgrade their weapon.
                    # The hero can choose from the list of available weapons, and the weapon's level is increased by 1.
                    # The weapon's additional damage is also increased by 3.
                    hero.upgrade_weapon()
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
    print(f"Hero's class last stand: {hero_class}")
    sleep(4)
    # Print the hero's last level to the console.
    print(f"Hero last Level: {level}")
    sleep(4)
    # Print the number of enemies that the hero has defeated.
    print(f"Enemies Defeated: {hero_score}\n")
    sleep(4)
    # Print a message to the console thanking the user for playing.
    print("Thanks for playing!")
# If the script is being run directly (i.e. not being imported), call the main function
if __name__ == "__main__":
    main()
