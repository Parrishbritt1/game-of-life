import pygame, math

class Button:
    def __init__(self, screen, name, text, text_x, text_y):
        self.screen = screen
        self.name = name.lower()
        self.text = text
        self.text_x = text_x
        self.text_y = text_y


    def __str__(self):
        return self.name

    def draw_button(self):
        """Drawing text onto screen
        """        
        font = pygame.font.SysFont("Corbel", 35)
        text = font.render(self.text, True, "black")
        self.screen.blit(text, (self.text_x, self.text_y))        


class CircleButton(Button):
    def __init__(self, screen, name, text, text_x, text_y, center_x, center_y, radius):
        super().__init__(screen, name, text, text_x, text_y)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def draw_button(self, color):
        """Drawing background onto screen and calls parent draw_button to draw text
        """   
        pygame.draw.circle(self.screen, color, (self.center_x, self.center_y), self.radius)
        super().draw_button()

    def mouse_over(self, pos):
        """Returns True if mouse is over Button

        Keyword arguments:
        pos -- (x, y) coords of mouse position
        """
        return math.hypot(self.center_x-pos[0], self.center_y-pos[1]) <= self.radius


class RectangleButton(Button):
    def __init__(self, screen, name, text, text_x, text_y, x, y, width, height):
        super().__init__(screen, name, text, text_x, text_y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_button(self, color):
        """Drawing background onto screen and calls parent draw_button to draw text
        """   
        pygame.draw.rect(self.screen, color, [self.x, self.y, self.width, self.height])
        super().draw_button()

    def mouse_over(self, pos, left_bound, right_bound, top_bound, bottom_bound):
        """Returns True if mouse is over Button

        Keyword arguments:
        pos -- (x, y) coords of mouse position
        left_bound -- x coord for left of button
        right_bound -- x coord for right of button
        top_bound -- y coord for top of button
        bottom_bound -- y coord for bottom of button
        """
        return left_bound <= pos[0] <= right_bound and top_bound <= pos[1] <= bottom_bound