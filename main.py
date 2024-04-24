import pygame
import sys
from src.sample_controller import Controller
imagebutton = pygame.image.load('assets/imagebutton.jpg')
from src.thebutton import ImageButton
from assets import imagebutton

#import your controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()
    thebutton = ImageButton(100, 100, 200, 100, "Click me", "assets/imagebutton.jpg")
    while controller.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controller.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controller.running = False
            thebutton.handle_event(event)
        thebutton.check_hover(pygame.mouse.get_pos())
        controller.screen.fill((0, 0, 0))
        thebutton.draw(controller.screen)
        pygame.display.flip()
        controller.clock.tick(60)
    
    pygame.quit()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
