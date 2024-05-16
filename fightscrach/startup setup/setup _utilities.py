import pygame

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



character_position = [190, 170]
character_position1 = [390, 180]

def pozadina(window, width, height, top_zone, left_zone):
# ------------------------------------------------------------------------------------------------------------------------------------ setup
    top_image = pygame.image.load("assets/img/pozadina1.png")                                                            
    top_image = pygame.transform.scale(top_image, (width, top_zone))

    left_image = pygame.image.load("assets/img/pozadina.png")
    left_image = pygame.transform.scale(left_image, (left_zone, height - top_zone))    

    right_image = pygame.image.load("assets/img/pozadina.png")
    right_image = pygame.transform.scale(right_image, (left_zone, height - top_zone))    

    interactive_screen = pygame.image.load("assets/img/opcija1.jpg")
    interactive_screen = pygame.transform.scale(interactive_screen, (width, top_zone))   

    offsetX = 5
# ------------------------------------------------------------------------------------------------------------------------------------ print
    window.fill((255, 255, 255)) 
    window.blit(top_image, (0, 0))
    window.blit(left_image, (0, top_zone))
    window.blit(right_image, (width + offsetX - left_zone, top_zone))
    # window.blit(interactive_screen, (0, height - top_zone))
# ------------------------------------------------------------------------------------------------------------------------------------ 

def grid(window, width, height, rows, mouse_pos, top_zone, left_zone, tile_size):
    offsetX = 5
    distance_between_rows = tile_size
    # Draw vertical grid lines
    for x in range(left_zone, width - left_zone, distance_between_rows):
        if x != 0 and x != int(width) - left_zone and x != left_zone:
            pygame.draw.line(window, (0, 0, 0), (x, top_zone), (x, height))
    # Draw horizontal grid lines
    for y in range(top_zone, height, distance_between_rows):
        if y != 0 and y != height - top_zone and y != top_zone:
            pygame.draw.line(window, (0, 0, 0), (left_zone, y), (width - left_zone + offsetX, y))

def redraw(window, width, height, rows, mouse_pos, character_sprite, character_sprite1, top_zone, left_zone, tile_size):
    window.fill((0, 0, 0)) 
    pozadina(window, width, height, top_zone, left_zone)
    grid(window, width, height, rows, mouse_pos, top_zone, left_zone, tile_size)
    

    # Calculate the position to blit the character sprite
    character_sprite_size = int(tile_size * 4)
    character_sprite_size1 = int(tile_size * 5)

    mouse_tile_x = (mouse_pos[0] - left_zone) // tile_size
    mouse_tile_y = (mouse_pos[1] - top_zone) // tile_size

    # Blit the character sprite onto the window

    character_sprite.draw(window, character_position[0], character_position[1], character_sprite_size)
    character_sprite1.draw(window, character_position1[0], character_position1[1], character_sprite_size1)

    # Check if the mouse position is within the boundaries of the tiles and make it glow
    if 0 <= mouse_tile_x < width and 0 <= mouse_tile_y < rows:
        if mouse_pos[0] < width - left_zone:
            rect = pygame.Rect(left_zone + mouse_tile_x * tile_size, top_zone + mouse_tile_y * tile_size, tile_size, tile_size)
            pygame.draw.rect(window, (255, 0, 0), rect, 3)

    pygame.display.update()  # Update the display
