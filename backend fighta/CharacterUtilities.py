import pygame, sys  
import random

# ------------------------------------------------------------------------------------------------------------------------------------

class Mercenary:
    def __init__(self, name, hp, at, mana, mv, sp):
        self.name = name
        self.hp = hp  # Hit Points
        self.at = at  # Attack
        self.mana = mana  # Mana
        self.mv = mv  # Movement
        self.sp = sp
        self.position = 0
        # self.shield = shield
        # self.startx = startx
        # self.starty = starty
        # self.x = x  # Starting x position
        # self.y = y  # Starting y position
        # self.cb = (max 5)
        # self.type = type (ap ili ad)
        # self.crit = crit
        # self.ev =
        # self.mb
        # self.pb

    # def move(self, mv, position):

    def attack(self, target):
        if target.hp > 0:
            damage = self.at
            target.hp -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else:
            print(f"{target.name} is already down!")
        # onhit passive
        # crit


    def skip_turn(self):
        print(f"{self.name} skips their turn.")

# ------------------------------------------------------------------------------------------------------------------------------------

    # def Turn():
    #     for 

    # def Fight():
        

# ------------------------------------------------------------------------------------------------------------------------------------ 

def assign_positions(mercenaries):
    # Sort the mercenaries based on speed in descending order
    sorted_mercenaries = sorted(mercenaries, key=lambda merc: merc.sp, reverse=True)

    # Assign positions from 1 to 10
    for i, merc in enumerate(sorted_mercenaries):
        merc.position = i + 1

    return sorted_mercenaries


def update_positions(mercenaries):
    while True:
        # Sort and assign positions
        sorted_mercenaries = assign_positions(mercenaries)
        
        # Print the sorted mercenaries with their positions
        for merc in sorted_mercenaries:
            print(merc)
        
        # Increment position for the next iteration
        for merc in mercenaries:
            merc.sp += 1
        
        # Break after one iteration for demonstration
        break

# Example usage


# ------------------------------------------------------------------------------------------------------------------------------------


def assign_positions(mercenaries):
    # Sort the mercenaries based on speed in descending order
    sorted_mercenaries = sorted(mercenaries, key=lambda merc: merc.sp, reverse=True)

    # Assign positions from 1 to 10
    for i, merc in enumerate(sorted_mercenaries):
        merc.position = i + 1

    return sorted_mercenaries

def take_turn(mercenary, mercenaries):
    if random.choice([True, False]):
        # Attack a random target
        target = random.choice([m for m in mercenaries if m != mercenary and m.hp > 0])
        mercenary.attack(target)
    else:
        # Skip turn
        mercenary.skip_turn()

def update_positions(mercenaries):
    while True:
        # Sort and assign positions
        sorted_mercenaries = assign_positions(mercenaries)

        # Each mercenary takes a turn
        for merc in sorted_mercenaries:
            if merc.hp > 0:
                take_turn(merc, sorted_mercenaries)

        # Increment position for the next iteration
        for merc in mercenaries:
            merc.sp += 1

        # Break after one iteration for demonstration
        break

# Example usage
mercenary1 = Mercenary(name="Mercenary1", hp=120, at=8, mana=80, mv=6, sp=5)
mercenary2 = Mercenary(name="Mercenarythorns", hp=180, at=14, mana=40, mv=4, sp=7)
mercenary3 = Mercenary(name="Mercenaryfast", hp=100, at=10, mana=60, mv=8, sp=9)

mercenaries = [mercenary1, mercenary2, mercenary3]

update_positions(mercenaries)

# ------------------------------------------------------------------------------------------------------------------------------------



# hp 
# at 
# mn 
# mv 
# cp 
# pss
# q         --> spells
# w         --> spells
# e         --> spells
# coordinates
# dal je ap ili ad, zbog damagea
# evasines
# magic block
# physical block
