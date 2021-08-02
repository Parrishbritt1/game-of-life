import pygame


# Screen stuff
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 60

# Grid stuff
CELL_WIDTH = 10
CELL_HEIGHT = 10
MARGIN = 5

def draw_window():
        screen.fill("gray")
        pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()