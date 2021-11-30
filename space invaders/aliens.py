from turtle import Turtle
from random import randint
from time import sleep
import gc
import threading
import queue
from player import Player
from barrier import Barrier
from score_board import scoreboard, DrawScoreBoard
import pathlib

graphics = queue.Queue(1)
draw_scoreboard = DrawScoreBoard()
base_path = pathlib.Path(__file__).parent.resolve()

SLEEP_TIME = 1
TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y = 1000, 1000
DISTANCE_FROM_BARRIER = 50
MOVEMENT_INCREMENT = 5


class AlienBaseClass(Turtle):
    def __init__(self):
        super(AlienBaseClass, self).__init__()
        self.penup()

        self.is_dead = False
        self.alien_move_distance = 5

        self.screen = self.getscreen()

    def move(self):
        while True:
            sleep(SLEEP_TIME)
            current_coord = self.ycor()
            self.sety(current_coord - self.alien_move_distance)
            self.screen.update()

            all_barriers = [turtle for turtle in self.screen.turtles() if
                            (not isinstance(turtle, Player) and isinstance(turtle, Barrier))]
            for barrier_obj in all_barriers:
                if self.distance(barrier_obj) < DISTANCE_FROM_BARRIER:
                    barrier_obj.hideturtle()
                    self.hideturtle()

                    barrier_obj.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                    self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                    self.screen.update()

            player_obj = [turtle for turtle in self.screen.turtles() if isinstance(turtle, Player)][0]
            if self.distance(player_obj) < DISTANCE_FROM_BARRIER:
                self.hideturtle()
                self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                scoreboard.player_lives -= 1
                draw_scoreboard.write_score()

                if scoreboard.player_lives == 0:
                    quit()

            if self.ycor() < -400:
                self.hideturtle()
                self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                self.screen.update()
                del self
                gc.collect()
                return


class Alien1(AlienBaseClass):
    ICON = f"{base_path}/images/alien1.gif"

    def __init__(self):
        super(Alien1, self).__init__()
        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


class Alien2(AlienBaseClass):
    ICON = f"{base_path}/images/alien2.gif"

    def __init__(self):
        super(Alien2, self).__init__()

        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


class Alien3(AlienBaseClass):
    ICON = f"{base_path}/images/alien3.gif"

    def __init__(self):
        super(Alien3, self).__init__()

        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


ALIEN1_START, ALIEN1_END = 30, 30
ALIEN2_START, ALIEN2_END = 0, 20
ALIEN3_START, ALIEN3_END = 0, 10
START_COORD_X, START_COORD_Y = -350, 200


def increase_dif(alien_obj):
    alien_obj.alien_move_distance += MOVEMENT_INCREMENT


def gen_level():
    aliens_1 = [Alien1 for _ in range(randint(ALIEN1_START, ALIEN1_END))]
    aliens_2 = [Alien2 for _ in range(randint(ALIEN2_START, ALIEN2_END))]
    aliens_3 = [Alien3 for _ in range(randint(ALIEN3_START, ALIEN3_END))]

    step_x, step_y = 0, 0

    for alien in aliens_1:
        alien_obj = alien()
        alien_obj.goto(START_COORD_X + step_x, START_COORD_Y + step_y)
        alien_obj.showturtle()
        alien_obj.screen.update()

        if alien_obj.xcor() > 330:
            step_y -= 50
            step_x = 0
            print(step_y)
        else:
            step_x += 50

        thread = threading.Thread(target=alien_obj.move)
        thread.daemon = True
        thread.start()
