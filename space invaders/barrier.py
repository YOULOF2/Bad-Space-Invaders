from turtle import Turtle
from random import randint

RANGE_X_MIN, RANGE_X_MAX = -340, 340
RANGE_Y_MIN, RANGE_Y_MAX = -250, -250
RANDINT_RANGE_START, RANDINT_RANGE_END = 3, 10

STRETCH_WID, STRETCH_LEN = 1, 4

BARRIER_COLOUR = "#FFFFFF"


def barrier_gen():
    def create_turtle():
        class Barrier(Turtle):
            def __init__(self):
                super(Barrier, self).__init__()
                self.penup()
                self.color(BARRIER_COLOUR)
                self.shape("square")
                self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)

        return Barrier()

    for _ in range(randint(RANDINT_RANGE_START, RANDINT_RANGE_END)):
        random_x = randint(RANGE_X_MIN, RANGE_X_MAX)
        random_y = randint(RANGE_Y_MIN, RANGE_Y_MAX)

        barrier = create_turtle()
        screen = barrier.getscreen()
        barrier.goto(random_x, random_y)

        screen.update()
