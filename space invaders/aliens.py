from turtle import Turtle
from time import sleep
import gc
import threading
import queue
import pathlib
from random import randint

from player import Player
from barrier import Barrier
from score_board import scoreboard, DrawScoreBoard

graphics = queue.Queue(1)
draw_scoreboard = DrawScoreBoard()
base_path = pathlib.Path(__file__).parent.resolve()

SLEEP_TIME = 1
TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y = 1000, 1000
DISTANCE_FROM_BARRIER = 50
DISTANCE_FROM_PLAYER = 50
MOVEMENT_INCREMENT = 5


class AlienBaseClass(Turtle):
    def __init__(self):
        super(AlienBaseClass, self).__init__()
        self.penup()

        self.is_dead = False
        self.alien_move_distance = 5

        self.screen = self.getscreen()

    def shoot(self):
        """
        This method is empty as it will be overwritten by Alien 3 class
        :return:
        :rtype:
        """
        pass

    def move(self):
        while True:
            sleep(SLEEP_TIME)
            current_coord = self.ycor()
            self.sety(current_coord - self.alien_move_distance)
            self.screen.update()

            all_aliens = [turtle for turtle in self.screen.turtles() if
                          (not isinstance(turtle, Player) and isinstance(turtle, Barrier))]
            for alien_obj in all_aliens:
                if self.distance(alien_obj) < DISTANCE_FROM_BARRIER:
                    alien_obj.hideturtle()
                    self.hideturtle()

                    alien_obj.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                    self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                    self.screen.update()

            player_obj = [turtle for turtle in self.screen.turtles() if isinstance(turtle, Player)][0]
            if self.distance(player_obj) < DISTANCE_FROM_PLAYER:
                self.hideturtle()
                self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                scoreboard.player_lives -= 1
                draw_scoreboard.write_score()

                if scoreboard.player_lives == 0:
                    break

            if randint(0, 20) == 1:
                self.shoot()

            if self.ycor() < -400:
                self.hideturtle()
                self.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                self.screen.update()
                del self
                gc.collect()
                break


class Alien1(AlienBaseClass):
    ICON = f"{base_path}/images/alien1.gif"
    START_COORD_X, START_COORD_Y = -350, 200

    def __init__(self):
        super(Alien1, self).__init__()
        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


class Alien2(AlienBaseClass):
    ICON = f"{base_path}/images/alien2.gif"
    START_COORD_X, START_COORD_Y = -350, 205

    def __init__(self):
        super(Alien2, self).__init__()

        self.screen.register_shape(self.ICON)
        self.shape(self.ICON)


class Alien3(AlienBaseClass):
    ICON = f"{base_path}/images/alien3.gif"
    BEAM_ICON = f"{base_path}/images/alien3_beam.gif"
    BEAM_COLOUR = "#800000"
    START_COORD_X, START_COORD_Y = -350, 210
    SLEEP_TIME = 0.1

    def __init__(self):
        super(Alien3, self).__init__()

        self.screen.register_shape(self.ICON)
        self.screen.register_shape(self.BEAM_ICON)

        self.shape(self.ICON)

    def shoot(self):
        beam = Turtle()
        beam.hideturtle()
        beam.shape("square")
        beam.shapesize(stretch_wid=0.5, stretch_len=2)
        beam.penup()
        beam.color(self.BEAM_COLOUR)
        beam.speed(0)
        beam.setheading(270)
        beam.showturtle()
        beam.goto(self.xcor(), self.ycor() - 50)

        while True:
            sleep(self.SLEEP_TIME)
            self.screen.update()
            beam.forward(20)

            barriers = [turtle for turtle in self.screen.turtles() if isinstance(turtle, Barrier)]
            for barrier in barriers:
                if beam.distance(barrier) < DISTANCE_FROM_BARRIER:
                    barrier.hideturtle()
                    beam.hideturtle()

                    barrier.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                    beam.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                    self.screen.update()
                    break

            player_obj = [turtle for turtle in self.screen.turtles() if isinstance(turtle, Player)][0]
            if beam.distance(player_obj) < DISTANCE_FROM_PLAYER:
                player_obj.reset_player()
                scoreboard.player_lives -= 1
                draw_scoreboard.write_score()

                beam.hideturtle()
                beam.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                self.screen.update()

            if beam.ycor() < -400:
                beam.hideturtle()
                beam.goto(TURTLE_HIDE_LOCATION_X, TURTLE_HIDE_LOCATION_Y)
                self.screen.update()
                del beam
                gc.collect()

                break


# The length of the screen, allows rows of 15 Alien1s
ALIEN1_NUM = 30
ALIEN2_NUM = 15
ALIEN3_NUM = 15


def increase_dif(alien_obj):
    alien_obj.alien_move_distance += MOVEMENT_INCREMENT


def gen_level():
    aliens_1 = [Alien1 for _ in range(ALIEN1_NUM)]
    aliens_2 = [Alien2 for _ in range(ALIEN2_NUM)]
    aliens_3 = [Alien3 for _ in range(ALIEN3_NUM)]
    all_aliens = aliens_3 + aliens_2 + aliens_1

    step_x, step_y = 0, 0

    for alien in all_aliens:
        alien_obj = alien()
        alien_obj.goto(alien.START_COORD_X + step_x, alien.START_COORD_Y + step_y)
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
