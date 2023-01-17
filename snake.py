from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_tail(pos)

    def add_tail(self, pos):
        new_segment = Turtle('square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def tail_extend(self):
        self.add_tail(self.segments[-1].position())

    def move_snake(self):
        # Snake tail moving with snake head
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)

        # Snake Moving through Walls
        if self.snake_head.position()[0] >= 381:
            self.snake_head.goto(-380, self.snake_head.position()[1])
        elif self.snake_head.position()[0] <= -381:
            self.snake_head.goto(380, self.snake_head.position()[1])
        elif self.snake_head.position()[1] >= 381:
            self.snake_head.goto(self.snake_head.position()[0], -380)
        elif self.snake_head.position()[1] <= -381:
            self.snake_head.goto(self.snake_head.position()[0], 380)
        else:
            self.snake_head.forward(MOVE_DISTANCE)

    # KeyStrokes
    def up(self):
        if self.snake_head.heading() != DOWN: self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP: self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT: self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT: self.snake_head.setheading(RIGHT)
