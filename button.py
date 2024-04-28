import pygame

class Button():
    def __init__(self, image=None, pos=(0, 0), scale_factor=1):
        if image is not None:
            self.original_image = image
            self.image = pygame.transform.scale(image, (image.get_width() * scale_factor, image.get_height() * scale_factor))
        else:
            # Create a default "Quit" button image
            self.image = pygame.Surface((200, 200))
            self.image.fill((255, 0, 0))  # Fill with red color
            font = pygame.font.Font(None, 36)
            text = font.render("Quit", True, (255, 255, 255))  # White text
            text_rect = text.get_rect(center=self.image.get_rect().center)
            self.image.blit(text, text_rect)
        
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
