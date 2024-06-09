import pygame, sys  

tile_size = 50
# ------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------

class Mercenary:
        def __init__(self, name, maxhp, hp, at, mana, mv, sp, shield):
                self.name = name
                self.maxhp = int(round(maxhp)) 
                self.hp = int(round(hp))    
                self.at = int(round(at))    
                self.mana = int(round(mana))  
                self.mv = int(round(mv))    
                self.sp = int(round(sp))    
                self.shield = int(round(shield))  
                self.position = [None , None]
                self.alive = 1
                self.buffs = []
                self.debuffs = []


# --------------------------------------------------------------------------------------------------------------------------

        def apply_stun(self, duration):

                        already_stunned = False
                        for debuff in self.debuffs:
                                if "is_stunned" in debuff and debuff["is_stunned"]:
                                        already_stunned = True
                                debuff["stun_duration"] += duration  # Extend duration if already stunned
                                print(f"{self.name}'s stun duration extended to {debuff['stun_duration']} turns.")
                                break

                        if not already_stunned:
                                self.debuffs.append({"is_stunned": True, "stun_duration": duration})
                                print(f"{self.name} is stunned for {duration} turns.")

# --------------------------------------------------------------------------------------------------------------------------

        def apply_burn(self, duration):

                        already_burned = False
                        for debuff in self.debuffs:
                                if "is_burned" in debuff and debuff["is_burned"]:
                                        already_burned = True
                                debuff["burn_duration"] += duration  # Extend duration if already stunned
                                print(f"{self.name}'s stun duration extended to {debuff['burn_duration']} turns.")
                                break

                        if not already_burned:
                                self.debuffs.append({"is_burned": True, "burn_duration": duration})
                                print(f"{self.name} is burned for {duration} turns.")

# --------------------------------------------------------------------------------------------------------------------------
# nije dobar
        def apply_regen(self, duration):
                        
                        heal_amount = int(0.02 * self.maxhp)        # Heal amount is calculated as 2% of max HP
                        self.buffs.append(duration, {"heal_amount": heal_amount})  # Apply buff with heal amount

# --------------------------------------------------------------------------------------------------------------------------

        def apply_heal(self, heal_amount):
                        # Direct heal for the specified amount
                        self.hp = min(self.hp + heal_amount, self.maxhp)  # Ensure HP doesn't exceed max HP

# --------------------------------------------------------------------------------------------------------------------------

        def apply_shield(self, shield_amount):
                        # Direct heal for the specified amount
                        self.shield = min(self.hp + shield_amount, (self.maxhp * 1.5))  # Ensure SHIELD is 1.5 maxhp

# ------------------------------------------------------------------------------------------------------------------------------------                
class Character:
        def __init__(self, spritesheet_path, num_frames, animation_speed=0.1):
                self.spritesheet = pygame.image.load(spritesheet_path)
                self.num_frames = num_frames
                self.frame_width = self.spritesheet.get_width() // num_frames
                self.frame_height = self.spritesheet.get_height()
                self.current_frame = 0
                self.animation_speed = animation_speed  # Adjust as needed
                self.animation_timer = 0
                self.frames_to_skip = 4 - num_frames
                self.current_image = None  # New attribute to hold the current frame surface

        def update(self, dt):
                self.animation_timer += dt

                if self.animation_timer >= self.animation_speed:
                        self.current_frame = (self.current_frame + 1) % self.num_frames
                        self.current_image = self.get_current_frame()  # Update current_image after frame change

                if self.current_frame >= self.num_frames - self.frames_to_skip:
                        self.current_frame = 0
                        self.current_image = self.get_current_frame()  # Update current_image after reset

        def get_current_frame(self):
                frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
                return self.spritesheet.subsurface(frame_rect)

        def draw(self, surface, x, y, character_sprite_size):
                if self.current_image is not None:  # Check if current_image is updated
                        sprite_width = character_sprite_size
                        sprite_height = character_sprite_size
                        resized_frame_surface = pygame.transform.scale(self.current_image, (sprite_width, sprite_height))
                        surface.blit(resized_frame_surface, (x, y))

        # def flip_character_animation(character, is_flipped):
        #         @staticmethod
        #         def flipped_get_current_frame(self):
        #                 frame_surface = self.get_current_frame()
        #                 if is_flipped:
        #                         frame_surface = pygame.transform.flip(frame_surface, True, False)
        #                 return frame_surface

        #         character.get_current_frame = flipped_get_current_frame if is_flipped else super().get_current_frame


# ------------------------------------------------------------------------------------------------------------------------------------ 

# class Character:
#         def __init__(self, spritesheet_path, num_frames, animation_speed=0.1):
#                 self.spritesheet = pygame.image.load(spritesheet_path)
#                 self.num_frames = num_frames
#                 self.frame_width = self.spritesheet.get_width() // num_frames 
#                 self.frame_height = self.spritesheet.get_height() # kad imas vise redova prosiri
#                 self.current_frame = 0
#                 self.animation_speed = animation_speed  # Adjust as needed
#                 self.animation_timer = 0
#                 self.frames_to_skip = 4 - num_frames

# # ------------------------------------------------------------------------------------------------------------------------------------

#         def update(self, dt):
#                 self.animation_timer += dt

#                 if self.animation_timer >= self.animation_speed:
#                         self.current_frame = (self.current_frame + 1) % self.num_frames
#                         self.animation_timer = 0
#                 if self.current_frame >= self.num_frames - self.frames_to_skip:
#                         self.current_frame = 0

# # ------------------------------------------------------------------------------------------------------------------------------------

#         def draw(self, surface, x, y, character_sprite_size):
#                 frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
#                 frame_surface = self.spritesheet.subsurface(frame_rect)
#                 resized_frame_surface = pygame.transform.scale(frame_surface, (character_sprite_size, character_sprite_size))
#                 surface.blit(resized_frame_surface, (x, y))

# # ------------------------------------------------------------------------------------------------------------------------------------


#         def flip_character_animation(self, is_flipped):

#                 if is_flipped:
#                         self.get_current_frame = lambda self: pygame.transform.flip(super().get_current_frame(), True, False)  # Flip horizontally only
#                 else:
#                         # Revert the get_current_frame method to its original behavior (no flip)
#                         self.get_current_frame = super().get_current_frame

# ------------------------------------------------------------------------------------------------------------------------------------

        def get_width(self):
                return self.frame_width

        def get_height(self):
                return self.frame_height

        def get_position(self):

                self.center_width  = self.frame_width / 2
                self.center_height  = self.frame_height / 2
                half_tile = (tile_size)

                self.pos_x = half_tile -self.center_width
                self.pos_y = half_tile -self.center_height

                return self.position[self.pos_x, self.pos_y]
        
        def half_tile(tile_size):
                tile_size_half = tile_size / 2
                return tile_size_half
        
# ------------------------------------------------------------------------------------------------------------------------------------

####

# ------------------------------------------------------------------------------------------------------------------------------------

####

# ------------------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------------------ 


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

# ------------------------------------------------------------------------------------------------------------------------------------

####

# ------------------------------------------------------------------------------------------------------------------------------------

####

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