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

def heal(self, amount):
    if self.hp + amount > self.maxhp:
        self.hp = self.maxhp  # Prevent overhealing
    else:
        self.hp += amount

# --> koji mercenari --> mercenary.heal(10)


# def use_spell(self):
# def use item
# def move
# shiled se ne remuva na kraju turna




# ------------------------------------------------------------------------------------------------------------------------------------

# sta je kliknuo q,w,e d,a,m


# ------------------------------------------------------------------------------------------------------------------------------------ 


# def Fight_start(player_team, enemy_team, action):

#     all_mercenaries = deque(player_team + enemy_team)
#     all_mercenaries.sort(key=lambda merc: merc.sp, reverse=True)

#     while all_mercenaries:                                  # gotovo kad prodje kroz sve i prodje 1 ciklus
#         current_merc = all_mercenaries.popleft()

#         # Apply buffs at the end of the turn (assuming your turn logic progresses through this loop)
#         for buff in current_merc.active_buffs:
#             if buff.__class__ == RegenerationBuff:  # Check for RegenerationBuff
#                 buff.on_turn_end(current_merc)  # Call the specific on_turn_end method

#         # Your action logic (attack, defend, spell) based on chosen action (action == 4, 3, or 5)
#         if action == 1:
#             attack(current_merc, select_target(current_merc, enemy_team))  # Replace with target selection logic
#             print(f" HP = {current_merc.target.hp}")  # Assuming target has hp attribute
#         elif action == 2:
#             defend(current_merc)
#             print(f"SHIELD = {current_merc.shield}")
#         elif action == 4:
#             spell1(current_merc, select_target(current_merc, enemy_team))  # Replace with target selection logic

#     # All turns completed
#     print("All turns finished!")



# # Example target selection function (replace with your actual logic)
# def select_target(mercenary, enemy_team):
#     # Implement logic to choose a target from the enemy team (e.g., weakest enemy)
#     # This is a placeholder, replace with your desired target selection strategy
#     return enemy_team[0]




















