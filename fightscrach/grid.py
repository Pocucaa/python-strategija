import pygame, sys
from utilities import *
from CharacterUtilities import *


clock = pygame.time.Clock()
dt = clock.tick(60) / 1000  # Convert milliseconds to second /// promeniti mozda na milisekunde zbog laga, videcemo

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
def redraw(window, width, height, rows, mouse_pos,  mumija_idle, vitez_idle, vitez_setnja, top_zone, left_zone, tile_size):
    pozadina(width, height, top_zone, left_zone)
    grid(window, width, height, rows, mouse_pos, top_zone, left_zone, tile_size)
    interactive_screen(window, width, height, top_zone)    # dodati da ne svetli ovde

    character_position = [
        left_zone + (tile_size / 20),
        top_zone + (tile_size / 2) + 15 + tile_size
    ]
    character_position1 = [
        left_zone + (tile_size / 20),
        top_zone + 5 * (tile_size / 2) +15             # za 2 se pomera tajl
    ]

    mumija_idle_size = int(tile_size * 1.1)
    vitez_idle_size = int(tile_size * 1.2)

    mouse_tile_x = (mouse_pos[0] - left_zone) // tile_size
    mouse_tile_y = (mouse_pos[1] - top_zone) // tile_size

    mumija_idle.draw(window, character_position[0], character_position[1], mumija_idle_size)
    # vitez_idle.draw(window, character_position1[0], character_position1[1], vitez_idle_size)


    is_walking = False  # Initialize flag
    walking_distance = 0  # Initialize walking distance

    if character_position[0] - 15 < mouse_pos[0] < character_position[0] + 15:
        is_walking = True  # Set flag to True when walking condition is met
        while walking_distance < 2 * tile_size:  # Loop until desired distance is reached
            direction = "right"  # Assuming movement is right for this example
            walking_speed = 15  # Adjust walking speed as needed

            # Update character position based on direction and speed
            character_position1[0] += walking_speed if direction == "right" else -walking_speed  # Handle left movement if needed

            # Update walking distance
            walking_distance += walking_speed
            vitez_setnja.draw(window, character_position1[0], character_position1[1], vitez_idle_size)

    else:
        is_walking = False  # Set flag to False when not walking


    # Draw based on the flag
    if is_walking:
        vitez_setnja.draw(window, character_position1[0], character_position1[1], vitez_idle_size)
        vitez_setnja.update(dt)
    else:
        vitez_idle.draw(window, character_position1[0], character_position1[1], vitez_idle_size)  # Use character_position for idle state





# ------------------------------------------------------------------------------------------------------------------------------------ 
    offsetY = 5
    # Check if the mouse position is within the boundaries of the tiles and make it glow
    if 0 <= mouse_tile_x < width and 0 <= mouse_tile_y < rows:
        if top_zone < mouse_pos[1] < height - top_zone - offsetY and top_zone < mouse_pos[1]:
            if 0 < mouse_pos[0] < width - left_zone:
                rect = pygame.Rect(left_zone + mouse_tile_x * tile_size, top_zone + mouse_tile_y * tile_size, tile_size, tile_size)
                pygame.draw.rect(window, (255, 0, 0), rect, 3)

    pygame.display.update()  # Update the display
# ------------------------------------------------------------------------------------------------------------------------------------ 