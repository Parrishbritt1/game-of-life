import pygame
from pygame.constants import KEYDOWN, K_ESCAPE
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
FPS = 60
START_BUTTON_LIGHT = "#1AC8F3"
START_BUTTON_DARK = "#3399FF"
STOP_BUTTON_LIGHT = "#FF0000"
STOP_BUTTON_DARK =  "#B92E34"
CLEAR_BUTTON_LIGHT = "#808080"
CLEAR_BUTTON_DARK = "#5a5a5a"

# Grid stuff
CELL_WIDTH = 20
CELL_HEIGHT = 20
MARGIN = 5
num_cell_cols = 30
num_cell_rows = 22

# Handy utility functions 
def pos_over_start(pos):
    return 328 <= pos[0] <= 447 and 560 <= pos[1] <= 590

def pos_over_clear(pos):
    return 620 <= pos[0] <= 740 and 560 <= pos[1] <= 590


def update_window(pos, grid, started, generation_count):
    rects = []
    for i in range(num_cell_rows):
        for j in range(num_cell_cols):
            color = "white"
            if grid[i][j] == 1:
                color = "green"
            rects.append(pygame.draw.rect(screen, color, [(MARGIN + CELL_WIDTH) * j + MARGIN,
                                            (MARGIN + CELL_HEIGHT) * i + MARGIN,
                                            CELL_WIDTH,
                                            CELL_HEIGHT]))


    # Start and Stop button hovered
    if pos_over_start(pos) and not started:
        pygame.draw.rect(screen, START_BUTTON_LIGHT, [WIDTH//2.3, 558, 120, 34])
    elif not started:
        pygame.draw.rect(screen, START_BUTTON_DARK, [WIDTH//2.3, 558, 120, 34])
    elif pos_over_start(pos) and started:
        pygame.draw.rect(screen, STOP_BUTTON_LIGHT, [WIDTH//2.3, 558, 120, 34])
    elif started:
        pygame.draw.rect(screen, STOP_BUTTON_DARK, [WIDTH//2.3, 558, 120, 34])

    # Start and Stop text rendering
    font = pygame.font.SysFont("Corbel", 35)
    if started:
        start_stop_text = font.render("STOP", True, "black")
    else:
        start_stop_text = font.render("START", True, "black")
    screen.blit(start_stop_text, (345, 560))

    # Generation counter
    generation_text = font.render("Generation: "+str(generation_count), True, "black")
    screen.blit(generation_text, (70, 560))

    # Back button
    pygame.draw.circle(screen, "#49ee13", (490, 568), 20)

    # Clear button
    if pos_over_clear(pos):
        pygame.draw.rect(screen, CLEAR_BUTTON_LIGHT, [620, 558, 120, 34])
    else:
        pygame.draw.rect(screen, CLEAR_BUTTON_DARK, [620, 558, 120, 34])

    clear_text = font.render("CLEAR", True, "black")
    screen.blit(clear_text, (625, 560))


    pygame.display.flip()


def is_grid_clicked(pos, grid, is_right_click):
    if is_right_click:
        if pos[1] < 550 and pos[0] < 750:
            col = pos[0] // (CELL_WIDTH + MARGIN)
            row = pos[1] // (CELL_HEIGHT + MARGIN)
            grid[row][col] = 0
    else:
        if pos[1] < 550 and pos[0] < 750:
            col = pos[0] // (CELL_WIDTH + MARGIN)
            row = pos[1] // (CELL_HEIGHT + MARGIN)
            grid[row][col] = 1


def clear_grid(grid):
    for i in range(num_cell_rows):
        for j in range(num_cell_cols):
            grid[i][j] = 0

def main():
    grid = []
    for i in range(num_cell_rows):
        grid.append([])
        for j in range(num_cell_cols):
            grid[i].append(0)

    clock = pygame.time.Clock()
    started = False
    run = True
    generation_count = 0
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            # Left click heled down
            elif pygame.mouse.get_pressed()[0]:
                if not started:
                    is_grid_clicked(pos, grid, False)      

            # Right click held down
            elif pygame.mouse.get_pressed()[2]:
                if not started:
                    is_grid_clicked(pos, grid, True)

            elif event.type == pygame.MOUSEBUTTONUP:
                if pos_over_start(pos) and not started:
                    started = True
                elif pos_over_start(pos) and started:
                    started = False

                if pos_over_clear(pos) and not started:
                    clear_grid(grid)
                    generation_count = 0

        screen.fill("gray")

        if started:
            grid = next_gen(grid)
            generation_count += 1
            clock.tick(5)

        update_window(pos, grid, started, generation_count)
    

    pygame.quit()


if __name__ == "__main__":
    main()