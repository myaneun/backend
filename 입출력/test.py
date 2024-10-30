import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_pos_x = 100
player_pos_y = 100

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        player_pos_x -= 1
    
    if key_event[pygame.K_RIGHT]:
        player_pos_x += 1

    if key_event[pygame.K_UP]:
        player_pos_y -= 1
    
    if key_event[pygame.K_DOWN]:
        player_pos_y += 1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (player_pos_x, player_pos_y), 20)
    pygame.display.update()