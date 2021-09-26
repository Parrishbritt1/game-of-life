import pygame
from pygame.constants import KEYDOWN, K_ESCAPE
from GOL import next_gen
import grid
from button import RectangleButton, CircleButton

# Screen
# ---- PC size ----
# WIDTH, HEIGHT = 755, 800
# ---- Laptop size ---
WIDTH, HEIGHT = 755, 600
FPS = 60

# BUTTONS dictionary contains Key - "button_name" : Value - "<Button>"
BUTTONS = {}
START_BUTTON_LIGHT = "#1AC8F3"
START_BUTTON_DARK = "#3399FF"
STOP_BUTTON_LIGHT = "#FF0000"
STOP_BUTTON_DARK =  "#B92E34"
CLEAR_BUTTON_LIGHT = "#808080"
CLEAR_BUTTON_DARK = "#5a5a5a"
MOVE_BUTTON_LIGHT = "#00FF00"
MOVE_BUTTON_DARK = "#00D100"

    
class PygameGrid(grid.Grid):
    def __init__(self, num_rows, num_cols, cell_width, cell_height, margin):
        super().__init__(num_rows, num_cols, cell_width, cell_height, margin)


    def draw_grid(self, screen):
        """Draws the rectangles onto screen representing the grid

        Keyword aruments:
        screen -- the pygame screen to draw on
        """
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                color = "white"
                if self.grid[i][j] == 1:
                    color = "green"
                pygame.draw.rect(screen, color, [(self.margin + self.cell_width) * j + self.margin,
                                                (self.margin + self.cell_height) * i + self.margin,
                                                self.cell_width,
                                                self.cell_height])

    def is_grid_clicked(self, pos, is_right_click):
        """Changes grid element to be 0(dead) or 1(alive) depending on where the mouse is positioned at time of click

        Keyword arguments:
        pos -- (x, y) coords of mouse position
        is_right_click -- if the click was a right click it (erases the cell) and vice versa
        """
        if is_right_click:
            if pos[1] < 550 and pos[0] < 750:
                col = pos[0] // (self.cell_width + self.margin)
                row = pos[1] // (self.cell_height + self.margin)
                self.grid[row][col] = 0
        else:
            if pos[1] < 550 and pos[0] < 750:
                col = pos[0] // (self.cell_width + self.margin)
                row = pos[1] // (self.cell_height + self.margin)
                self.grid[row][col] = 1


def create_buttons(screen):
    # Creates buttons and adds them to BUTTONS dictionary
    BUTTONS["start"] = RectangleButton(screen, name="start", text="START", text_x=345, text_y=560, top_left=WIDTH//2.3, top_right=558, bottom_left=120, bottom_right=34)
    BUTTONS["clear"] = RectangleButton(screen, name="clear", text="CLEAR", text_x=625, text_y=560, top_left=620, top_right=558, bottom_left=120, bottom_right=34)
    BUTTONS["back"] = CircleButton(screen, name="back", text="<", text_x=510, text_y=558, center_x=520, center_y=575, radius=20)
    BUTTONS["forward"] = CircleButton(screen, name="forward", text=">", text_x=565, text_y=558, center_x=570, center_y=575, radius=20)

def update_window(pos, started, current_gen, screen, g):
    # Updates the pygame screen 
    g.draw_grid(screen)


    # Default colors of buttons
    start_color = START_BUTTON_DARK
    clear_color = CLEAR_BUTTON_DARK
    back_color = MOVE_BUTTON_DARK
    forward_color = MOVE_BUTTON_DARK
    if pos is not None:
        # If Buttons are hovered change to brighter color
        if BUTTONS["start"].mouse_over(pos, left_bound=328, right_bound=447, top_bound=560, bottom_bound=590) and not started:
            start_color = START_BUTTON_LIGHT
        elif BUTTONS["start"].mouse_over(pos, left_bound=328, right_bound=447, top_bound=560, bottom_bound=590) and started:
            start_color = STOP_BUTTON_LIGHT
        elif BUTTONS["clear"].mouse_over(pos, left_bound=620, right_bound=740, top_bound=560, bottom_bound=590) and not started:
            clear_color = CLEAR_BUTTON_LIGHT
        elif BUTTONS["back"].mouse_over(pos) and not started:
            back_color = MOVE_BUTTON_LIGHT
        elif BUTTONS["forward"].mouse_over(pos) and not started:
            forward_color = MOVE_BUTTON_LIGHT
    # This is to change to stop color (red) if the game loop is "started"
    if started and start_color != STOP_BUTTON_LIGHT:
        start_color = STOP_BUTTON_DARK

    BUTTONS["start"].draw_button(start_color, started)
    BUTTONS["clear"].draw_button(clear_color, started)
    BUTTONS["back"].draw_button(back_color, started)
    BUTTONS["forward"].draw_button(forward_color, started)

    # Generation counter
    font = pygame.font.SysFont("Corbel", 35)
    generation_text = font.render("Generation: "+str(current_gen), True, "black")
    screen.blit(generation_text, (70, 560))

    pygame.display.flip()


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life")
    
    g = PygameGrid(num_rows=22, num_cols=30, cell_width=20, cell_height=20, margin=5)
    # grid_states dictionary responsible for saving each grid (for the back and forward buttons)
    grid_states = {}

    create_buttons(screen)
    
    clock = pygame.time.Clock()
    started = False
    current_gen = 0
    run = True
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Escape and the X close application
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            
            # Left click heled down
            elif pygame.mouse.get_pressed()[0]:
                # Draw onto grid if game isn't running
                if not started:
                    g.is_grid_clicked(pos, False)

            # Right click held down
            elif pygame.mouse.get_pressed()[2]:
                # Draw onto grid if game isn't running
                if not started:
                    g.is_grid_clicked(pos, True)

            # On click
            elif event.type == pygame.MOUSEBUTTONUP:
                # Start pressed
                if BUTTONS["start"].mouse_over(pos, left_bound=328, right_bound=447, top_bound=560, bottom_bound=590) and not started:
                    started = True
                    grid_states[current_gen] = g.grid
                elif BUTTONS["start"].mouse_over(pos, left_bound=328, right_bound=447, top_bound=560, bottom_bound=590) and started:
                    started = False

                # Back pressed
                if BUTTONS["back"].mouse_over(pos) and not started:
                    # If there is a "grid state" in the one prior to the current generation then move to it
                    if current_gen - 1 in grid_states:
                        current_gen -= 1
                        g.grid = grid_states[current_gen]

                # Forward pressed
                if BUTTONS["forward"].mouse_over(pos) and not started:
                    # In case you decide to click forward without clicking start first (saves the initial generation)
                    if current_gen == 0:
                        grid_states[current_gen] = g.grid

                    # Similar but opposite of back button in that it will get the next generation if at the end of "grid states"
                    if current_gen + 1 in grid_states and grid_states[current_gen+1] == next_gen(g.grid):
                        current_gen += 1
                        g.grid = grid_states[current_gen]
                    else:
                        g.grid = next_gen(g.grid)
                        current_gen += 1
                        grid_states[current_gen] = g.grid

                # Clear pressed
                if BUTTONS["clear"].mouse_over(pos, left_bound=620, right_bound=740, top_bound=560, bottom_bound=590) and not started:
                    g.clear_grid()
                    grid_states.clear()
                    current_gen = 0

        screen.fill("gray")

        # If the start button was pressed
        if started:
            g.grid = next_gen(g.grid)
            current_gen += 1
            grid_states[current_gen] = g.grid
            # Slows FPS to 5 so the grid doesn't update insanely fast
            # (need to find a better solution because it makes the start/stop button "laggy" when game is 'started') 
            clock.tick(5)
        

        update_window(pos, started, current_gen, screen, g)
    
    pygame.quit()


if __name__ == "__main__":
    main()