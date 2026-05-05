import pygame, sys
pygame.init()

screen = pygame.display.set_mode((400, 300))

x, y = 100, 100   # position
dx, dy = 3, 3     # speed

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            sys.exit()

    # move ball
    x += dx
    y += dy

    # bounce logic (correct)
    if x <= 0 or x >= 380:
        dx *= -1
    if y <= 0 or y >= 280:
        dy *= -1

    # draw
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 10) 
    pygame.display.update()

