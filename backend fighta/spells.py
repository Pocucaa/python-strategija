# buzdovan bata ------------
# passive thorns, return 30% damage

# 1. hit stun
# stun 1, 1.8x damage
# combo: stun 2, 2.3x damage, gain 150 shield

# 2. shield
# gain 40 shield
# combo: gain megashield 120

# 3. charge
# charge 4 tiles, first target hit, stun 1, 33% damage
# combo: 6 tiles, 66% damage, aply 2 weaken

from CharacterUtilities import *
from CurrentParty import *
from debuffbuff_check import *

def spell1(self, target):
        if target.hp > 0:
            damage = self.at * 1.8
            target.hp -= int(round(damage))
            target.apply_stun(2)

        if target.hp < 0:
            target.alive = 0
        # pokreni smrt funckiju

        if target.hp > 0:
            print(f"{self.name} bonks {target.name} for {damage} damage!")
            print(f" Target HP = {target.hp}")
        else: 
            print(f"{target.name} is dead.")

def spell2(self):
    if self.hp > 0:
        self.apply_shield(40)