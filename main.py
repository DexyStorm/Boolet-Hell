import pygame

import player
from player import *

from screen import *


pygame.init()


#sets the game to fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#needed to make sure that the player doesnt go off-screen
screen_rect = get_display_rect(screen)

#needed for creating player in the middle of the screen
display_size = pygame.display.Info() 

#creates player lulw
player = create_player(display_size.current_w, display_size.current_h)

running = True
while(running):
      
   #background colour
   screen.fill((0, 0, 0))

   #draws the player onto the screen
   pygame.draw.rect(screen, (0, 255, 0), player)
   
   #moves the player
   player_movement(player, screen_rect)
      
   #goes through all events that pygame picks up
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   
   #updates game state
   pygame.display.update()      
      
pygame.quit()