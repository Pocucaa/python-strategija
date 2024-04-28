import pygame

character_position = (190, 170)
character_position1 = (390, 180)

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

mercenary1 = Mercenary(hp=120, at=15, mana=40, mv=6)
mercenary2 = Mercenary(hp=90, at=12, mana=60, mv=4)

class Character:
    def __init__(self, spritesheet_path, num_frames, animation_speed=0.1):
        self.spritesheet = pygame.image.load(spritesheet_path)
        self.num_frames = num_frames
        self.frame_width = self.spritesheet.get_width() // num_frames
        self.frame_height = self.spritesheet.get_height()
        self.current_frame = 0
        self.animation_speed = animation_speed  # Adjust as needed
        self.animation_timer = 0
        self.frames_to_skip = 5 - num_frames
    
    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0
            if self.current_frame >= self.num_frames - self.frames_to_skip:
                self.current_frame = 0

    
    def draw(self, surface, x, y, character_sprite_size):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.spritesheet.subsurface(frame_rect)
        resized_frame_surface = pygame.transform.scale(frame_surface, (character_sprite_size, character_sprite_size))
        surface.blit(resized_frame_surface, (x, y))

        # Define a function to draw a grid
def grid(window, width, height, rows, mouse_pos, start_x, start_y):
    # Calculate the distance between rows
    distance_between_rows = int((height - height * 0.15) // rows)
    # Define the width for the left side (equivalent to 4 tiles)
    left_width = int(width * 0.15)
    # Draw vertical grid lines for the left side
    for x in range(start_x, left_width, distance_between_rows):
            pygame.draw.line(window, (0, 0, 0), (x, height * 0.15), (x, height))
    # Draw horizontal grid lines for the left side
    for y in range(start_y, height, distance_between_rows):
        if y != 0:
            pygame.draw.line(window, (0, 0, 0), (0, y), (left_width, y))


# Define a function to redraw the window
def redraw(window, width, height, rows, mouse_pos, image, image2, image3, character_sprite, character_sprite1):
    window.fill((255, 255, 255))  # Fill the window with white color

    # Draw the image at the top of the window
    window.blit(image, (0, 0))
    # Draw the image on the left side
    window.blit(image2, (0, int(height * 0.15)))
    # Draw the image on the right side
    window.blit(image3, (width - int(width * 0.145), int(height * 0.15)))
    
    left_inactive_percent = 0.15
    top_inactive_percent = 0.15

    left_inactive_zone = width * left_inactive_percent
    top_inactive_zone = height * top_inactive_percent

    grid_offset_x = 0
    grid_offset_y = int(top_inactive_zone)

    # Draw the grid
    grid(window, width, height, rows, mouse_pos, grid_offset_x, grid_offset_y)

    # Calculate the position to blit the character sprite
    tile_size = int((height - height * 0.15) // rows)

    character_sprite_size = int(tile_size * 1.3)
    character_sprite_size1 = int(tile_size * 2)

    offset_x = grid_offset_x % tile_size
    offset_y = grid_offset_y % tile_size

    mouse_tile_x = (mouse_pos[0] - offset_x) // tile_size
    mouse_tile_y = (mouse_pos[1] - offset_y) // tile_size

    # Blit the character sprite onto the window

    character_sprite.draw(window, character_position[0], character_position[1], character_sprite_size)
    character_sprite1.draw(window, character_position1[0], character_position1[1], character_sprite_size1)

    # Check if the mouse position is within the boundaries of the left side tiles and make it glow
    if int(width - left_inactive_percent)> mouse_pos[0] < left_inactive_zone - (tile_size / 2) and mouse_pos[1] > top_inactive_percent:
        rect = pygame.Rect(offset_x + mouse_tile_x * tile_size, offset_y + mouse_tile_y * tile_size, tile_size, tile_size)
        pygame.draw.rect(window, (255, 0, 0), rect, 3)
    pygame.display.update()  # Update the display