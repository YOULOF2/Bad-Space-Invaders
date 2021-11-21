import logging
from turtle import Turtle

from global_vars import global_vars

DISTANCE_FROM_BORDER = 10

PEN_COLOUR_PRIMARY = "#00D58B"
PEN_COLOUR_SECONDARY = "#FFFFFF"
PEN_WIDTH_PRIMARY = 8
PEN_WIDTH_SECONDARY = 4

FONT = ("Arial", 50, "bold")
LIVES_FONT = ("Arial", 25, "bold")
TITLE_TEXT = "BAD Space Invaders"

START_BTN = "icons/start_btn.gif"

DISTANCE_BOTTOM_BORDER = -300


class GameManager(Turtle):
    __slots__ = "logger", "__half_width", "__half_height", "start_btn", "ship", "alien_dealer"

    def __init__(self, width: int, height: int):
        """
        
        :param width: 
        :param height: 
        """""
        super().__init__()

        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())

        self.speed(0)

        self.screen = global_vars.screen_obj
        self.__half_width = width / 2
        self.__half_height = height / 2

        self.hideturtle()

        self.__draw_border()
        self.__place_title()

        self.start_btn = Turtle()
        self.start_btn.goto(0, 0)
        self.screen.register_shape(START_BTN)
        self.start_btn.shape(START_BTN)
        self.start_btn.onclick(self.__start_game)

        self.ship = global_vars.ship_obj
        self.alien_dealer = global_vars.alien_dealer_obj

        self.screen.update()

        self.logger.info("WinManager class initialised")

    # Private classes
    def __draw_border(self):
        self.logger.info("Drawing border")
        self.__draw(PEN_WIDTH_PRIMARY, PEN_COLOUR_PRIMARY)
        self.__draw(PEN_WIDTH_SECONDARY, PEN_COLOUR_SECONDARY)

    def __draw(self, pen_width, pen_colour):
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
        self.logger.info("Placing title")
        self.penup()
        y = self.__half_height - DISTANCE_FROM_BORDER - 100
        self.goto(x=0, y=y)

        self.write(TITLE_TEXT, align="center", font=FONT)

    def __create_bottom_bar(self):
        self.pensize(PEN_WIDTH_PRIMARY)
        self.penup()
        self.pencolor(PEN_COLOUR_PRIMARY)
        self.goto(self.__half_width - DISTANCE_FROM_BORDER, DISTANCE_BOTTOM_BORDER)
        self.pendown()
        self.setx(-self.__half_width + DISTANCE_FROM_BORDER)

        self.pensize(PEN_WIDTH_SECONDARY)
        self.penup()
        self.pencolor(PEN_COLOUR_SECONDARY)
        self.goto(self.__half_width - DISTANCE_FROM_BORDER, DISTANCE_BOTTOM_BORDER)
        self.pendown()
        self.setx(-self.__half_width + DISTANCE_FROM_BORDER)

        self.screen.update()

    def update_player_health(self):
        self.penup()
        self.goto(-550, DISTANCE_BOTTOM_BORDER)
        self.write(f"Lives left: {self.ship.lives}", font=LIVES_FONT)

    def __start_game(self, *args):
        self.logger.info("Starting game")

        self.start_btn.hideturtle()
        del self.start_btn

        self.clear()
        self.__draw_border()
        self.__create_bottom_bar()
        self.screen.update()

        self.ship.init(self.__half_height)
        self.update_player_health()

        self.alien_dealer.next_stage()
