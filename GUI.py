from types import prepare_class
import pygame
from pygame.constants import KEYDOWN, K_ESCAPE
from GOL import next_gen
import time


WIDTH, HEIGHT = 755, 600
FPS = 60

# Grid stuff
CELL_WIDTH = 20
CELL_HEIGHT = 20
MARGIN = 5
num_cell_cols = 30
num_cell_rows = 22

class Button:
    def __init__(self, screen, name, text, text_x, text_y, shape, center_x=None, center_y=None, radius=None, top_left=None, top_right=None, bottom_left=None, bottom_right=None):
        self.screen = screen
        self.name = name.lower()
        self.text = text
        self.text_x = text_x
        self.text_y = text_y
        self.shape = shape.lower()

        # Circle inputs
        if radius is not None and center_x is not None and center_y is not None:
            self.radius = radius
            self.center_x = center_x
            self.center_y = center_y
        # Rect inputs
        elif top_left is not None and top_right is not None and bottom_left is not None and bottom_right is not None:
            self.top_left = top_left
            self.top_right = top_right
            self.bottom_left = bottom_left
            self.bottom_right = bottom_right

    def __str__(self):
        return self.name

    def draw_button(self, color):
        if self.shape == "circle":
            pygame.draw.circle(self.screen, color, (self.center_x, self.center_y), self.radius)
        elif self.shape == "rect":
            pygame.draw.rect(self.screen, color, [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

        font = pygame.font.SysFont("Corbel", 35)
        text = font.render(self.text, True, "black")
        self.screen.blit(text, (self.text_x, self.text_y))

    def mouse_over(self, pos):
        if self.name == "start":
            return 328 <= pos[0] <= 447 and 560 <= pos[1] <= 590
        elif self.name == "clear":
            return 620 <= pos[0] <= 740 and 560 <= pos[1] <= 590
        elif self.name == "back":
            pass
        elif self.name == "forward":
            pass
    
BUTTONS = {}
START_BUTTON_LIGHT = "#1AC8F3"
START_BUTTON_DARK = "#3399FF"
STOP_BUTTON_LIGHT = "#FF0000"
STOP_BUTTON_DARK =  "#B92E34"
CLEAR_BUTTON_LIGHT = "#808080"
CLEAR_BUTTON_DARK = "#5a5a5a"
MOVE_BUTTON_LIGHT = "#00FF00"
MOVE_BUTTON_DARK = "#00D100"

def create_buttons(screen):
    BUTTONS["start"] = Button(screen, name="start", text="START", text_x=345, text_y=560, shape="rect", top_left=WIDTH//2.3, top_right=558, bottom_left=120, bottom_right=34)
    BUTTONS["clear"] = Button(screen, name="clear", text="CLEAR", text_x=625, text_y=560, shape="rect", top_left=620, top_right=558, bottom_left=120, bottom_right=34)
    BUTTONS["back"] = Button(screen, name="back", text="<", text_x=510, text_y=558, shape="circle", center_x=520, center_y=575, radius=20)
    BUTTONS["forward"] = Button(screen, name="forward", text=">", text_x=565, text_y=558, shape="circle", center_x=570, center_y=575, radius=20)

def update_window(pos, grid, started, generation_count, screen):
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

    start_color = START_BUTTON_DARK
    clear_color = CLEAR_BUTTON_DARK
    back_color = MOVE_BUTTON_DARK
    forward_color = MOVE_BUTTON_DARK
    if pos is not None:
        if BUTTONS["start"].mouse_over(pos):
            start_color = START_BUTTON_LIGHT
        elif BUTTONS["clear"].mouse_over(pos) and not started:
            clear_color = CLEAR_BUTTON_LIGHT
        elif BUTTONS["back"].mouse_over(pos) and not started:
            back_color = MOVE_BUTTON_LIGHT
        elif BUTTONS["forward"].mouse_over(pos) and not started:
            forward_color = MOVE_BUTTON_LIGHT
    BUTTONS["start"].draw_button(start_color)
    BUTTONS["clear"].draw_button(clear_color)
    BUTTONS["back"].draw_button(back_color)
    BUTTONS["forward"].draw_button(forward_color)

    # Generation counter
    font = pygame.font.SysFont("Corbel", 35)
    generation_text = font.render("Generation: "+str(generation_count), True, "black")
    screen.blit(generation_text, (70, 560))

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
    # Screen stuff
    pygame.init()
    # ---- PC size ----
    # WIDTH, HEIGHT = 755, 800
    # --- Laptop size ---
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life")

    grid = []
    for i in range(num_cell_rows):
        grid.append([])
        for j in range(num_cell_cols):
            grid[i].append(0)


    create_buttons(screen)

    clock = pygame.time.Clock()
    started = False
    generation_count = 0
    pos = None
    run = True
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
                if BUTTONS["start"].mouse_over(pos) and not started:
                    started = True
                elif BUTTONS["start"].mouse_over(pos) and started:
                    started = False

                if BUTTONS["clear"].mouse_over(pos) and not started:
                    clear_grid(grid)
                    generation_count = 0

        screen.fill("gray")

        if started:
            grid = next_gen(grid)
            generation_count += 1
            clock.tick(5)

        update_window(pos, grid, started, generation_count, screen)
    

    pygame.quit()


if __name__ == "__main__":
    main()