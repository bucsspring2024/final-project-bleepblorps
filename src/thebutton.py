import pygame
class ImageButton:
    def __init__(self, x, y, width, height, text, image_path):
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.text = text
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image 
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.is_hovered = False
    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, ("green"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSBUTTONDOWN and event.button == 1:
            return True
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))  
        