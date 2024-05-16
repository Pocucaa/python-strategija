import pygame

character_position = (310, 215)
character_position1 = (110, 215)

frejm = pygame.image.load("assets/img/frejm.png")
scaled_frejm = pygame.transform.scale(frejm, (80, 80))
dugme_L = pygame.image.load("assets/img/dugme_L.png")
# scaled_dugme_L = pygame.transform.scale(dugme_L, (200, 200))
dugme_R = pygame.image.load("assets/img/dugme_R.png")
# scaled_dugme_R = pygame.transform.scale(dugme_R, (200, 200))
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

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

# Define a function to redraw the window
def redraw(window, width, height, rows, character_sprite, character_sprite1):
    window.fill((255, 255, 255))  # Fill the window with white color
    
    # Draw the background image
    BG = pygame.image.load("assets/img/pozadina.png")
    BG = pygame.transform.scale(BG, (1280, 720))
    window.blit(BG, (0, 0))
    MERC_TEXT = get_font(35).render("Select your starting army", True, "Black")
    window.blit(MERC_TEXT, (40, 130))
    ITEM_TEXT = get_font(35).render("Select your starting items", True, "Black")
    window.blit(ITEM_TEXT, (40, 430))
    # Calculate the position to blit the character sprite
    tile_size = int((height - height * 0.15) // rows)
    character_sprite_size = int(tile_size * 1.3)
    character_sprite_size1 = int(tile_size * 1.3)
# ---------------------------------------------------------------------------------------- merc
    window.blit(scaled_frejm, (100, 200))
    window.blit(dugme_L, (60, 230))
    window.blit(dugme_R, (190, 230))

    window.blit(scaled_frejm, (300, 200))
    window.blit(dugme_L, (260, 230))
    window.blit(dugme_R, (390, 230))

    window.blit(scaled_frejm, (500, 200))
    window.blit(dugme_L, (460, 230))
    window.blit(dugme_R, (590, 230))
# ---------------------------------------------------------------------------------------- items
    window.blit(scaled_frejm, (100, 500))
    window.blit(dugme_L, (60, 530))
    window.blit(dugme_R, (190, 530))

    window.blit(scaled_frejm, (300, 500))
    window.blit(dugme_L, (260, 530))
    window.blit(dugme_R, (390, 530))

    window.blit(scaled_frejm, (500, 500))
    window.blit(dugme_L, (460, 530))
    window.blit(dugme_R, (590, 530))
# ----------------------------------------------------------------------------------------
    # Blit the character sprite onto the window
    character_sprite.draw(window, character_position[0], character_position[1], character_sprite_size)
    character_sprite1.draw(window, character_position1[0], character_position1[1], character_sprite_size1)

    pygame.display.update()  # Update the display
