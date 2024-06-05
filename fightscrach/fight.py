import pygame, sys
from grid import *
from utilities import *
from CharacterUtilities import *


#!!!!!!!!!!!!!!!!!!!! promenjeni fajlovi: ideje, dev_notes, informacije, fight ( informacije u fajlovima )

def main():
    pygame.init()                                                                                
    screen_width = 1280                                                                          
    screen_height = 720    
    window = pygame.display.set_mode((screen_width, screen_height))     
    pygame.event.set_grab(True)  # Grab the mouse cursor
# ------------------------------------------------------------------------------------------------------------------------------------  setup                                          
    play = True                                                                                    
    clock = pygame.time.Clock()

    top_inactive_precent = 0.15
    left_inactive_precent = 0.15

    top_inactive_zone = int(screen_height * top_inactive_precent)
    left_inactive_zone = int(screen_width * left_inactive_precent)

    tile_size = 50 # radi na 20 i 50 i 25                                                             
    rows = int(screen_height - top_inactive_zone // tile_size)      

    mumija_idle = Character("assets/likovi/mumijalik_2.png", 5)
    vitez_idle = Character("assets/likovi/crni_vitez_idle.png", 4, animation_speed=0.2)
    vitez_setnja = Character("assets/likovi/crni_vitez_walk.png", 6, animation_speed=0.1)
    vitez_sprites = [vitez_idle, vitez_setnja]
# ------------------------------------------------------------------------------------------------------------------------------------


# Create instances of CameraGroup and Player

    # camera_group = CameraGroup()



# ------------------------------------------------------------------------------------------------------------------------------------  start 
    while play:                                                          
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = [mouse_x, mouse_y]

        for event in pygame.event.get():                                
            if event.type == pygame.QUIT:                              
                play = False          

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # if event.type == pygame.MOUSEWHEEL:
        #     camera_group.zoom_scale += event.y * 0.03   
        #     if camera_group.zoom_scale >= 3:
        #         camera_group.zoom_scale = 3
        #     if camera_group.zoom_scale <= 0.1:
        #         camera_group.zoom_scale = 0.1                                 

        dt = clock.tick(60) / 1000  # Convert milliseconds to second /// promeniti mozda na milisekunde zbog laga, videcemo

        redraw(window, screen_width, screen_height, rows, mouse_pos, mumija_idle, vitez_idle, vitez_setnja, top_inactive_zone, left_inactive_zone, tile_size)

        mumija_idle.update(dt)
        vitez_idle.update(dt)
        vitez_setnja.update(dt)
        # camera_group.update()  # Update the camera
        # camera_group.custom_draw(window)  # Draw the scene with custom camera settings

# ------------------------------------------------------------------------------------------------------------------------------------        





# ------------------------------------------------------------------------------------------------------------------------------------        
        # Update the display
        pygame.display.update()

    # pygame.quit()

if __name__ == "__main__":
    main()
