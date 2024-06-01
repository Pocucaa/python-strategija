import pygame, sys  
import random

# ------------------------------------------------------------------------------------------------------------------------------------

class Mercenary:
    def __init__(self, name, maxhp, hp, at, mana, mv, sp, shield):
        self.name = name
        self.maxhp = int(round(maxhp))  # Round maxhp to whole number
        self.hp = int(round(hp))        # Round hp to whole number
        self.at = int(round(at))        # Round at to whole number
        self.mana = int(round(mana))    # Round mana to whole number
        self.mv = int(round(mv))        # Round mv to whole number
        self.sp = int(round(sp))        # Round sp to whole number
        self.shield = int(round(shield))  # Round shield to whole number
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
