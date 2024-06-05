import pygame, sys  
from random import randint 
from grid import *

# smanjiti funckije koristeci ovo
#        self.display_surface = pygame.display.get_surface()  # Get the display surface where the game is rendered
#
#        # Camera offset and borders setup
#        self.offset = pygame.math.Vector2()  # Create a vector to store the camera offset
#        self.half_w = self.display_surface.get_size()[0] // 2  # Get half of the display width
#        self.half_h = self.display_surface.get_size()[1] // 2  # Get half of the display height


# ------------------------------------------------------------------------------------------------------------------------------------ 
class CameraGroup(pygame.sprite.Group):
    def __init__(self, top_zone, left_zone):  # Constructor method, initializes the CameraGroup object
        super().__init__()  # Call the superclass constructor
        self.display_surface = pygame.display.get_surface()  # Get the display surface where the game is rendered

        # Camera offset and borders setup
        self.offset = pygame.math.Vector2()  # Create a vector to store the camera offset
        self.half_w = self.display_surface.get_size()[0] // 2  # Get half of the display width
        self.half_h = self.display_surface.get_size()[1] // 2  # Get half of the display height
        self.camera_borders = {'left': left_zone, 'right': top_zone, 'top': top_zone, 'bottom': left_zone}  # Define borders for the camera view

        # Camera rectangle setup
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)  # Create a rectangle representing the camera view

        # Ground setup
        self.ground_surf = pygame.image.load('assets/img/pozadina.png').convert_alpha()  # Load the ground image with transparency
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))  # Get the rectangle that encloses the ground image and set its top-left position

        # Camera movement speed
        self.keyboard_speed = 20  # Set the speed for keyboard-controlled camera movement

        # Zoom setup
        self.zoom_scale = 1  # Set the initial zoom scale
        self.internal_surf_size = (3000, 3000)  # Set the size of the internal surface for rendering
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)  # Create an internal surface for rendering with alpha channel
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w, self.half_h))  # Get the rectangle that encloses the internal surface and set its center position
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
    def custom_draw(self, tile_size, mumija_idle, vitez_idle, left_zone, top_zone):
        
        self.keyboard_control()
        self.zoom_keyboard_control()

        # Clear the internal surface with a sky blue color
        self.internal_surf.fill('#71ddee')

        # Draw the ground
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.internal_surf, ground_offset)

        # Scale the internal surface based on zoom scale
        scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))

        # Blit the scaled surface onto the display surface
        self.display_surface.blit(scaled_surf, scaled_rect)


        mumija_idle_image = mumija_idle.get_current_frame  # Get the current image from the Character
        vitez_idle_image = vitez_idle.get_current_frame  # Get the current image from the Character

        mumija_idle_scaled = pygame.transform.scale(mumija_idle_image, (mumija_idle.get_width() * self.zoom_scale, mumija_idle.get_height() * self.zoom_scale))
        vitez_idle_scaled = pygame.transform.scale(vitez_idle_image, (vitez_idle.get_width() * self.zoom_scale, vitez_idle.get_height() * self.zoom_scale))

        
        character_position = [
            left_zone +  mumija_idle_scaled.get_width(),
            top_zone + (tile_size / 2)
        ]
        character_position1 = [
            left_zone + vitez_idle_scaled.get_width(),
            top_zone + 5 * (tile_size / 2)
        ]

        self.display_surface.blit(mumija_idle_scaled, (character_position))
        self.display_surface.blit(vitez_idle_scaled, (character_position1))

        # Adjust positions based on zoom for proper centering within camera view
        character_position[0] += (scaled_rect.centerx - self.half_w) / self.zoom_scale
        character_position[1] += (scaled_rect.centery - self.half_h) / self.zoom_scale
        character_position1[0] += (scaled_rect.centerx - self.half_w) / self.zoom_scale
        character_position1[1] += (scaled_rect.centery - self.half_h) / self.zoom_scale

        self.display_surface.blit(mumija_idle_scaled, character_position)
        self.display_surface.blit(vitez_idle_scaled, character_position1)
# ------------------------------------------------------------------------------------------------------------------------------------ 
