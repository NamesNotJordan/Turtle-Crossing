import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
scoreboard = Scoreboard()
cm = CarManager()

#Key Listeners
screen.listen()
screen.onkey(player.go_up,"w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cm.create_car()
    cm.move_cars()

    # Road Kill Detection
    for car in cm.all_cars:
        if car.distance(player) <20:
            game_is_on = False
    # Home free
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.reset_player()
        

screen.exitonclick()