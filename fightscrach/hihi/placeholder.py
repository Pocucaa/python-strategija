# Import necessary modules or classes
from battle_assets.CurrentParty import *
import random
from battle_assets.debuffbuff_check import *

# Define the fight function
def fight(player_team, enemy_team):

    all_mercenaries = player_team + enemy_team
    all_mercenaries.sort(key=lambda merc: merc.speed, reverse=True)
    
    # Iterate through all mercenaries in turn order
    for mercenary in all_mercenaries:
        # Check for passive effects and debuffs before the turn
        # (You'll need to implement these checks based on your game's mechanics)
        check_passive_effects(mercenary)
        check_debuffs(mercenary)
        
        # Take turn for each mercenary
        if mercenary in player_team:
            # Player's turn
            player_turn(mercenary, enemy_team)
        else:
            # Enemy's turn
            enemy_turn(mercenary, player_team)
        
        # Check for passive effects and debuffs after the turn
        # (You'll need to implement these checks based on your game's mechanics)
        check_passive_effects(mercenary)
        check_debuffs(mercenary)

# Define functions for player and enemy turns (you'll need to implement these)
def player_turn(mercenary, enemy_team):
    """
    Simulates a turn for a player-controlled mercenary.
    
    Args:
        mercenary (Mercenary): The player-controlled mercenary taking the turn.
        enemy_team (list): List of Mercenary objects representing the enemy team.
    """
    # Implement player's turn logic here
    pass

def enemy_turn(mercenary, player_team):
    """
    Simulates a turn for an enemy mercenary.
    
    Args:
        mercenary (Mercenary): The enemy mercenary taking the turn.
        player_team (list): List of Mercenary objects representing the player's team.
    """
    # Implement enemy's turn logic here
    pass

def passive(mercenary, target, damage):

    if mercenary.name == "Mercenarythorns":
        target.hp -= int(0.3 * damage)  # Reflect 30% of the damage
    else:
        return 0  # No damage reflection for other mercenaries


    
# Start the fight
fight(player_team, enemy_team)
