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


def apply_regen(self, duration):
        # Heal amount is calculated as 2% of max HP
    heal_amount = int(0.02 * self.maxhp)
    self.apply_buff(duration, {"heal_amount": heal_amount})  # Apply buff with heal amount

def apply_heal(self, heal_amount):
        # Direct heal for the specified amount
    self.hp = min(self.hp + heal_amount, self.maxhp)  # Ensure HP doesn't exceed max HP



# fruits = ["apple", "banana"]
# fruits.append("orange")

# print(fruits)  # Output: ["apple", "banana", "orange"]