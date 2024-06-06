
# --------------------------------------------------------------------------------------------------------------------------

def attack(self, target):
        
        crit = 0

        if target.hp > 0:
            damage = self.at + crit

        if damage < target.shield > 0 :
            target.shield -= int(round(damage))

        elif damage > target.shield > 0:
            target.hp -= int(round(damage - target.shield))
            target.shield = 0

        elif target.shield == 0:
            target.hp -= int(round(damage))

        if target.hp < 0:
            target.alive = 0
        # pokreni smrt funckiju

# --------------------------------------------------
        if target.hp > 0:
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else: 
            print(f"{target.name} is dead.")
            
        # onhit passive
        # crit

# --------------------------------------------------------------------------------------------------------------------------

def defend(self):

    self.shield = min(self.hp + int(round(self.maxhp * 0.05)), (self.maxhp * 1.5))  # Ensure SHIELD is 1.5 maxhp

# --------------------------------------------------------------------------------------------------------------------------

def heal(self, amount):

    self.shield = min(self.hp + int(round(amount)), (self.maxhp))
# --> koji mercenari --> mercenary.heal(10)

# --------------------------------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------------------------------

def char_infront(pos_x, target_x, tile_size):

    if target_x == pos_x + tile_size:
        return True
    else:
        return False

# ------------------------------------------------------------------------------------------------------------------------------------

# sta je kliknuo q,w,e d,a,m


# ------------------------------------------------------------------------------------------------------------------------------------ 






















