from turtle import Turtle

DISTANCE_FROM_BORDER = 20

PEN_COLOUR_PRIMARY = "#00D58B"
PEN_COLOUR_SECONDARY = "#FFFFFF"
PEN_WIDTH_PRIMARY = 10
PEN_WIDTH_SECONDARY = 4

FONT = ("Arial", 50, "bold")
TITLE_TEXT = "BAD Space Invaders"

START_BTN_COLOUR = "#FFFFFF"

START_BTN = "icons/start_btn.gif"


def create_start_button(screen):
    start_btn = Turtle()
    start_btn.goto(0, 0)
    start_btn.color(START_BTN_COLOUR)
    screen.addshape(START_BTN)
    start_btn.shape(START_BTN)
    start_btn.shapesize(stretch_wid=5, stretch_len=10)

    return start_btn


class WinManager(Turtle):
    def __init__(self, screen_obj, width: int, height: int):
        super().__init__()
        self.screen = screen_obj
        self.speed(0)
        self.__half_width = width / 2
        self.__half_height = height / 2

        self.hideturtle()

        self.draw_border()
        self.__place_title()

        self.start_btn = create_start_button(self.screen)
        self.start_btn.onclick(self.start_game)

        self.start = False

    def draw_border(self):
        self.draw(PEN_WIDTH_PRIMARY, PEN_COLOUR_PRIMARY)
        self.draw(PEN_WIDTH_SECONDARY, PEN_COLOUR_SECONDARY)

    def draw(self, pen_width, pen_colour):
        self.pencolor(pen_colour)
        self.width(pen_width)

        start_x = self.__half_width - DISTANCE_FROM_BORDER
        start_y = self.__half_height - DISTANCE_FROM_BORDER
        self.penup()

        self.goto(x=start_x, y=start_y)

        self.pendown()

        self.sety(y=DISTANCE_FROM_BORDER - self.__half_height)

        self.setx(x=DISTANCE_FROM_BORDER - self.__half_width)

        self.sety(y=self.__half_height - DISTANCE_FROM_BORDER)

        self.setx(self.__half_width - DISTANCE_FROM_BORDER)

    def __place_title(self):
        self.penup()
        y = self.__half_height - DISTANCE_FROM_BORDER - 100
        self.goto(x=0, y=y)

        self.write(TITLE_TEXT, align="center", font=FONT)

    def start_game(self, a, b):
        self.start_btn.reset()
        self.start_btn.hideturtle()

        self.reset()
        self.hideturtle()
        self.speed(0)
        self.draw_border()

        self.start = True

