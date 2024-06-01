from CharacterUtilities import *
from funtions import *
from CurrentParty import *
from debuffbuff_check import *
from spells import *
from collections import deque

# def, at, move, qwe, item
# ! -> dodati i enemije






def Fight_start(player_team, enemy_team, action):

    # all_mercenaries = list(player_team + enemy_team)
    # all_mercenaries.sort(key=lambda merc: merc.sp, reverse=True)

    # while all_mercenaries:                                  # gotovo kad prodje kroz sve i prodje 1 ciklus
    #     current_merc = all_mercenaries.popleft()

        # # Apply buffs at the end of the turn (assuming your turn logic progresses through this loop)
        # for buff in current_merc.active_buffs:
        #     if buff.__class__ == RegenerationBuff:  # Check for RegenerationBuff
        #         buff.on_turn_end(current_merc)  # Call the specific on_turn_end method

        if action == 1:
            attack(mercenary1, mercenary2)  # Replace with target selection logic
            print(f" HP = {mercenary2.hp}")  # Assuming target has hp attribute

        elif action == 2:
            defend(mercenary1)
            print(f"SHIELD = {mercenary1.shield}")

        elif action == 4:
            spell1(mercenary1, mercenary2)  # Replace with target selection logic




# Example target selection function (replace with your actual logic)
def select_target(mercenary, enemy_team):
    # Implement logic to choose a target from the enemy team (e.g., weakest enemy)
    # This is a placeholder, replace with your desired target selection strategy
    return enemy_team[0]

