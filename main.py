import pygame

pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode([800, 600])
FPS_CLOCK = pygame.time.Clock()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    DISPLAY_SURFACE.fill((255, 0, 0))
    pygame.draw.circle(DISPLAY_SURFACE, (0, 0, 0), (300, 300), 20)
    pygame.display.update()
    FPS_CLOCK.tick(30)
