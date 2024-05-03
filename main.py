import pygame
import sys
from src.sample_controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.run()