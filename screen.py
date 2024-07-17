import pygame

def create_window():
   return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def get_display_rect(screen):
   return screen.get_rect()