import pygame

def create_player(width, height):
   return pygame.Rect((width/2, height/2, 25, 25))

def player_movement(player, screen_rect):
   key = pygame.key.get_pressed()
   if key[pygame.K_a] == True:
      player.move_ip(-1, 0)
   if key[pygame.K_d] == True:
         player.move_ip(1, 0)
   if key[pygame.K_s] == True:
      player.move_ip(0, 1)
   if key[pygame.K_w] == True:
      player.move_ip(0, -1)

   #makes it so the player cannot escape the screen
   player.clamp_ip(screen_rect)