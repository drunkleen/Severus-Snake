from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random_shape())
        self.color(random_color())
        self.penup()
        self.speed(0)
        self.goto(random.randint(-380, 380), random.randint(-380, 380))
        self.random_new_food()

    def random_new_food(self):
        self.shape(random_shape())
        self.color(random_color())
        self.goto(random.randint(-380, 380), random.randint(-380, 380))


def random_shape():
    return random.choice(['circle', 'triangle', 'square'])


def random_color():
    return random.randint(150, 255), random.randint(150, 255), random.randint(150, 255)
