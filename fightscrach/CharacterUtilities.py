
character_position = [190, 160]
character_position1 = [230, 180]

class Mercenary:
    def __init__(self, name, hp=100, at=10, mana=50, mv=5):
        self.name = name
        self.hp = hp  # Hit Points
        self.at = at  # Attack
        self.mana = mana  # Mana
        self.mv = mv  # Movement
        # self.shield = shield
        # self.startx = startx
        # self.starty = starty
        # self.x = x  # Starting x position
        # self.y = y  # Starting y position
        # self.c = (max 5)
        # self.type = type (ap ili ad)
        # self.ev =
        # self.mb
        # self.pb

    def attack(self, target):
        target.hp -= self.at
        # onhit passive
        
    def heal(self, amount):
        self.hp += amount

    def cast_spell(self, spell_mana_cost, spell_name):
        if self.mana >= spell_mana_cost:
            self.mana -= spell_mana_cost

        else:
            print("Not enough mana to cast the spell.")

    def move(self, distance):
        if distance <= self.mv:
            print("Moved {} tiles.".format(distance))
        else:
            print("Cannot move that far. Maximum movement range exceeded.")

mercenary1 = Mercenary(name="Mercenary1", hp=120, at=8, mana=80, mv=6)
mercenary2 = Mercenary(name="Mercenarythorns", hp=180, at=14, mana=40, mv=4)
mercenary11 = Mercenary(name="Mercenary1", hp=121, at=9, mana=81, mv=6)
mercenary22 = Mercenary(name="Mercenary1", hp=182, at=14, mana=42, mv=4)

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
