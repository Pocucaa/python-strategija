from CharacterUtilities import *


mercenary1 = Mercenary(name="Mercenary1", hp=120, at=8, mana=80, mv=6, sp=5)
mercenary2 = Mercenary(name="Mercenarythorns", hp=180, at=14, mana=40, mv=4, sp=4)


# ------------------------------------------------------------------------------------------------------------------------------------ 
player_team = [
    mercenary1, mercenary2, 
    # mercenary3, mercenary4, mercenary5, 
    # mercenary6, mercenary7, mercenary8, mercenary9, mercenary10
    ]
# ------------------------------------------------------------------------------------------------------------------------------------ 












# coordinates
# buffsdebuffs

# izjednacava svojih 10 slotova sa statistikom karakter utiliries
# ako se karakter obrise, klinuje se taj placeholder,
# ako se karakter levelaupje i sve uzima se is lvlup funckije

# takodje storuje sve ajteme koje imas

# lvlup funckija, povecava sav stats za neke procente
# lvl 10 op level

# game func 
# - debuffbuff pre turn check
# ( turn)
# - debuffendturn effect

# array poredjanih po brzini kako ko krecei menja se idex karaktera [0] pa nadalje, kada je index veci od karakteri - 1
# resetuje se, 

# neprijateljski ai mora za pocetak da bude 20% attak 40% lowes health enemy svaka 3 turna ability pomocu ability buffera
# neke stvari ce davati na neprijatelje taj buffer, pa ce cesce bacati spellove