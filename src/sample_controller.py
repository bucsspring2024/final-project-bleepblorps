import pygame

class Background(pygame.sprite.Sprite):
  def __init__(self, width, height):
    self.color = (50, 50, 50)
    self.image = pygame.Surface((width, height))
    self.rect = self.image.get_rect()
    
  def update(self):
    for idx, c in enumerate(self.color):
      self.color[idx] = (c + 1) % 256
    self.image.fill(self.colors)
  

  
class Controller:
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode()
    self.clock = pygame.time.Clock()
    self.background = Background(self.screen.get_size())
    self.state = "menu"
    self.running = True

  def mainloop(self):
    while True:
      if self.state == "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
        
        
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
    while self.state == "game":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.running = False
        elif event.type == pygame.USEREVENT:
          if event.button == self.button:
            self.state = "gameover"
      self.background.update()
      self.background.draw(self.screen)
      pygame.display.flip()
      self.clock.tick(60)
    elif event.type ==

  def gameoverloop(self):
    pass  # Ill do this l8r

if __name__ == "__main__":
  controller = Controller()
  controller.mainloop()
  pygame.quit()
  pass()
