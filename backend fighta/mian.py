import pygame, sys
from fightt import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Custom Print Display")

# Set up font
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
background_color = (0, 0, 0)
# -----------------------------------------------

# Main loop
running = True
clock = pygame.time.Clock()

print("This is a test print statement.")
print("Another line to display.")
print("Hello, Pygame!")

# -----------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

# -----------------------------------------------
    action = 3
    Fight_start(player_team, enemy_team, action)
    break
    
# -----------------------------------------------
    pygame.display.flip()

pygame.quit()
sys.exit()
