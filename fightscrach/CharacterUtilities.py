import pygame, sys  
tile_size = 50
# ------------------------------------------------------------------------------------------------------------------------------------

class Mercenary:
    def __init__(self, name, hp, at, mana, mv):
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
        # self.cb = (max 5)
        # self.type = type (ap ili ad)
        # self.crit = crit
        # self.ev =
        # self.mb
        # self.pb

mercenary1 = Mercenary(name="Mercenary1", hp=120, at=8, mana=80, mv=6)
mercenary2 = Mercenary(name="Mercenarythorns", hp=180, at=14, mana=40, mv=4)

# ------------------------------------------------------------------------------------------------------------------------------------ 

class Character:
    def __init__(self, spritesheet_path, num_frames, animation_speed=0.1):
        self.spritesheet = pygame.image.load(spritesheet_path)
        self.num_frames = num_frames
        self.frame_width = self.spritesheet.get_width() // num_frames 
        self.frame_height = self.spritesheet.get_height() # kad imas vise redova prosiri
        self.current_frame = 0
        self.animation_speed = animation_speed  # Adjust as needed
        self.animation_timer = 0
        self.frames_to_skip = 4 - num_frames

# ------------------------------------------------------------------------------------------------------------------------------------

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0
            if self.current_frame >= self.num_frames - self.frames_to_skip:
                self.current_frame = 0

# ------------------------------------------------------------------------------------------------------------------------------------

    def draw(self, surface, x, y, character_sprite_size):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.spritesheet.subsurface(frame_rect)
        resized_frame_surface = pygame.transform.scale(frame_surface, (character_sprite_size, character_sprite_size))
        surface.blit(resized_frame_surface, (x, y))

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

# ------------------------------------------------------------------------------------------------------------------------------------

####

# ------------------------------------------------------------------------------------------------------------------------------------

####

# ------------------------------------------------------------------------------------------------------------------------------------

    def half_tile(tile_size):
        tile_size_half = tile_size / 2
        return tile_size_half
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
