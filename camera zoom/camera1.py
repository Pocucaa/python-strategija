import pygame, sys  # Import the pygame library for game development and sys module for system-specific parameters and functions
from random import randint  # Import the randint function from the random module


# Define a class for managing a group of sprites with a camera
class CameraGroup(pygame.sprite.Group):
    def __init__(self):  # Constructor method, initializes the CameraGroup object
        super().__init__()  # Call the superclass constructor
        self.display_surface = pygame.display.get_surface()  # Get the display surface where the game is rendered

        # Camera offset and borders setup
        self.offset = pygame.math.Vector2()  # Create a vector to store the camera offset
        self.half_w = self.display_surface.get_size()[0] // 2  # Get half of the display width
        self.half_h = self.display_surface.get_size()[1] // 2  # Get half of the display height
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}  # Define borders for the camera view

        # Camera rectangle setup
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)  # Create a rectangle representing the camera view

        # Ground setup
        self.ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()  # Load the ground image with transparency
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))  # Get the rectangle that encloses the ground image and set its top-left position

        # Camera movement speed
        self.keyboard_speed = 20  # Set the speed for keyboard-controlled camera movement

        # Zoom setup
        self.zoom_scale = 1  # Set the initial zoom scale
        self.internal_surf_size = (2500,2500)  # Set the size of the internal surface for rendering
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)  # Create an internal surface for rendering with alpha channel
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))  # Get the rectangle that encloses the internal surface and set its center position
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)  # Create a vector to store the size of the internal surface
        self.internal_offset = pygame.math.Vector2()  # Create a vector to store the internal offset

    # Method to control the camera movement using keyboard input
    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.camera_rect.x -= self.keyboard_speed
        if keys[pygame.K_d]: self.camera_rect.x += self.keyboard_speed
        if keys[pygame.K_w]: self.camera_rect.y -= self.keyboard_speed
        if keys[pygame.K_s]: self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    # Method to control the camera zoom using keyboard input
    def zoom_keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.zoom_scale += 0.1
        if keys[pygame.K_e]:
            self.zoom_scale -= 0.1

    # Method to draw the scene with custom camera settings
    def custom_draw(self,player):
        
        # Call methods to control camera movement and zoom
        self.mouse_control()
        self.zoom_keyboard_control()

        # Clear the internal surface with a sky blue color
        self.internal_surf.fill('#71ddee')

        # Draw the ground
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.ground_surf,ground_offset)

        # Draw active elements sorted by y-coordinate
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image,offset_pos)

        # Scale the internal surface based on zoom scale
        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))

        # Blit the scaled surface onto the display surface
        self.display_surface.blit(scaled_surf,scaled_rect)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))  # Set up the display surface
clock = pygame.time.Clock()  # Create a Clock object for controlling the frame rate
pygame.event.set_grab(True)  # Grab the mouse cursor

# Create instances of CameraGroup and Player
camera_group = CameraGroup()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEWHEEL:
            camera_group.zoom_scale += event.y * 0.03

    screen.fill('#71ddee')  # Fill the screen with a sky blue color

    camera_group.update()  # Update the camera

    pygame.display.update()  # Update the display
    clock.tick(60)  # Cap the frame rate at 60 frames per second
