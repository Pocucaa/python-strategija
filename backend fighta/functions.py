

# --------------------------------------------------------------------------------------------------------------------------

def attack(self, target):
        if target.hp > 0:
            damage = self.at
            target.hp -= int(round(damage))

        if target.hp < 0:
            target.alive = 0
        # pokreni smrt funckiju

        if target.hp > 0:
            print(f"{self.name} attacks {target.name} for {damage} damage!")
        else: 
            print(f"{target.name} is dead.")
            
        # onhit passive
        # crit

# --------------------------------------------------------------------------------------------------------------------------

def defend(self):

    self.shield = min(self.hp + int(round(self.maxhp * 0.1)), (self.maxhp * 1.5))  # Ensure SHIELD is 1.5 maxhp

# --------------------------------------------------------------------------------------------------------------------------

def heal(self, amount):
    if self.hp + amount > self.maxhp:
        self.hp = self.maxhp  # Prevent overhealing
    else:
        self.hp += amount

# --------------------------------------------------------------------------------------------------------------------------

# --> koji mercenari --> mercenary.heal(10)


# def move
# shiled se ne remuva na kraju turna




# ------------------------------------------------------------------------------------------------------------------------------------

# sta je kliknuo q,w,e d,a,m


# ------------------------------------------------------------------------------------------------------------------------------------ 






















