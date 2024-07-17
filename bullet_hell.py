import pygame

pygame.init()

display_size = pygame.display.Info()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


player = pygame.Rect((display_size.current_w/4, display_size.current_h/4, 25, 25))





running = True
while(running):
   
   #background colour
   screen.fill((0, 0, 0))
   
   pygame.draw.rect(screen, (255, 0, 0), player)
   
   #movement
   key = pygame.key.get_pressed()
   if key[pygame.K_a] == True:
      player.move_ip(-1, 0)
   if key[pygame.K_d] == True:
      player.move_ip(1, 0)
   if key[pygame.K_s] == True:
      player.move_ip(0, 1)
   if key[pygame.K_w] == True:
      player.move_ip(0, -1)

   
   #goes through all events that pygame picks up
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   
   pygame.display.update()      
   
pygame.quit()