import pygame, sys
from button import Button
from Fight import main


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/img/pozadina1.png")
BG = pygame.transform.scale(BG, (1280, 720))

brod = pygame.image.load("assets/img/brod.png")
scaled_brod = pygame.transform.scale(brod, (600, 600))

drvo1 = pygame.image.load("assets/img/drvo1.png")
scaled_drvo1 = pygame.transform.scale(drvo1, (200, 200))
drvo2 = pygame.image.load("assets/img/drvo2.png")
scaled_drvo2 = pygame.transform.scale(drvo2, (350, 350))
drvo3 = pygame.image.load("assets/img/drvo3.png")
scaled_drvo3 = pygame.transform.scale(drvo3, (370, 370))
scaled_drvo32 = pygame.transform.scale(drvo3, (175, 175))
drvo4 = pygame.image.load("assets/img/drvo4.png")
scaled_drvo4 = pygame.transform.scale(drvo4, (400, 400))

oblak1 = pygame.image.load("assets/img/oblak1.png")
oblak2 = pygame.image.load("assets/img/oblak2.png")
oblak3 = pygame.image.load("assets/img/oblak3.png")
scaled_oblak1 = pygame.transform.scale(oblak1, (280, 280))
scaled_oblak2 = pygame.transform.scale(oblak2, (300, 300))
scaled_oblak3 = pygame.transform.scale(oblak3, (320, 320))

pygame.mixer.music.load('assets/music/Saban.mp3')
pygame.mixer.music.play(-1)  # -1 plays the music on loop

logo = pygame.image.load("assets/img/brod.png")
logo_rect = logo.get_rect(center=(1280 // 2, 720 // 2))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to get the desired font from a TTF file
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    # pygame.mixer.music.load('assets/music/Stoja.mp3')
    # pygame.mixer.music.play(-1)  # -1 plays the music on loop     -- muzika --
    
    # Loop until the user exits
    while True:
        # Get the current mouse position
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # Fill the screen with black
        SCREEN.fill("black")
        # Render the play text
        PLAY_TEXT = get_font(45).render("NE MOZEEEEE", True, "White")
        # Get the rectangle that encloses the rendered text
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # Blit (draw) the play text onto the screen
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        # Create the "BACK" button
        PLAY_BACK = Button(image=None, pos=(640, 460))
        # Change the color of the "BACK" button based on mouse interaction
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # Update the appearance of the "BACK" button on the screen
        PLAY_BACK.update(SCREEN)
        # Event handling loop
        for event in pygame.event.get():
            # Check if the user wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if the "BACK" button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    # Return to the main menu
                    main_menu()
        # Update the display
        pygame.display.update()

# Function for the "Options" screen (similar structure to "play" function)
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(35).render("Jedina opcija je da se ubijes", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        # Create the "BACK" button
        OPTIONS_BACK = Button(image=None, pos=(640, 460))
        
        # Update and display the "BACK" button
        OPTIONS_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        
        pygame.display.update()


def update_cloud_positions():
    global oblak_x1, oblak_x2, oblak_x3, oblak_x4, oblak_x5, oblak_x6
    
    oblak_x1 -= 1 
    if oblak_x1 < -300:  
        oblak_x1 = 1280

    oblak_x2 -= 2
    if oblak_x2 < -300:  
        oblak_x2 = 1480

    oblak_x3 -= 3
    if oblak_x3 < -300:  
        oblak_x3 = 1880

    oblak_x4 -= 0.5
    if oblak_x4 < -300:  
        oblak_x4 = 1780

    oblak_x5 -= 2  
    if oblak_x5 < -300:  
        oblak_x5 = 1520

    oblak_x6 -= 2  
    if oblak_x6 < -300:  
        oblak_x6 = 1920

def render_screen():
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(scaled_oblak2, (230, 120)) 
    SCREEN.blit(oblak1, (210, 70))
    SCREEN.blit(oblak3, (330, 50)) 
    SCREEN.blit(oblak2, (600, 90))  
    SCREEN.blit(scaled_oblak1, (370, 20)) 

    SCREEN.blit(scaled_oblak1, (oblak_x2, 180))  
    SCREEN.blit(scaled_oblak2, (oblak_x1, 70))  
    SCREEN.blit(scaled_oblak3, (oblak_x3, 120))
    SCREEN.blit(scaled_oblak1, (oblak_x4, 180))  
    SCREEN.blit(scaled_oblak2, (oblak_x5, 70))  
    SCREEN.blit(scaled_oblak3, (oblak_x6, 120))      
    SCREEN.blit(oblak1, (oblak_x2, 70))  

    SCREEN.blit(brod, (640, 30))  

    SCREEN.blit(scaled_oblak1, (oblak_x2, 220))  
    SCREEN.blit(scaled_oblak3, (oblak_x3, 70))  
    SCREEN.blit(scaled_oblak1, (oblak_x4, -110))  


    SCREEN.blit(scaled_drvo1, (230, 540))  
    SCREEN.blit(drvo2, (320, 630))  
    SCREEN.blit(scaled_drvo32, (370, 550))  
    SCREEN.blit(scaled_drvo2, (440, 380))
    SCREEN.blit(scaled_drvo32, (600, 550))  
    SCREEN.blit(drvo4, (600, 630))  
    SCREEN.blit(drvo4, (670, 630))  
    SCREEN.blit(scaled_drvo1, (670, 540))  
    SCREEN.blit(scaled_drvo4, (680, 320))             
    SCREEN.blit(drvo2, (780, 630))  
    SCREEN.blit(scaled_drvo3, (880, 350))
    SCREEN.blit(drvo1, (970, 280)) 

def start_screen():
    # Variables for animation
    flash_count = 0
    fade_alpha = 0

    # Main loop for start screen
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        SCREEN.blit(BG, (0, 0))

        # Flash logo
        if flash_count < 20:
            SCREEN.blit(logo, logo_rect)
            flash_count += 1
            MENU_TEXT = get_font(40).render("pečurka and počuča prodakšn :)", True, "#FF4500")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 620))
            SCREEN.blit(MENU_TEXT, MENU_RECT)
        else:
            # Fade out
            fade_surface = pygame.Surface((1280, 720))
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(fade_alpha)
            SCREEN.blit(fade_surface, (0, 0))
            fade_alpha += 7
            if fade_alpha > 255:
                # Transition to main game
                running = False

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(10)

def main_menu():
    global oblak_x1, oblak_x2, oblak_x3, oblak_x4, oblak_x5, oblak_x6
    
    oblak_x1 = 1280 # Initial x-coordinate of the image
    oblak_x2 = 1880
    oblak_x3 = 1280 # Initial x-coordinate of the image
    oblak_x4 = 720
    oblak_x5 = 980 # Initial x-coordinate of the image
    oblak_x6 = 460 # Initial x-coordinate of the image
    
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        update_cloud_positions()  # Update cloud positions
        
        render_screen()  # Render the screen

        MENU_TEXT = get_font(40).render("Insert ime igrice ovde", True, "#FF0000")
        MENU_RECT = MENU_TEXT.get_rect(center=(480, 40))
        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/img/title_start.png"), pos=(170, 170), scale_factor=1.8)
        UPGRADE_BUTTON = Button(image=pygame.image.load("assets/img/title_unapredjenja.png"), pos=(170, 320), scale_factor=2.7)
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/img/title_opcije.png"), pos=(170, 470), scale_factor=1.8)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/img/title_izlaz.png"), pos=(170, 620), scale_factor=2.7)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, UPGRADE_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # Update the display
        pygame.display.update()

start_screen()
# Start the main menu
main_menu()


