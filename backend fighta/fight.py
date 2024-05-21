import pygame, sys
from CharacterUtilities import *

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

# Custom print function
output_lines = []

def custom_print(*args, **kwargs):
    text = ' '.join(map(str, args))
    output_lines.append(text)
    if len(output_lines) > 200:  # Keep only the last 20 lines
        output_lines.pop(0)

# Replace the built-in print with the custom print
print = custom_print

# Function to render text on the Pygame window
def render_text(surface):
    surface.fill(background_color)
    y_offset = 10
    for line in output_lines:
        text_surface = font.render(line, True, text_color)
        surface.blit(text_surface, (10, y_offset))
        y_offset += 40

# Main loop
running = True
clock = pygame.time.Clock()

print("This is a test print statement.")
print("Another line to display.")
print("Hello, Pygame!")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    render_text(screen)
    clock.tick(60)

    
    pygame.display.flip()

pygame.quit()
sys.exit()
