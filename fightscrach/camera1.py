import pygame, sys  # Import the pygame library for game development and sys module for system-specific parameters and functions
from random import randint  # Import the randint function from the random module

# Define a class for the Tree sprite
class Tree(pygame.sprite.Sprite):
    def __init__(self,pos,group):  # Constructor method, initializes the Tree object
        super().__init__(group)  # Call the superclass constructor
        self.image = pygame.image.load('graphics/tree.png').convert_alpha()  # Load the tree image with transparency
        self.rect = self.image.get_rect(topleft = pos)  # Get the rectangle that encloses the image and set its top-left position

# Define a class for the Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):  # Constructor method, initializes the Player object
        super().__init__(group)  # Call the superclass constructor
        self.image = pygame.image.load('graphics/player.png').convert_alpha()  # Load the player image with transparency
        self.rect = self.image.get_rect(center = pos)  # Get the rectangle that encloses the image and set its center position
        self.direction = pygame.math.Vector2()  # Create a vector to store the player's movement direction
        self.speed = 5  # Set the player's movement speed

    # Method to handle player input
    def input(self):
        keys = pygame.key.get_pressed()  # Get the state of all keyboard keys

        if keys[pygame.K_UP]:  # If the up arrow key is pressed
            self.direction.y = -1  # Set the y-component of the movement direction vector to -1
        elif keys[pygame.K_DOWN]:  # If the down arrow key is pressed
            self.direction.y = 1  # Set the y-component of the movement direction vector to 1
        else:
            self.direction.y = 0  # Otherwise, set the y-component of the movement direction vector to 0

        if keys[pygame.K_RIGHT]:  # If the right arrow key is pressed
            self.direction.x = 1  # Set the x-component of the movement direction vector to 1
        elif keys[pygame.K_LEFT]:  # If the left arrow key is pressed
            self.direction.x = -1  # Set the x-component of the movement direction vector to -1
        else:
            self.direction.x = 0  # Otherwise, set the x-component of the movement direction vector to 0

    # Method to update the player's position based on input
    def update(self):
        self.input()  # Call the input method to handle player input
        self.rect.center += self.direction * self.speed  # Move the player's rectangle based on the direction vector and speed

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
        self.keyboard_speed = 3  # Set the speed for keyboard-controlled camera movement
        self.mouse_speed = 2  # Set the speed for mouse-controlled camera movement

        # Zoom setup
        self.zoom_scale = 1  # Set the initial zoom scale
        self.internal_surf_size = (2500,2500)  # Set the size of the internal surface for rendering
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)  # Create an internal surface for rendering with alpha channel
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))  # Get the rectangle that encloses the internal surface and set its center position
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)  # Create a vector to store the size of the internal surface
        self.internal_offset = pygame.math.Vector2()  # Create a vector to store the internal offset

    # Method to center the camera on the target sprite
    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    # Method to box the camera around the target sprite
    def box_target_camera(self,target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    # Method to control the camera movement using keyboard input
    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.camera_rect.x -= self.keyboard_speed
        if keys[pygame.K_d]: self.camera_rect.x += self.keyboard_speed
        if keys[pygame.K_w]: self.camera_rect.y -= self.keyboard_speed
        if keys[pygame.K_s]: self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    # Method to control the camera movement using mouse input
    def mouse_control(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()

        left_border = self.camera_borders['left']
        top_border = self.camera_borders['top']
        right_border = self.display_surface.get_size()[0] - self.camera_borders['right']
        bottom_border = self.display_surface.get_size()[1] - self.camera_borders['bottom']

        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                pygame.mouse.set_pos((left_border,mouse.y))
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
                pygame.mouse.set_pos((right_border,mouse.y))
        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border,top_border)
                pygame.mouse.set_pos((left_border,top_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border,top_border)
                pygame.mouse.set_pos((right_border,top_border))
        elif mouse.y > bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border,bottom_border)
                pygame.mouse.set_pos((left_border,bottom_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border,bottom_border)
                pygame.mouse.set_pos((right_border,bottom_border))

        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                pygame.mouse.set_pos((mouse.x,top_border))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                pygame.mouse.set_pos((mouse.x,bottom_border))

        self.offset += mouse_offset_vector * self.mouse_speed

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
player = Player((640,360),camera_group)

# Create trees at random positions and add them to the CameraGroup
for i in range(20):
    random_x = randint(1000,2000)
    random_y = randint(1000,2000)
    Tree((random_x,random_y),camera_group)

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
    camera_group.custom_draw(player)  # Draw the scene with custom camera settings

    pygame.display.update()  # Update the display
    clock.tick(60)  # Cap the frame rate at 60 frames per second
