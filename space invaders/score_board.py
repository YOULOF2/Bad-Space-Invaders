from turtle import Turtle

PRIMARY_PEN_COLOUR = "#FF0000"
SECONDARY_PEN_COLOUR = "#0000FF"

CORNER_COORD = 390


def draw_border():
    def draw_square(pen_size):
        border.pensize(pen_size)
        border.goto(CORNER_COORD, CORNER_COORD)
        border.pendown()
        border.goto(CORNER_COORD, -CORNER_COORD)
        border.goto(-CORNER_COORD, -CORNER_COORD)
        border.goto(-CORNER_COORD, CORNER_COORD)
        border.goto(CORNER_COORD, CORNER_COORD)
        border.penup()

    border = Turtle()
    screen = border.getscreen()
    border.hideturtle()
    border.penup()

    border.pencolor(PRIMARY_PEN_COLOUR)
    draw_square(8)

    border.pencolor(SECONDARY_PEN_COLOUR)
    draw_square(4)
