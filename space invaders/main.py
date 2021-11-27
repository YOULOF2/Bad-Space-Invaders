import tkinter
import turtle
from player import Player
from score_board import draw_border

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BG_COLOUR = "#000000"

# TODO: Create Alien Class

screen = turtle.Screen()
screen.bgcolor(BG_COLOUR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0, 0)

draw_border()

player = Player()

screen.listen()
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")
screen.onkey(player.shoot_bullet, "w")

if __name__ == "__main__":
    tkinter.mainloop()
