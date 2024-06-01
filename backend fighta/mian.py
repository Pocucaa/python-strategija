import pygame, sys
from fightt import *

# import ilkj

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tatakae")

# Set up font
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
background_color = (0, 0, 0)
# -----------------------------------------------

# Main loop
running = True
clock = pygame.time.Clock()

action_keys = {
    pygame.K_a: 1,  # Attack (action = 1)
    pygame.K_s: 2,  # Defend (action = 2)
    pygame.K_d: 4,  # Spell (action = 4)
    # You can add more keys for other actions
}

player_team = []
enemy_team = []
action = None
# -----------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in action_keys:
                action = action_keys[event.key]

    # Execute action based on chosen action (assuming you implemented Fight_start)
    if action is not None:
        Fight_start(player_team, enemy_team, action)
        action = None  # Reset action for next input

    clock.tick(60)

    clock.tick(60)

# -----------------------------------------------

    pygame.display.flip()

pygame.quit()
sys.exit()
