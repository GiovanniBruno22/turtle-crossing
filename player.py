from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen.tracer(0)
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(0, self.ycor() - MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
