import pygame, sys  
from random import randint 
# from grid import *
# ------------------------------------------------------------------------------------------------------------------------------------ 

class Character:
    def __init__(self, spritesheet_path, num_frames, animation_speed=0.1):
        self.spritesheet = pygame.image.load(spritesheet_path)
        self.num_frames = num_frames
        self.frame_width = self.spritesheet.get_width() // num_frames
        self.frame_height = self.spritesheet.get_height()
        self.current_frame = 0
        self.animation_speed = animation_speed  # Adjust as needed
        self.animation_timer = 0
        self.frames_to_skip = 5 - num_frames
    
    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.animation_timer = 0
            if self.current_frame >= self.num_frames - self.frames_to_skip:
                self.current_frame = 0

    
    def draw(self, surface, x, y, character_sprite_size):
        frame_rect = pygame.Rect(self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
        frame_surface = self.spritesheet.subsurface(frame_rect)
        resized_frame_surface = pygame.transform.scale(frame_surface, (character_sprite_size, character_sprite_size))
        surface.blit(resized_frame_surface, (x, y))

    def position(self, x, y):
        character_position = [260, 170]
        character_position1 = [240, 180]
# ------------------------------------------------------------------------------------------------------------------------------------ 


# smanjiti funckije koristeci ovo
#        self.display_surface = pygame.display.get_surface()  # Get the display surface where the game is rendered
#
#        # Camera offset and borders setup
#        self.offset = pygame.math.Vector2()  # Create a vector to store the camera offset
#        self.half_w = self.display_surface.get_size()[0] // 2  # Get half of the display width
#        self.half_h = self.display_surface.get_size()[1] // 2  # Get half of the display height


# ------------------------------------------------------------------------------------------------------------------------------------ 
def interactive_screen(window, width, height, top_zone):

    interactive_screen = pygame.image.load("assets/img/opcija1.jpg")
    interactive_screen = pygame.transform.scale(interactive_screen, (width, top_zone))   

    window.blit(interactive_screen, (0, height - top_zone))
# ------------------------------------------------------------------------------------------------------------------------------------ 
def pozadina(width, height, top_zone, left_zone):
    window = pygame.display.get_surface()  # Get the display surface where the game is rendered
    top_image = pygame.image.load("assets/img/pozadina1.png")                                                            
    top_image = pygame.transform.scale(top_image, (width, top_zone))

    left_image = pygame.image.load("assets/img/pozadina.png")
    left_image = pygame.transform.scale(left_image, (left_zone, height - top_zone))    

    right_image = pygame.image.load("assets/img/pozadina.png")
    right_image = pygame.transform.scale(right_image, (left_zone, height - top_zone))    

    offsetX = 5
# ------------------------------------------------------------------------------------------------------------------------------------  print
    window.fill((255, 255, 255)) 
    window.blit(top_image, (0, 0))
    window.blit(left_image, (0, top_zone))
    window.blit(right_image, (width + offsetX - left_zone, top_zone))
# ------------------------------------------------------------------------------------------------------------------------------------ 





# ------------------------------------------------------------------------------------------------------------------------------------ 
class CameraGroup(pygame.sprite.Group):
    def __init__(self):  # Constructor method, initializes the CameraGroup object
        super().__init__()  # Call the superclass constructor
        self.display_surface = pygame.display.get_surface()  # Get the display surface where the game is rendered

        # Camera offset and borders setup
        self.offset = pygame.math.Vector2()  # Create a vector to store the camera offset
        self.half_w = self.display_surface.get_size()[0] // 2  # Get half of the display width
        self.half_h = self.display_surface.get_size()[1] // 2  # Get half of the display height
        self.camera_borders = {'left': 100, 'right': 100, 'top': 100, 'bottom': 100}  # Define borders for the camera view

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
        self.internal_surf_size = (3000, 3000)  # Set the size of the internal surface for rendering
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)  # Create an internal surface for rendering with alpha channel
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))  # Get the rectangle that encloses the internal surface and set its center position
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)  # Create a vector to store the size of the internal surface
        self.internal_offset = pygame.math.Vector2()  # Create a vector to store the internal offset

    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.camera_rect.x -= self.keyboard_speed
        if keys[pygame.K_d]: self.camera_rect.x += self.keyboard_speed
        if keys[pygame.K_w]: self.camera_rect.y -= self.keyboard_speed
        if keys[pygame.K_s]: self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def zoom_keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.zoom_scale += 0.1
            if self.zoom_scale >= 3:
                self.zoom_scale = 3
        if keys[pygame.K_e]:
            self.zoom_scale -= 0.1
            if self.zoom_scale <= 0.1:
                self.zoom_scale = 0.1

    # Method to draw the scene with custom camera settings
    def custom_draw(self, player):
        
        self.keyboard_control()
        self.zoom_keyboard_control()

        # Clear the internal surface with a sky blue color
        self.internal_surf.fill('#71ddee')

        # Draw the ground
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.ground_surf, ground_offset)

        # Scale the internal surface based on zoom scale
        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w, self.half_h))

        # Blit the scaled surface onto the display surface
        self.display_surface.blit(scaled_surf, scaled_rect)
# ------------------------------------------------------------------------------------------------------------------------------------ 
