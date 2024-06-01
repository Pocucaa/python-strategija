from spells import *

def attack(self, target):
        if target.hp > 0:
            damage = self.at
            target.hp -= damage

        if target.hp < 0:
            target.alive == 0
        # pokreni smrt funckiju

        if target.hp > 0:
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else: 
            print(f"{target.name} is dead.")
            
        # onhit passive
        # crit


def defend(self):
    self.shield += self.hp * 0.05

# def use_spell(self):
# def use item
# def move
# shiled se ne remuva na kraju turna




# ------------------------------------------------------------------------------------------------------------------------------------

# sta je kliknuo q,w,e d,a,m


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

# update_positions(mercenaries)






