import pygame
from grid import *
from utilities import *

character_position = [190, 170]
character_position1 = [390, 180]

def main():
    pygame.init()                                                                                
    screen_width = 1280                                                                          
    screen_height = 720    
    window = pygame.display.set_mode((screen_width, screen_height))     
# ------------------------------------------------------------------------------------------------------------------------------------                                               
    play = True                                                                                    
    clock = pygame.time.Clock()

    top_inactive_precent = 0.15
    left_inactive_precent = 0.15

    top_inactive_zone = int(screen_height * top_inactive_precent)
    left_inactive_zone = int(screen_width * left_inactive_precent)

    tile_size = 25 # 25                                                                   
    rows = int(screen_height - top_inactive_zone // tile_size)      

    character_sprite = Character("assets/likovi/mumijalik_2.png", 5)
    character_sprite1 = Character("assets/likovi/crni_vitez_idle.png", 4, animation_speed=0.17)

    while play:                                                          
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = [mouse_x, mouse_y]

        for event in pygame.event.get():                                
            if event.type == pygame.QUIT:                              
                play = False                                            

        dt = clock.tick(60) / 1000  # Convert milliseconds to second



        redraw(window, screen_width, screen_height, rows, mouse_pos, character_sprite, character_sprite1, top_inactive_zone, left_inactive_zone, tile_size)

        character_sprite.update(dt)
        character_sprite1.update(dt)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
