import pygame
import sys
 
class Controller:
    def __init__(self):
        pygame.init()
 
        self.WHITE = (255, 255, 255)
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
        self.retry_button_text = self.popup_font.render("Retry", True, self.BLACK)
        self.retry_button_text_rect = self.retry_button_text.get_rect(center=self.retry_button.center)
 
        self.win_lose_font = pygame.font.Font(None, 48)
        self.font = pygame.font.Font(None, 36)
 
        wrapped_text = "Your goal is to pay for your loans.\nYou can gain your balance by clicking on the\nx10 button every 10 clicks for a person. You\nhave to pay all of your loans before the timer\nruns out."
        self.text_surface = self.font.render(wrapped_text, True, self.BLACK)
        self.new_surface = pygame.transform.smoothscale(self.text_surface, (550, 150))
        self.text_rect = self.new_surface.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 80))
 
        self.show_bottom_button = False
        self.show_pay_button = False
        self.play_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT//2 - 50, 100, 50)
        self.pay_button = pygame.Rect(self.WIDTH//2 + 70, self.HEIGHT - 70, 100, 50)
        self.pay_button_text = self.font.render("Pay", True, self.BLACK)
        self.pay_button_text_rect = self.pay_button_text.get_rect(center=self.pay_button.center)
        self.bottom_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT - 70, 100, 50)
        self.bottom_button_text = self.font.render("x10", True, self.BLACK)
        self.bottom_button_text_rect = self.bottom_button_text.get_rect(center=self.bottom_button.center)
 
        self.loan_balance = 0
        self.loan_amount = 150000
        self.show_loans = False
        self.stop_gaining_balance = False
        self.loan_text = self.font.render("Loans: ${} (Balance: ${})".format(self.loan_amount, self.loan_balance), True, self.BLACK)
        self.people_text = self.font.render("People: {}".format(self.people), True, self.BLACK)
        self.people_rect = self.people_text.get_rect(topleft=(10, 35))
        self.loan_rect = self.loan_text.get_rect(topleft=(10, 10))
 
        self.timer_font = pygame.font.Font(None, 48)
        self.continue_timer = False
        self.timer_value = 420
        self.show_timer = False
        self.timer_text = self.timer_font.render("Timer: {}:{}{}".format(self.timer_value // 60, str(self.timer_value % 60).zfill(2), "s"), True, self.BLACK)
        self.timer_rect = self.timer_text.get_rect(topright=(self.WIDTH - 10, 10))
 
        self.running = True
        self.play_button_screen = True
    
    def updatetext(self):
        x, y, z, zbottom = textrect = self.text_surface.get_rect()
        self.new_surface.blit(self.text_surface, textrect)
 
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
        self.loan_amount = 150000
        self.people = 0
        self.loan_balance = 0
        wrapped_text = "Your goal is to pay for your loans.\nYou can gain your balance by clicking on the\nx10 button every 10 clicks for a person. You\nhave to pay all of your loans before the timer\nruns out."
        self.text_surface = self.font.render(wrapped_text, True, self.BLACK)
        self.new_surface = pygame.transform.smoothscale(self.text_surface, (550, 150))
        self.text_rect = self.new_surface.get_rect(center=(self.WIDTH//2, self.HEIGHT//2 + 80))
        self.play_button = pygame.Rect(self.WIDTH//2 - 50, self.HEIGHT//2 - 50, 100, 50)
    
    def show_popup_message(self, message):
        self.popup_text = message
        self.show_popup = True
 
    def draw_popup(self):
        pygame.draw.rect(self.screen, self.WHITE, self.popup_rect)
        pygame.draw.rect(self.screen, self.BLACK, self.popup_rect, 2)
        popup_text_surface = self.popup_font.render(self.popup_text, True, self.BLACK)
        popup_text_rect = popup_text_surface.get_rect(center=self.popup_rect.center)
        self.screen.blit(popup_text_surface, popup_text_rect)
 
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
 
            self.screen.fill(self.WHITE)
 
            if self.play_button.width > 0:
                pygame.draw.rect(self.screen, self.GRAY, self.play_button)
                pygame.draw.rect(self.screen, self.BLACK, self.play_button, 2)
 
                play_text = self.font.render("Play", True, self.BLACK)
                play_text_rect = play_text.get_rect(center=self.play_button.center)
 
                self.screen.blit(play_text, play_text_rect)
 
            if self.show_bottom_button:
                pygame.draw.rect(self.screen, self.GRAY, self.bottom_button)
                pygame.draw.rect(self.screen, self.BLACK, self.bottom_button, 2)
                self.screen.blit(self.bottom_button_text, self.bottom_button_text_rect)
 
            if self.show_pay_button:
                pygame.draw.rect(self.screen, self.GRAY, self.pay_button)
                pygame.draw.rect(self.screen, self.BLACK, self.pay_button, 2)
                self.screen.blit(self.pay_button_text, self.pay_button_text_rect)
 
            if self.text_surface.get_width() > 0:
                pygame.draw.rect(self.screen, self.BLACK, self.text_rect, 2)
                self.screen.blit(self.text_surface, self.text_rect)
 
            if self.show_loans:
                self.loan_text = self.font.render("Loans: ${} (Balance: ${})".format(self.loan_amount, self.loan_balance), True, self.BLACK)
                self.screen.blit(self.loan_text, self.loan_rect)
            
            if self.show_people:
                self.people_text = self.font.render("People: {}".format(self.people), True, self.BLACK)
                self.screen.blit(self.people_text, self.people_rect)
 
            if self.show_timer and self.continue_timer:
                self.timer_text = self.timer_font.render("Timer: {}:{}{}".format(self.timer_value // 60, str(self.timer_value % 60).zfill(2), "s"), True, self.BLACK)
                self.screen.blit(self.timer_text, self.timer_rect)
            
            if self.show_popup:
                pygame.draw.rect(self.screen, self.GRAY, self.popup_rect)
                pygame.draw.rect(self.screen, self.BLACK, self.popup_rect, 2)
 
                popup_surface = self.popup_font.render(self.popup_text, True, self.BLACK)
                popup_rect = popup_surface.get_rect(center=self.popup_rect.center)
 
                self.screen.blit(popup_surface, popup_rect)
 
                if self.show_retry_button:
                    pygame.draw.rect(self.screen, self.GRAY, self.retry_button)
                    pygame.draw.rect(self.screen, self.BLACK, self.retry_button, 2)
                    self.screen.blit(self.retry_button_text, self.retry_button_text_rect)
 
            pygame.display.flip()
 
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
 
        pygame.quit()
        sys.exit()
 
scene = Controller()
scene.run()