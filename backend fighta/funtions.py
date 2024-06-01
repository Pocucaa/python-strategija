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
    self.shield += self.hp * 0.1

# def use_spell(self):
# def use item
# def move
# shiled se ne remuva na kraju turna




# ------------------------------------------------------------------------------------------------------------------------------------

# sta je kliknuo q,w,e d,a,m


# ------------------------------------------------------------------------------------------------------------------------------------ 

def assign_positions(mercenaries):

    sorted_mercenaries = sorted(mercenaries, key=lambda merc: merc.sp, reverse=True)

    for i, merc in enumerate(sorted_mercenaries):
        merc.position = i + 1

    return sorted_mercenaries


def assign_positions(teams):
  """
  Sorts mercenaries by speed in descending order for each team in the provided list of teams.
  Assigns positions from 1 to the number of mercenaries in each team.

  Args:
      teams: A list containing lists of mercenaries (representing teams).

  Returns:
      A list containing the sorted and positioned teams.
  """

  sorted_teams = []
  for team in teams:
    sorted_team = sorted(team, key=lambda merc: merc.sp, reverse=True)
    for i, merc in enumerate(sorted_team):
      merc.position = i + 1
    sorted_teams.append(sorted_team)

  return sorted_teams


















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






