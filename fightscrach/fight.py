from CharacterUtilities import *
from functions import *
from CurrentParty import *
from debuffbuff_check import *
from spells import *
from collections import deque

# ! -> dodati i enemije

# proveri da li su koordinate misa na tajlu gde je enemy, check target

def Fight_start(player_team, enemy_team, action):


    # all_mercenaries = list(player_team + enemy_team)
    # all_mercenaries.sort(key=lambda merc: merc.sp, reverse=True)

    # while all_mercenaries:                                  # gotovo kad prodje kroz sve i prodje 1 ciklus
    #     current_merc = all_mercenaries.popleft()


# --------------------------------------------------------------------------------------------------------------------------
# handle debuffs ( separate function?)

#   # Handle debuffs
#     for debuff in self.debuffs[:]:  # Use a copy to avoid index issues during removal
#         if "is_stunned" in debuff and debuff["is_stunned"]:
#         # Handle stun effect (e.g., print message, prevent actions)
#             print(f"{self.name} is stunned and cannot act!")

#         # Handle burn effect (assuming it deals damage)
#         elif "is_burned" in debuff and debuff["is_burned"]:
#             damage = 2  # Replace with your burn damage calculation
#             self.hp -= damage
#             debuff["duration"] -= 1
#             print(f"{self.name} takes {damage} burn damage!")

#         if debuff["duration"] <= 0:
#                 self.debuffs.remove(debuff)
#                 print(f"{self.name}'s burn has ended.")
            
        print(mercenary2.debuffs)

        # Check for stun debuff (assuming "is_stunned" key is used)
        if any(debuff["is_stunned"] for debuff in mercenary2.debuffs):
            print(f"{mercenary2.name} is stunned and cannot act!")

        # Decrement the duration of each debuff with "is_stunned": True
        for debuff in mercenary2.debuffs:
            if debuff["is_stunned"]:
                debuff["stun_duration"] -= 1  # Decrement duration by 1 for stunned debuffs
            # Optionally, remove debuffs with zero duration
            if debuff["stun_duration"] <= 0:
                mercenary2.debuffs.remove(debuff)  # Remove debuff if duration reaches zer

# --------------------------------------------------------------------------------------------------------------------------
#actions
        if action == 1:
            attack(mercenary1, mercenary2)  # Replace with target selection logic
            print(f" HP = {mercenary2.hp}")  # Assuming target has hp attribute

        elif action == 2:
            defend(mercenary1)
            print(f"SHIELD = {mercenary1.shield}")

        elif action == 4:
            spell1(mercenary1, mercenary2)  # Replace with target selection logic

        elif action == 5:
            spell2(mercenary1)  # Replace with target selection logic

        # elif action == 6:
            # spell2(mercenary1)  # Replace with target selection logic

# --------------------------------------------------------------------------------------------------------------------------


# def start_turn(self):
#         # Check for and apply debuffs at the start of the turn
#         for debuff in self.debuffs:
#             debuff.on_turn_start(self)
#             debuff.tick()
#             if debuff.is_expired():
#                 self.debuffs.remove(debuff)


# # Example target selection function (replace with your actual logic)
# def select_target(mercenary, enemy_team):
#     # Implement logic to choose a target from the enemy team (e.g., weakest enemy)
#     # This is a placeholder, replace with your desired target selection strategy
#     return enemy_team[0]

