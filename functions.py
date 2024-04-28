import pygame
from CharacterUtilities import *
from FightUtilities import Character, get_character_tile

def MercCoordinates(height, rows):
    # Inside the redraw function
    tile_size = 50  # Assuming the tile size is 50

    # Calculate the tile indices for the character position
    character_tile_x = character_position[0] // tile_size
    character_tile_y = character_position[1] // tile_size

    # Calculate the tile indices for the character1 position
    character_tile_x1 = character_position1[0] // tile_size
    character_tile_y1 = character_position1[1] // tile_size

    return (character_tile_x, character_tile_y), (character_tile_x1, character_tile_y1)

def is_mouse_on_character(mouse_x, mouse_y, character_tile):
    tile_size = 50
    # Check if the mouse coordinates match the character's tile
    return (mouse_x // tile_size, mouse_y // tile_size) == character_tile

def onClickMove(mouse_x, mouse_y, character_position, character_tile):
    tile_size = 50
    # Check if the mouse is on the character's tile
    if is_mouse_on_character(mouse_x, mouse_y, character_tile):
        # Lock the character to the mouse position
        character_position[0] = mouse_x
        character_position[1] = mouse_y
    else:
        # Move the character to the clicked tile
        character_position[0] = mouse_x // tile_size * tile_size
        character_position[1] = mouse_y // tile_size * tile_size









# def findNerest ():

# def random():

# def attack():

# def zoom?
