import pygame

class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    self.clock = pygame.time.Clock()
    self.running = True

  def mainloop(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.running = False
      self.menuloop()
      self.gameloop()
      self.gameoverloop()
      pygame.display.flip()
      self.clock.tick(60)

  def menuloop(self):
    pass  # Ill do this l8r

  def gameloop(self):
    pass  # Ill do this l8r

  def gameoverloop(self):
    pass  # Ill do this l8r

if __name__ == "__main__":
  controller = Controller()
  controller.mainloop()
  pygame.quit()
