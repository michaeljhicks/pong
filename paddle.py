from turtle import Turtle
# STARTING_POSITIONS = [(0, 0), (), ()]


class Paddle(Turtle):

    def __init__(self):
        super.__init__
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=100, stretch_wid=20)
        self.goto(x=350, y=0)

    def up():
