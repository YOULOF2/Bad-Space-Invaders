from turtle import Screen
from game_manager import GameManager
from player.player import Ship

BACKGROUND_IMG = "icons/background.gif"

screen = Screen()
screen.setup(width=1200, height=780)
screen.bgpic(BACKGROUND_IMG)
screen.tracer(0)

screen_width = screen.window_width()
screen_height = screen.window_height()

ship = Ship(screen)
gm = GameManager(screen, screen_width, screen_height, ship)

screen.listen()
screen.onkey(ship.move_right, "d")
screen.onkey(ship.move_left, "a")
screen.onkey(ship.shoot, "w")

screen.mainloop()
