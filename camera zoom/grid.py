import pygame
from utilities import *
from CharacterUtilities import Character


# ------------------------------------------------------------------------------------------------------------------------------------ 
def interactive_screen(window, width, height, top_zone):

    interactive_screen = pygame.image.load("assets/img/opcija1.jpg")
    interactive_screen = pygame.transform.scale(interactive_screen, (width, top_zone))   

    window.blit(interactive_screen, (0, height - top_zone))
# ------------------------------------------------------------------------------------------------------------------------------------ 
def pozadina(width, height, top_zone, left_zone):
    window = pygame.display.get_surface()  # Get the display surface where the game is rendered
    top_image = pygame.image.load("assets/img/pozadina1.png")                                                            
    top_image = pygame.transform.scale(top_image, (width, top_zone))

    left_image = pygame.image.load("assets/img/pozadina.png")
    left_image = pygame.transform.scale(left_image, (left_zone, height - top_zone))    

    right_image = pygame.image.load("assets/img/pozadina.png")
    right_image = pygame.transform.scale(right_image, (left_zone, height - top_zone))    

    offsetX = 5
# ------------------------------------------------------------------------
    window.fill((255, 255, 255)) 
    window.blit(top_image, (0, 0))
    window.blit(left_image, (0, top_zone))
    window.blit(right_image, (width + offsetX - left_zone, top_zone))
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
# ------------------------------------------------------------------------------------------------------------------------------------ 
def redraw(window, width, height, rows, mouse_pos,  mumija_idle, vitez_idle, top_zone, left_zone, tile_size):
    pozadina(width, height, top_zone, left_zone)
    grid(window, width, height, rows, mouse_pos, top_zone, left_zone, tile_size)
    interactive_screen(window, width, height, top_zone)    # dodati da ne svetli ovde

    character_position = [
        left_zone + vitez_idle.frame_width,
        top_zone + (tile_size / 2)
    ]
    character_position1 = [
        left_zone + (tile_size / 20),
        top_zone + 5 * (tile_size / 2)              # za 2 se pomera tajl
    ]

    # Calculate the position to blit the character sprite
    mumija_idle_size = int(tile_size * 1.1)
    vitez_idle_size = int(tile_size * 1.2)

    mouse_tile_x = (mouse_pos[0] - left_zone) // tile_size
    mouse_tile_y = (mouse_pos[1] - top_zone) // tile_size

    mumija_idle.draw(window, character_position[0], character_position[1], mumija_idle_size)
    vitez_idle.draw(window, character_position1[0], character_position1[1], vitez_idle_size)

    offsetY = 5
    # Check if the mouse position is within the boundaries of the tiles and make it glow
    if 0 <= mouse_tile_x < width and 0 <= mouse_tile_y < rows:
        if top_zone < mouse_pos[1] < height - top_zone - offsetY and top_zone < mouse_pos[1]:
            if 0 < mouse_pos[0] < width - left_zone:
                rect = pygame.Rect(left_zone + mouse_tile_x * tile_size, top_zone + mouse_tile_y * tile_size, tile_size, tile_size)
                pygame.draw.rect(window, (255, 0, 0), rect, 3)

    pygame.display.update()  # Update the display
# ------------------------------------------------------------------------------------------------------------------------------------ 