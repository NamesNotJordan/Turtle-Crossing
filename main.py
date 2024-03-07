import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
scorenoard = Scoreboard()
cm = CarManager()

#Key Listeners
screen.onkey(player.go_up,"w")
screen.onkey(player.go_up,"up")

screen.onkey(player.go_back,"s")
screen.onkey(player.go_back,"down")

screen.onkey(player.go_left,"a")
screen.onkey(player.go_left,"left")

screen.onkey(player.go_right,"d")
screen.onkey(player.go_right,"right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
