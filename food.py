from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
