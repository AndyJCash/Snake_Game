from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # makes shape half of default to 10x10cm
        self.refresh()

    def refresh(self):
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 280)
        self.goto(x_food, y_food)
