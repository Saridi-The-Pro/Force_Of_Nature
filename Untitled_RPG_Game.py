from random import randint
class HeroLongSword:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroKatana:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroBow:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroThrowableKnife:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroAxe:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroMace:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroSpear:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class HeroDagger:
    def __init__(self,hero_special_power):
        self.hero_special_power = hero_special_power
    def info(self):
        print("Special Power: ", self.hero_special_power)
class EnemyLongSword:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemyKatana:
    def __init__(self,enemey_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemyBow:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemyThrowableKnife:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemyAxe:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemyMace:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemySpear:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
class EnemyDagger:
    def __init__(self,enemy_special_power):
        self.enemy_special_power = enemy_special_power
    def info(self):
        print("Special Power: ", self.enemy_special_power)
repetition_2 = "yes"
while repetition_2 != "no":
    hero_weapons = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger"]
    hero_weapon = hero_weapons[randint(0,7)]
    hero_special_powers = ["Fire", "Water", "Ice"]
    hero_special_power = hero_special_powers[randint(0,2)]
    enemy_weapons = ["Long Sword", "Katana", "Bow", "Throwable Knife", "Axe", "Mace", "Spear", "Dagger"]
    enemy_weapon = enemy_weapons[randint(0,7)]
    enemy_special_powers = ["Fire", "Water", "Ice"]
    enemy_special_power = enemy_special_powers[randint(0,2)]
    if hero_weapon == "Long Sword":
        if hero_special_power == "Fire":
            HeroLongSword("Fire")
            HeroLongSword.info("Fire")
        if hero_special_power == "Water":
            HeroLongSword("Water")
            HeroLongSword.info("Water")
        if hero_special_power == "Ice":
            HeroLongSword("Ice")
            HeroLongSword.info("Ice")
    if enemy_weapon == "Long Sword":
        if enemy_special_power == "Fire":
            EnemyLongSword("Fire")
            EnemyLongSword.info("Fire")
        if enemy_special_power == "Water":
            EnemyLongSword("Water")
            EnemyLongSword.info("Water")
        if enemy_special_power == "Ice":
            EnemyLongSword("Ice")
            EnemyLongSword.info("Ice")
    repetition = input("Do you want to restart the game??")
    repetition_2 = repetition.lower()