class Mercenary:
    def __init__(self, hp=100, at=10, mana=50, mv=5):
        self.hp = hp  # Hit Points
        self.at = at  # Attack
        self.mana = mana  # Mana
        self.mv = mv  # Movement
        # self.startx = startx
        # self.starty = starty
        # self.x = x  # Starting x position
        # self.y = y  # Starting y position

    def attack(self, target):
        target.hp -= self.at

    def heal(self, amount):
        self.hp += amount

    def cast_spell(self, spell_mana_cost):
        if self.mana >= spell_mana_cost:
            self.mana -= spell_mana_cost
            # Perform spell casting actions here
        else:
            print("Not enough mana to cast the spell.")

    def move(self, distance):
        if distance <= self.mv:
            print("Moved {} tiles.".format(distance))
        else:
            print("Cannot move that far. Maximum movement range exceeded.")

mercenary1 = Mercenary(hp=120, at=8, mana=80, mv=6)
mercenary2 = Mercenary(hp=180, at=14, mana=40, mv=4)

# hp 
# at 
# mn 
# mv 
# cp 
# pss
# q         --> spells
# w         --> spells
# e         --> spells

