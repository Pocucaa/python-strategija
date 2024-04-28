import pygame  # Import the pygame module
from utilities1 import *
from CharacterUtilities import *


# Define the main function
def main():
    pygame.init()  # Initialize pygame
    # Calculate the number of rows based on the screen width and height
    screen_width = 1280  # Define the screen width
    screen_height = 720  # Define the screen height
    tile_size = 50 # Adjust the size of each tile as desired
    rows = int(screen_height // tile_size)
    window = pygame.display.set_mode((screen_width, screen_height))  # Set the window size
    play = True  # Flag to control the game loop
    
    clock = pygame.time.Clock()

    character_sprite = Character("assets/likovi/mumijalik_2.png", 5)
    character_sprite1 = Character("assets/likovi/crni_vitez_idle.png", 4, animation_speed=0.17)

    while play:  # Main game loop
        mouse_pos = pygame.mouse.get_pos()  # Get the mouse position

        dt = clock.tick(60) / 1000  # Convert milliseconds to second
        character_sprite.update(dt)
        character_sprite1.update(dt)
        for event in pygame.event.get():  # Iterate through events
            if event.type == pygame.QUIT:  # If the user clicks the close button
                play = False  # Exit the game loop

        # Redraw the window
        redraw(window, screen_width, screen_height, rows, mouse_pos, character_sprite, character_sprite1)

    pygame.quit()  # Quit pygame when the game loop ends

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly

    # magicni brojevi X

