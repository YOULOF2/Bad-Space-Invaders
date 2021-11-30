from turtle import Screen
from player import Player
from draw_border import draw_border
from barrier import BarrierGen
from aliens import gen_level

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BG_COLOUR = "#000000"

screen = Screen()
screen.bgcolor(BG_COLOUR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0, 0)

draw_border()

player = Player()
BarrierGen()
gen_level()

screen.listen()
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")
screen.onkey(player.shoot_bullet, "w")

if __name__ == "__main__":
    screen.mainloop()
