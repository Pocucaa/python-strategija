from CharacterUtilities import *
from funtions import *
from CurrentParty import *

# def, at, move, qwe, item
# ! -> dodati i enemije

# hocemo po speedu ili jedan po jedan po potezu ili be spida ti biras

def Fight_start(player_team, enemy_team, action):

    sorted_mercenaries = assign_positions(player_team)
    for merc in sorted_mercenaries:
    #    print(f"Name: {merc.name}, Speed: {merc.sp}, Position: {merc.position}")
        
        if action == 4:
            attack(merc, mercenary2)
            print(f" HP = {mercenary2.hp}")

        if action == 3:
            defend(merc)
            print(f"SHIELD = {merc.shield}")

    sorted_mercenaries = assign_positions(enemy_team)

