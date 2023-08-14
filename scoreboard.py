from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.color("black")
        self.setpos(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over.", align="center", font=("Courier", 24, "normal"))
