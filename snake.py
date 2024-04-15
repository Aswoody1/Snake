from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    from turtle import Turtle, Screen

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = self.head.heading()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
        self.direction = self.head.heading()


    def left(self):
        if self.direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.direction != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.direction != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
