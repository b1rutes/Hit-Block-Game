from random import choice
from turtle import Turtle


class GameBall:
    def __init__(self, position=(0, -215), x_speed=5, y_speed=5):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.shape("square")
        self.turtle.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.turtle.color("white")
        self.turtle.goto(position)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.turtle.goto(
            self.turtle.xcor() + self.x_speed,
            self.turtle.ycor() + self.y_speed,
        )

    def bounce_horizontal(self):
        self.x_speed *= -1

    def bounce_vertical(self):
        self.y_speed *= -1

    def reset(self, position=(0, -215)):
        self.turtle.goto(position)
        self.x_speed = choice((-5, 5))
        self.y_speed = 5

    def hide(self):
        self.turtle.goto(500, 500)


class Ball:
    def __init__(self, lives=3):
        self.spawn_position = (0, -215)
        self.all_balls = [
            GameBall(self.spawn_position, x_speed=5, y_speed=5)
        ]
        self.reserve_balls = [
            GameBall((500, 500), x_speed=5, y_speed=5)
            for _ in range(max(0, lives - 1))
        ]
        self.current_ball = self.all_balls[0]
        

    def move(self):
        self.current_ball.move()

    def side_walls_bounce(self):
        self.current_ball.bounce_horizontal()

    def up_walls_bounce(self):
        self.current_ball.bounce_vertical()

    def start_ball(self):
        self.current_ball.reset(self.spawn_position)

    def next_ball(self):
        if not self.reserve_balls:
            return False
        self.current_ball.hide()
        self.reserve_balls.pop(0)
        self.current_ball = GameBall(self.spawn_position)
        self.all_balls.append(self.current_ball)
        return True

    def remaining_lives(self):
        return len(self.reserve_balls) + 1


class Duplicate:
    def __init__(self):
        self.duplicate_balls = []

    def create_dups(self, position):
        if self.duplicate_balls:
            return
        self.duplicate_balls = [
            GameBall(position, x_speed=-5, y_speed=5),
            GameBall(position, x_speed=5, y_speed=5),
        ]

    def duplicates_move(self, paddle):
        for duplicate in self.duplicate_balls:
            duplicate.move()
            if duplicate.turtle.xcor() >= 380 or duplicate.turtle.xcor() <= -380:
                duplicate.bounce_horizontal()
            if duplicate.turtle.ycor() >= 290:
                duplicate.bounce_vertical()
            if (
                duplicate.turtle.distance(paddle) < 50
                and duplicate.turtle.ycor() < -260
            ):
                duplicate.bounce_vertical()

    def kill_duplicates(self):
        active = []
        for duplicate in self.duplicate_balls:
            if duplicate.turtle.ycor() < -280:
                duplicate.hide()
            else:
                active.append(duplicate)
        self.duplicate_balls = active

    def reset_duplicates(self):
        for duplicate in self.duplicate_balls:
            duplicate.hide()
            self.duplicate_balls.remove(duplicate)
        self.duplicate_balls = []    