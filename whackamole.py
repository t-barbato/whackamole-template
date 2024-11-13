import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x = 32 * random.randrange(0, 20)
        y = 32 * random.randrange(0, 16)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            grid = (16, 7, 181)
            for i in range(32, 640, 32):
                pygame.draw.line(screen, grid, (i, 0), (i, 512))
            for i in range(32, 512, 32):
                pygame.draw.line(screen, grid, (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            if event.type == pygame.MOUSEBUTTONDOWN:
                a, b = event.pos
                if x <= a <= x + 32 and y <= b <= y + 32:
                    x = 32 * random.randrange(0, 20)
                    y = 32 * random.randrange(0, 16)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
