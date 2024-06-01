# bleed: 2max ph damage end turn, 10% more damage taken
# red burn: 1mhp damage end turn
# {
# blue burn: 1.5mhp damage end turn, undispelable
# black burn: 2.5mhp damage end turn, undispelable, cannot heal
# }
# blind: cant attack
# green poison: take start turn damage, lowers poison by 7
# {
# pink posion:
# }
# stun: skips turn
# spell damage taken: % 
# phisical damage taken: % ( nema armora)
# manablock: cant cast spells 
# charm: 20% misschanse, take 10% less damage
# confusion: 10% chanse to be stunned start turn
# regen: end of turn heal 3% hp


# def Bleedcheck (bleed):
#     if bleed == true:

    # def RegenCheck (regen):
    #     if regen == true:
    #         mercenary.Hp =+ mercenary.HP + 
    #     if regen == false:
    #         skip


# Define functions for checking passive effects and debuffs (you'll need to implement these)


class Buff:
    def __init__(self, name, duration, modifiers):
        self.name = name
        self.duration = duration
        self.modifiers = modifiers  # Dictionary of stat changes (e.g., {"damage": 0.2, "accuracy": 0.1})

class Debuff:
    def __init__(self, name, duration, effects):
        self.name = name
        self.duration = duration
        self.effects = effects  # List of functions to apply during the debuff (e.g., reduce_speed)


def apply_buff(mercenary, buff):
    mercenary.active_buffs.append(buff)

def apply_debuff(mercenary, debuff):
    mercenary.active_debuffs.append(debuff)

def apply_regeneration_buff(mercenary, duration):
    buff = RegenerationBuff(duration)
    apply_buff(mercenary, buff)

class RegenerationBuff(Buff):
    def __init__(self, duration):
        super().__init__("Regeneration", duration, {})  # No initial modifiers

    def on_turn_end(self, mercenary):
        mercenary.heal(2)  # Heal 2 MHP at the end of the turn
