import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dino Game")
dino_img = pygame.image.load("dino.png")
dino_rect = dino_img.get_rect()
obstacle_img = pygame.image.load("cactus.png")
obstacle_rect = obstacle_img.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                dino_rect.y -= 10
                screen.fill((255, 255, 255))
                screen.blit(dino_img, dino_rect)
                screen.blit(obstacle_img, obstacle_rect)
                pygame.display.update()
