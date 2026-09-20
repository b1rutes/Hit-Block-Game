from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -285)

    def r_move(self):
        self.setx(min(340, self.xcor() + 20))

    def l_move(self):
        self.setx(max(-340, self.xcor() - 20))