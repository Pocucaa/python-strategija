from CharacterUtilities import *
from funtions import *
from CurrentParty import *

# def, at, move, qwe, item

def Fight_start(player_team, enemy_team, action):

    sorted_mercenaries = assign_positions(player_team)
    for merc in sorted_mercenaries:
        print(f"Name: {merc.name}, Speed: {merc.sp}, Position: {merc.position}")








  #  if action == 4:
 #       attack(current_mercenary, target)


