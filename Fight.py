import pygame  # Import the pygame module
from FightUtilities import *

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
# Define the main function
def main():
    pygame.init()  # Initialize pygame
    screen_width = 1280  # Define the screen width
    screen_height = 720  # Define the screen height
    tile_size = 25 # Adjust the size of each tile as desired
    # Calculate the number of rows based on the screen width and height
    rows = int(screen_height // tile_size)
    window = pygame.display.set_mode((screen_width, screen_height))  # Set the window size
    play = True  # Flag to control the game loop
    
    clock = pygame.time.Clock()
    # Load the image and scale it to fit the top of the window
    image = pygame.image.load("assets/img/pozadina1.png")
    image = pygame.transform.scale(image, (screen_width, int(screen_height * 0.15)))

    # Load the image and scale it to fit the left side of the window
    image2 = pygame.image.load("assets/img/pozadina.png")
    image2 = pygame.transform.scale(image2, (int(screen_width * 0.15), screen_height - int(screen_height * 0.15)))

    # Load the image and scale it to fit the right side of the window
    image3 = pygame.image.load("assets/img/pozadina.png")
    image3 = pygame.transform.scale(image3, (int(screen_width * 0.15), screen_height - int(screen_height * 0.15)))

    character_sprite = Character("assets/likovi/mumijalik_2.png", 5)
    character_sprite1 = Character("assets/likovi/crni_vitez_idle.png", 4, animation_speed=0.17)

    while play:  # Main game loop
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = [mouse_x, mouse_y]

        for event in pygame.event.get():  # Iterate through events
            if event.type == pygame.QUIT:  # If the user clicks the close button
                play = False  # Exit the game loop

        # Check if the mouse is on any of the characters
        # onClickMove(mouse_x, mouse_y, character_position, character_position1)s

        dt = clock.tick(60) / 1000  # Convert milliseconds to second
        character_sprite.update(dt)
        character_sprite1.update(dt)

        # Redraw the window
        redraw(window, screen_width, screen_height, rows, mouse_pos, image, image2, image3, character_sprite, character_sprite1)

    pygame.quit()  # Quit pygame when the game loop ends

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly

    # magicni brojevi X












def FIGHT():

    STARTpassive

    ONHITpassive

    ENDpassive