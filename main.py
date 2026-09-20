from ball import Ball, Duplicate
from block import Block
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen



WIDTH_LIMIT = 380
TOP_LIMIT = 290
BALL_LOSS_LIMIT = -280
FRAME_DELAY = 16


def run_game():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Hit Block")
    screen.bgcolor("black")
    screen.tracer(0)

    paddle = Paddle()
    ball = Ball()
    duplicates = Duplicate()
    blocks = Block()
    scoreboard = Scoreboard()
    level = 1
    score = 0
    rows = 1
    game_over = False
    highscore = scoreboard.get_highscore()

    screen.listen()
    screen.onkey(paddle.r_move, "Right")
    screen.onkey(paddle.l_move, "Left")

    def game_tick():
        nonlocal level, score, rows, game_over,highscore
        if game_over:
            return

        screen.update()
        ball.move()
        current = ball.current_ball.turtle
        screen.title(
            f"HIT BLOCK | Level: {level} | Blocks: {score} | Lives: {ball.remaining_lives()} "
            f"{highscore}"
        )

        if current.xcor() >= WIDTH_LIMIT or current.xcor() <= -WIDTH_LIMIT:
            ball.side_walls_bounce()
        if current.ycor() >= TOP_LIMIT:
            ball.up_walls_bounce()
        if current.distance(paddle) < 50 and current.ycor() < -260:
            ball.up_walls_bounce()

        hit_block = next(
            (
                game_block
                for game_block in blocks.all_blocks
                if current.distance(game_block) < 20
                and current.ycor() > 90
            ),
            None,
        )
        if hit_block is not None:
            score += 1
            is_bonus = hit_block.color()[0] == "brown"
            bonus_position = hit_block.pos()
            blocks.remove_blocks(hit_block)
            ball.up_walls_bounce()
            if is_bonus and score % 3 == 0:
                duplicates.create_dups(bonus_position)

        for duplicate in duplicates.duplicate_balls:
            duplicate_turtle = duplicate.turtle
            hit_block = next(
                (
                    game_block
                    for game_block in blocks.all_blocks
                    if duplicate_turtle.distance(game_block) < 20
                    and duplicate_turtle.ycor() > 90
                ),
                None,
            )
            if hit_block is not None:
                blocks.remove_blocks(hit_block)
                duplicate.bounce_vertical()
                score += 1

        if duplicates.duplicate_balls:
            duplicates.duplicates_move(paddle)
        duplicates.kill_duplicates()

        if blocks.empty_blocks():
            level += 1
            rows += 1
            blocks.reset()
            blocks.create(rows)
            ball.start_ball()

        if current.ycor() < BALL_LOSS_LIMIT and not duplicates.duplicate_balls:
            if not ball.next_ball():
                game_over = True
            else:
                ball.start_ball()

        if game_over:
            scoreboard.end_game(level, score)
            scoreboard.update_highscore(level, score)
            screen.update()
            return

        screen.ontimer(game_tick, FRAME_DELAY)

    game_tick()
    screen.mainloop()


if __name__ == "__main__":
    run_game()