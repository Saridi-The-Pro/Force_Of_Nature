from random import choice, randint

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
weapons = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger"]
special_powers = ["Fire", "Water", "Ice"]

# Main game loop
repetition = "yes"
score = 0  # Track the number of enemies defeated

while repetition == "yes":
    # Initialize Hero and Enemy
    hero = Character(randint(15, 20), choice(weapons), choice(special_powers))
    enemy = Character(randint(15, 25), choice(weapons), choice(special_powers))

    print("\nA new enemy approaches!")
    declaration = input("Attack the enemy? (yes/no): ").strip().lower()

    if declaration == "yes":
        print("\nHero Stats:")
        print(hero.info())
        print("\nEnemy Stats:")
        print(enemy.info())

        while hero.health > 0 and enemy.health > 0:
            # Hero's turn
            hero_action = input("Choose action: 'attack' or 'dodge': ").strip().lower()
            if hero_action == "attack":
                damage = randint(5, 10)  # Randomize damage
                enemy.health -= damage
                print(f"\nYou attacked the enemy and dealt {damage} damage!")

                # Hero's special power effect
                if hero.special_power == "Fire":
                    burn_damage = 2
                    enemy.health -= burn_damage
                    print(f"Your fire power burns the enemy for {burn_damage} extra damage!")
                elif hero.special_power == "Water":
                    heal = 2
                    hero.health += heal
                    print(f"Your water power heals you for {heal} health!")
                elif hero.special_power == "Ice" and randint(1, 4) == 1:
                    enemy.is_frozen = True
                    print("Your ice power freezes the enemy! They lose their next turn!")

            elif hero_action == "dodge":
                print("\nYou dodged the enemy's attack!")
                continue
            else:
                print("\nInvalid action! The enemy attacks!")

            # Check if enemy is still alive
            if enemy.health <= 0:
                break

            # Enemy's turn (skipped if frozen)
            if not enemy.is_frozen:
                damage = randint(5, 8)
                hero.health -= damage
                print(f"The enemy attacked and dealt {damage} damage!")

                # Enemy's special power effect
                if enemy.special_power == "Fire":
                    burn_damage = 2
                    hero.health -= burn_damage
                    print(f"The enemy's fire power burns you for {burn_damage} extra damage!")
                elif enemy.special_power == "Water":
                    heal = 2
                    enemy.health += heal
                    print(f"The enemy's water power heals them for {heal} health!")
                elif enemy.special_power == "Ice" and randint(1, 4) == 1:
                    hero.is_frozen = True
                    print("The enemy's ice power freezes you! You lose your next turn!")
            else:
                print("The enemy is frozen and loses their turn!")
                enemy.is_frozen = False  # Reset frozen state

            # Show updated health
            print(f"\nHero Health: {hero.health}")
            print(f"Enemy Health: {enemy.health}")

        # Determine winner
        if hero.health > 0:
            print("\nYou defeated the enemy!")
            score += 1
            # Level-up mechanic
            hero.health += 5
            print("You leveled up! Your health increased by 5!")
        else:
            print("\nYou have been defeated by the enemy!")
            break

    else:
        print("\nYou let the enemy escape!")

    repetition = input("\nDo you want to restart the game? (yes/no): ").strip().lower()

# Endgame summary
print("\nGame Over!")
print(f"Enemies Defeated: {score}")
print("Thanks for playing!")
