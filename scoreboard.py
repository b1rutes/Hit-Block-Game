import json
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,0)

    def end_game(self,level,score):
        self.clear()
        self.write(
            f"GAME OVER\nBlocks hit: {score}\nLevel: {level}",
            align="center",
            font=("Arial", 24, "bold"),
        )

    def update_highscore(self,level,score):
        new_highscore = {"Level":level,
                         "Score":score}
        try:
            with open("highscore.json","r") as highscore_file:
                data = json.load(highscore_file)
                if (level, score) > (data.get("Level", 0), data.get("Score", 0)):
                    data.update(new_highscore)
        except FileNotFoundError:
            with open("highscore.json","w") as highscore_file:
                json.dump(new_highscore,highscore_file,indent=4)
        else:
            with open("highscore.json","w") as highscore_file:
                json.dump(data,highscore_file,indent=4)

    def get_highscore(self):
        try:
            with open("highscore.json", "r") as highscore_file:
                data = json.load(highscore_file)
        except FileNotFoundError:
            highscore_level = 0
            highscore_blocks = 0
        else:
            highscore_level = data.get("Level", 0)
            highscore_blocks = data.get("Score", 0)
        finally:
            current_highscore = f"High score: Level {highscore_level} | Blocks: {highscore_blocks}"

        return current_highscore