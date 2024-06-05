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
# rage: +15% damage
# lifesteal: heal for % damage dealt from attacks
# manabutn: burn x mana

# --------------------------------------------------------------------------------------------------------------------------

def apply_stun(self, duration):

                already_stunned = False
                for debuff in self.debuffs:
                        if "is_stunned" in debuff and debuff["is_stunned"]:
                                already_stunned = True
                        debuff["duration"] += duration  # Extend duration if already stunned
                        print(f"{self.name}'s stun duration extended to {debuff['duration']} turns.")
                        break

                if not already_stunned:
                        self.debuffs.append({"is_stunned": True, "duration": duration})
                        print(f"{self.name} is stunned for {duration} turns.")

# --------------------------------------------------------------------------------------------------------------------------

def apply_burn(self, duration):

                already_burned = False
                for debuff in self.debuffs:
                        if "is_burned" in debuff and debuff["is_burned"]:
                                already_burned = True
                        debuff["duration"] += duration  # Extend duration if already stunned
                        print(f"{self.name}'s stun duration extended to {debuff['duration']} turns.")
                        break

                if not already_burned:
                        self.debuffs.append({"is_burned": True, "duration": duration})
                        print(f"{self.name} is burned for {duration} turns.")

# --------------------------------------------------------------------------------------------------------------------------

def apply_regen(self, duration):
                # Heal amount is calculated as 2% of max HP
                heal_amount = int(0.02 * self.maxhp)
                self.apply_buff(duration, {"heal_amount": heal_amount})  # Apply buff with heal amount

# --------------------------------------------------------------------------------------------------------------------------

def apply_heal(self, heal_amount):
                # Direct heal for the specified amount
                self.hp = min(self.hp + heal_amount, self.maxhp)  # Ensure HP doesn't exceed max HP

# --------------------------------------------------------------------------------------------------------------------------

def apply_shield(self, shield_amount):
                # Direct heal for the specified amount
                self.hp = min(self.hp + shield_amount, (self.maxhp * 1.5))  # Ensure SHIELD is 1.5 maxhp




# fruits = ["apple", "banana"]
# fruits.append("orange")

# print(fruits)  # Output: ["apple", "banana", "orange"]
