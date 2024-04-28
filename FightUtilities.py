import pygame
from CharacterUtilities import *

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

    def get_character_tile(character_position, tile_size):
        character_tile_x = character_position[0] // tile_size
        character_tile_y = character_position[1] // tile_size
        return character_tile_x, character_tile_y




        # Define a function to draw a grid
def grid(window, width, height, rows, mouse_pos):
    # Calculate the distance between rows
    distance_between_rows = int((height - height * 0.15) // rows)
    # Draw vertical grid lines
    for x in range(int(width * 0.15), int(width - width * 0.15), distance_between_rows):
        # Skip drawing grid lines where images are inserted
        if x != 0 and x != int(width) - int(width * 0.15) and x != int(width * 0.15):
            pygame.draw.line(window, (0, 0, 0), (x, height * 0.15), (x, height))
    # Draw horizontal grid lines
    for y in range(int(height * 0.15), height, distance_between_rows):
        if y != 0 and y != height - int(height * 0.15) and y != int(height * 0.15):
            pygame.draw.line(window, (0, 0, 0), (int(width * 0.15), y), (int(width - width * 0.145), y))

# Define a function to redraw the window
def redraw(window, width, height, rows, mouse_pos, image, image2, image3, character_sprite, character_sprite1):
    window.fill((255, 255, 255))  # Fill the window with white color
    # Draw the image at the top of the window
    window.blit(image, (0, 0))
    # Draw the image on the left side
    window.blit(image2, (0, int(height * 0.15)))
    # Draw the image on the right side
    window.blit(image3, (width - int(width * 0.145), int(height * 0.15)))
    # Draw the grid
    grid(window, width, height, rows, mouse_pos)

    # Calculate the position to blit the character sprite
    tile_size = int((height - height * 0.15) // rows)
    character_sprite_size = int(tile_size * 1.3)
    character_sprite_size1 = int(tile_size * 2)

    mouse_tile_x = (mouse_pos[0] - int(width * 0.15)) // tile_size
    mouse_tile_y = (mouse_pos[1] - int(height * 0.15)) // tile_size

    # Blit the character sprite onto the window

    character_sprite.draw(window, character_position[0], character_position[1], character_sprite_size)
    character_sprite1.draw(window, character_position1[0], character_position1[1], character_sprite_size1)

    # Check if the mouse position is within the boundaries of the tiles and make it glow
    if 0 <= mouse_tile_x < width and 0 <= mouse_tile_y < rows:
        if mouse_pos[0] < width - int(width * 0.147):
            rect = pygame.Rect(int(width * 0.15) + mouse_tile_x * tile_size, int(height * 0.15) + mouse_tile_y * tile_size, tile_size, tile_size)
            pygame.draw.rect(window, (255, 0, 0), rect, 3)

    pygame.display.update()  # Update the display