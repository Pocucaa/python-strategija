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
