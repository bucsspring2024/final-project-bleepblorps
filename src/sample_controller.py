'''import pygame

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
  pygame.quit()'''
  

import pygame
import sys

class Controller:
    def __init__(self):
        pygame.init()

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)

        self.show_people = False
        self.people = 0
        self.bottom_button_clicked = 0

        self.WIDTH, self.HEIGHT = 600, 400
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Game")

        self.popup_font = pygame.font.Font(None, 48)
        self.show_popup = False
        self.popup_text = ""
        self.popup_rect = pygame.Rect(self.WIDTH//4, self.HEIGHT//4, self.WIDTH//2, self.HEIGHT//2)
        self.show_retry_button = False
        self.retry_button = pygame.Rect(self.popup_rect.centerx - 50, self.popup_rect.bottom - 70, 100, 50)

        self.win_lose_font = pygame.font.Font(None, 48)
        self.font = pygame.font.Font(None, 36)

        wrapped_text = f"Your goal is to pay for your loans.\n\tYou can gain your balance by clicking on the\n\tx10 button every 10 clicks for a person. You\n\thave to pay all of your loans before the timer\n\truns out."
        self.text_surface = self.font.render(wrapped_text, True, self.RED)
        self.new_surface = pygame.transform.smoothscale(self.text_surface, (550, 150))
        self.text_rect = self.new_surface.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 80))
        wrapped_text = ["Your goal is to pay for your loans.","You can gain your balance by clicking on the", "button every 10 clicks for a person.",
        "You have to pay all of your loans before the timer", "runs out."]
        ycoor = 0
        self.text_surface = pygame.Surface((self.WIDTH//2, self.HEIGHT//2))
        self.text_surface.fill(self.WHITE)
        for text in wrapped_text:
          text_surface = self.font.render(text, True, self.RED)
          text_surface = pygame.transform.smoothscale_by(text_surface, 0.5)
          self.text_surface.blit(text_surface, (0, ycoor))
          ycoor += 30
        self.play_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT//2 - 50, 100, 50)
        self.show_bottom_button = False
        self.show_pay_button = False
        self.play_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT//2 - 50, 100, 50)
        self.pay_button = pygame.Rect(self.WIDTH//2 + 70, self.HEIGHT - 70, 100, 50)
        self.bottom_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT - 70, 100, 50)

        self.background_image = pygame.image.load("assets/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (600, 400))

        self.play_button_image = pygame.image.load("assets/imagebutton.png")
        self.bottom_button_image = pygame.image.load("assets/imagebutton.png")
        self.pay_button_image = pygame.image.load("assets/imagebutton.png")
        self.retry_button_image = pygame.image.load("assets/imagebutton.png")

        self.stick_figure_image = pygame.image.load("assets/Stick_Fig.png")

        button_width, button_height = 100, 50
        self.play_button_image = pygame.transform.scale(self.play_button_image, (button_width, button_height))
        self.bottom_button_image = pygame.transform.scale(self.bottom_button_image, (button_width, button_height))
        self.pay_button_image = pygame.transform.scale(self.pay_button_image, (button_width, button_height))
        self.retry_button_image = pygame.transform.scale(self.retry_button_image, (button_width, button_height))

        self.stick_figure = pygame.transform.scale(self.stick_figure_image, (75, 75))

        self.loan_balance = 0
        self.loan_amount = 150000
        self.show_loans = False
        self.stop_gaining_balance = False
        self.loan_text = self.font.render("Loans: ${} (Balance: ${})".format(self.loan_amount, self.loan_balance), True, self.RED)
        self.people_text = self.font.render("x{}".format(self.people), True, self.RED)
        self.people_rect = self.people_text.get_rect(topleft=(10, 55))  # Adjusted to go down a bit
        self.loan_rect = self.loan_text.get_rect(topleft=(10, 10))

        self.timer_font = pygame.font.Font(None, 48)
        self.continue_timer = False
        self.timer_value = 420
        self.show_timer = False
        self.timer_text = self.timer_font.render("Timer: {}:{}{}".format(self.timer_value // 60, str(self.timer_value % 60).zfill(2), "s"), True, self.RED)
        self.timer_rect = self.timer_text.get_rect(topright=(self.WIDTH - 10, 10))

        self.play_button_text = self.font.render("Play", True, self.BLACK)
        self.bottom_button_text = self.font.render("x10", True, self.BLACK)
        self.pay_button_text = self.font.render("Pay", True, self.BLACK)
        self.retry_button_text = self.font.render("Retry", True, self.BLACK)

        self.play_button_text_rect = self.play_button_text.get_rect(center=self.play_button.center)
        self.bottom_button_text_rect = self.bottom_button_text.get_rect(center=self.bottom_button.center)
        self.pay_button_text_rect = self.pay_button_text.get_rect(center=self.pay_button.center)
        self.retry_button_text_rect = self.retry_button_text.get_rect(center=self.retry_button.center)

        self.running = True
        self.play_button_screen = True


    def reset_scene(self):
        self.show_timer = False
        self.show_loans = False
        self.show_pay_button = False
        self.show_people = False
        self.show_popup = False
        self.show_retry_button = False
        self.continue_timer = False
        self.show_bottom_button = False
        
        self.bottom_button_clicked = 0
        self.timer_value = 420
        self.loan_amount = 150000 # enter class
        self.people = 0 #enter class
        self.loan_balance = 0 # enter class Access through organization object. Instead of self.people do self.org.people
        # wrapped_text = ["Your goal is to pay for your loans.","You can gain your balance by clicking on the", "button every 10 clicks for a person.",
        # "You have to pay all of your loans before the timer", "runs out."]
        # xcoor = 0
        # for text in wrapped_text:
        #   text_surface = self.font.render(wrapped_text, True, self.RED)
        #   self.new_surface = pygame.transform.smoothscale(text_surface, (550, 150))
        #   xcoor += 50
        #   self.text_rect = self.new_surface.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + xcoor))
        #   self.play_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT//2 - 50, 100, 50)
    
    def show_popup_message(self, message):
        self.popup_text = message
        self.show_popup = True
    
    def show_up_timer(self):
        if self.show_timer:
            pygame.time.wait(1000)
            self.timer_value -= 1

            if self.people > 0 and not self.stop_gaining_balance:
                self.loan_balance += self.people * self.people

            if self.timer_value == 0 and self.loan_amount > 0:
                self.continue_timer = False
                self.stop_gaining_balance = True
                self.show_popup = True
                self.show_retry_button = True
                self.show_pay_button = False
                self.show_bottom_button = False
                self.popup_text = "You Lost!"

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.play_button_screen and self.running:
                            self.running = False
                        if not self.play_button_screen:
                            self.show_bottom_button = False
                            self.play_button_screen = True
                            self.show_popup = False
                            self.reset_scene()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        self.show_loans = True
                        self.show_timer = True
                        self.continue_timer = True
                        self.show_people = True
                        self.text_surface = self.font.render("", True, self.BLACK)
                        self.play_button = pygame.Rect(0, 0, 0, 0)
                        self.play_button_screen = False
                        self.show_bottom_button = True
                        self.stop_gaining_balance = False
                        self.show_pay_button = True
                    elif self.bottom_button.collidepoint(event.pos):
                        self.bottom_button_clicked += 1
                        if self.bottom_button_clicked % 10 == 0:
                            self.people += 1
                            self.people_text = self.font.render("x{}".format(self.people), True, self.RED)
                    elif self.pay_button.collidepoint(event.pos):
                        if self.loan_balance > 0:
                            self.loan_amount -= self.loan_balance
                            self.loan_balance = 0
                            if self.loan_amount <= 0:
                                self.continue_timer = False
                                self.stop_gaining_balance = True
                                self.show_popup = True
                                self.show_retry_button = True
                                self.show_pay_button = False
                                self.show_bottom_button = False
                                self.popup_text = "You Won!"
                    elif self.show_retry_button and self.retry_button.collidepoint(event.pos):
                        self.reset_scene()

            self.screen.blit(self.background_image, (0, 0))

            if self.play_button.width > 0:
                self.screen.blit(self.play_button_image, self.play_button)
                self.screen.blit(self.play_button_text, self.play_button_text_rect)

            if self.show_bottom_button:
                self.screen.blit(self.bottom_button_image, self.bottom_button)
                self.screen.blit(self.bottom_button_text, self.bottom_button_text_rect)

            if self.show_pay_button:
                self.screen.blit(self.pay_button_image, self.pay_button)
                self.screen.blit(self.pay_button_text, self.pay_button_text_rect)

            if self.text_surface.get_width() > 0:
                # pygame.draw.rect(self.screen, self.RED, self.text_rect, 2)
                self.screen.blit(self.text_surface, (0, self.HEIGHT/2)) #place text

            if self.show_loans:
                self.loan_text = self.font.render("Loans: ${} (Balance: ${})".format(self.loan_amount, self.loan_balance), True, self.RED)
                self.screen.blit(self.loan_text, self.loan_rect)
            
            if self.show_people:
                stick_figure_x = 10 
                stick_figure_y = 75 

                self.screen.blit(self.stick_figure, (stick_figure_x, stick_figure_y))

                self.screen.blit(self.people_text, (stick_figure_x + self.stick_figure.get_width() + 10, stick_figure_y))  # Adjusted for spacing

            if self.show_timer and self.continue_timer:
                self.timer_text = self.timer_font.render("Timer: {}:{}{}".format(self.timer_value // 60, str(self.timer_value % 60).zfill(2), "s"), True, self.RED)
                self.screen.blit(self.timer_text, self.timer_rect)
            
            if self.show_popup:
                pygame.draw.rect(self.screen, self.GRAY, self.popup_rect)
                pygame.draw.rect(self.screen, self.BLACK, self.popup_rect, 2)

                popup_surface = self.popup_font.render(self.popup_text, True, self.BLACK)
                popup_rect = popup_surface.get_rect(center=self.popup_rect.center)

                self.screen.blit(popup_surface, popup_rect)

                if self.show_retry_button:
                    self.screen.blit(self.retry_button_image, self.retry_button)
                    self.screen.blit(self.retry_button_text, self.retry_button_text_rect)

            pygame.display.flip()

            self.show_up_timer()

        pygame.quit()
        sys.exit()

scene = Controller()
scene.run()