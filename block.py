from random import choice
from turtle import Turtle

class Block:
    def __init__(self):
        self.start_rows = 1
        self.all_blocks = []
        self.colors = ["blue","orange","red","green","purple","yellow","brown"]
        self.x_position = -380
        self.y_position = 290
        self.create(self.start_rows)

    def create(self,block_rows):
        for _ in range(block_rows):
            for n in range(19):
                block = Turtle("square")
                block.color(choice(self.colors))
                block.shapesize(stretch_wid=0.9, stretch_len=2)
                block.penup()
                block.goto(self.x_position,self.y_position)
                self.x_position += 41.7
                self.all_blocks.append(block)
            self.y_position -= 20
            self.x_position = -380

    def remove_blocks(self,rem_block):
        if rem_block in self.all_blocks:
            self.all_blocks.remove(rem_block)
            rem_block.goto(500, 500)

    def reset(self):
        self.y_position = 290

    def empty_blocks(self):
        if not self.all_blocks:
            return True
        else:
            return False
