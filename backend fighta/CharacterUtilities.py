import pygame, sys  
import random

# ------------------------------------------------------------------------------------------------------------------------------------

class Mercenary:
        def __init__(self, name, maxhp, hp, at, mana, mv, sp, shield):
                self.name = name
                self.maxhp = int(round(maxhp)) 
                self.hp = int(round(hp))    
                self.at = int(round(at))    
                self.mana = int(round(mana))  
                self.mv = int(round(mv))    
                self.sp = int(round(sp))    
                self.shield = int(round(shield))  
                self.position = 0
                self.alive = 1
                self.buffs = []
                self.debuffs = []

# --------------------------------------------------------------------------------------------------------------------------

        def apply_stun(self, duration):

                        already_stunned = False
                        for debuff in self.debuffs:
                                if "is_stunned" in debuff and debuff["is_stunned"]:
                                        already_stunned = True
                                debuff["duration"] += duration  # Extend duration if already stunned
                                print(f"{self.name}'s stun duration extended to {debuff['duration']} turns.")
                                break

                        if not already_stunned:
                                self.debuffs.append({"is_stunned": True, "duration": duration})
                                print(f"{self.name} is stunned for {duration} turns.")

# --------------------------------------------------------------------------------------------------------------------------

        def apply_burn(self, duration):

                        already_burned = False
                        for debuff in self.debuffs:
                                if "is_burned" in debuff and debuff["is_burned"]:
                                        already_burned = True
                                debuff["duration"] += duration  # Extend duration if already stunned
                                print(f"{self.name}'s stun duration extended to {debuff['duration']} turns.")
                                break

                        if not already_burned:
                                self.debuffs.append({"is_burned": True, "duration": duration})
                                print(f"{self.name} is burned for {duration} turns.")

# --------------------------------------------------------------------------------------------------------------------------
# nije dobar
        def apply_regen(self, duration):
                        
                        heal_amount = int(0.02 * self.maxhp)        # Heal amount is calculated as 2% of max HP
                        self.buffs.append(duration, {"heal_amount": heal_amount})  # Apply buff with heal amount

# --------------------------------------------------------------------------------------------------------------------------

        def apply_heal(self, heal_amount):
                        # Direct heal for the specified amount
                        self.hp = min(self.hp + heal_amount, self.maxhp)  # Ensure HP doesn't exceed max HP

# --------------------------------------------------------------------------------------------------------------------------

        def apply_shield(self, shield_amount):
                        # Direct heal for the specified amount
                        self.shield = min(self.hp + shield_amount, (self.maxhp * 1.5))  # Ensure SHIELD is 1.5 maxhp

# ------------------------------------------------------------------------------------------------------------------------------------

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
