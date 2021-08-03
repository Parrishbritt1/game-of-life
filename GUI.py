import pygame


# Screen stuff
pygame.init()
WIDTH, HEIGHT = 755, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 400
START_BUTTON_LIGHT = "#1AC8F3"
START_BUTTON_DARK = "#3399FF"

# Grid stuff
CELL_WIDTH = 20
CELL_HEIGHT = 20
MARGIN = 5
grid = []

# Button stuff
start_button_clicked = False
for i in range(30):
    grid.append([])
    for j in range(30):
        grid[i].append(0)

def draw_window(pos):
    for i in range(30):
        for j in range(30):
            color = "white"
            if grid[i][j] == 1:
                color = "green"
            pygame.draw.rect(screen, color, [(MARGIN + CELL_WIDTH) * j + MARGIN,
                                             (MARGIN + CELL_HEIGHT) * i + MARGIN,
                                             CELL_WIDTH,
                                             CELL_HEIGHT])
    
    
    # Start button hovered
    if 328 <= pos[0] <= 447 and 760 <= pos[1] <= 790:
        pygame.draw.rect(screen, START_BUTTON_LIGHT, [WIDTH//2.3, 758, 120, 34])
    else:
        pygame.draw.rect(screen, START_BUTTON_DARK, [WIDTH//2.3, 758, 120, 34])

    font = pygame.font.SysFont("Corbel", 35)
    text = font.render("Start", True, "black")
    screen.blit(text, (355, 760))
    pygame.display.flip()

def grid_clicked(pos):
    if pos[1] < 750 and pos[0] < 750:
        col = pos[0] // (CELL_WIDTH + MARGIN)
        row = pos[1] // (CELL_HEIGHT + MARGIN)
        grid[row][col] = 1



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                grid_clicked(pos)
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid_clicked(pos)

        screen.fill("gray")
        pos = pygame.mouse.get_pos()
        draw_window(pos)

    pygame.quit()


if __name__ == "__main__":
    main()