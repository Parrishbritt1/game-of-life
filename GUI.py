import pygame
from GOL import next_gen
import time


# Screen stuff
pygame.init()
# ---- PC size ----
# WIDTH, HEIGHT = 755, 800
# --- Laptop size ---
WIDTH, HEIGHT = 755, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
FPS = 400
START_BUTTON_LIGHT = "#1AC8F3"
START_BUTTON_DARK = "#3399FF"

# Grid stuff
CELL_WIDTH = 20
CELL_HEIGHT = 20
MARGIN = 5
num_cell_cols = 30
num_cell_rows = 22




def draw_window(pos, grid):
    """Updates the Screen with grid and buttons"""
    for i in range(num_cell_rows):
        for j in range(num_cell_cols):
            color = "white"
            if grid[i][j] == 1:
                color = "green"
            pygame.draw.rect(screen, color, [(MARGIN + CELL_WIDTH) * j + MARGIN,
                                             (MARGIN + CELL_HEIGHT) * i + MARGIN,
                                             CELL_WIDTH,
                                             CELL_HEIGHT])
    
    
    # Start button hovered
    if pos_over_start(pos):
        pygame.draw.rect(screen, START_BUTTON_LIGHT, [WIDTH//2.3, 558, 120, 34])
    else:
        pygame.draw.rect(screen, START_BUTTON_DARK, [WIDTH//2.3, 558, 120, 34])

    font = pygame.font.SysFont("Corbel", 35)
    text = font.render("Start", True, "black")
    screen.blit(text, (355, 560))
    pygame.display.flip()

def grid_clicked(pos, grid):
    if pos[1] < 550 and pos[0] < 750:
        col = pos[0] // (CELL_WIDTH + MARGIN)
        row = pos[1] // (CELL_HEIGHT + MARGIN)
        grid[row][col] = 1

def pos_over_start(pos):
    return 328 <= pos[0] <= 447 and 560 <= pos[1] <= 590


def main():
    grid = []
    for i in range(num_cell_rows):
        grid.append([])
        for j in range(num_cell_cols):
            grid[i].append(0)

    start_button_clicked = False
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Left click heled down
            elif pygame.mouse.get_pressed()[0]:
                if not start_button_clicked:
                    grid_clicked(pos, grid)

            elif event.type == pygame.MOUSEBUTTONUP:
                if pos_over_start(pos):
                    start_button_clicked = True
                    # Loop through 100 iterations
                    for _ in range(100):
                        grid = next_gen(grid)
                        draw_window(pos, grid)
                        time.sleep(.3)


        screen.fill("gray")
        pos = pygame.mouse.get_pos()
        draw_window(pos, grid)

    pygame.quit()


if __name__ == "__main__":
    main()