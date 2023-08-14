import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()

    # Detect successful crossing
    if player.ycor() >= 280:
        player.reset_position()
        scoreboard.level_up()
        car_manager.level_up()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
