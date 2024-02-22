from turtle import Turtle

COORDINATES = ((0, 0), (-20, 0), (-60, 0))
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

  def __init__(self):
    # we will create a new list called 'snakes'. No need to make one outside the class.
    self.snakes = []
    self.create_snake()
    
  def create_snake(self):
    for i in COORDINATES:
      self.add_segment(i)

  def add_segment(self, position):
    new_segment = Turtle()    
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)    
    self.snakes.append(new_segment)
        
  def extend(self):
    # add a new segment to the snake
    self.add_segment(self.snakes[-1].position())
  
  
  
  def move(self):
    # creating 3 blocks and making them move
    # for segment in range(start=(len(snakes) - 1), stop = 0, step = -1)
    for segment in range((len(self.snakes) - 1), 0, -1):
      new_x = self.snakes[segment - 1].xcor()
      new_y = self.snakes[segment - 1].ycor()
      self.snakes[segment].goto(new_x, new_y)
    self.snakes[0].forward(MOVE_DISTANCE)


  def up(self):    
    if self.snakes[0].heading() != DOWN:
      self.snakes[0].setheading(UP)

  def down(self):    
    if self.snakes[0].heading() != UP:
      self.snakes[0].setheading(DOWN)

  def right(self):    
    if self.snakes[0].heading() != LEFT:
      self.snakes[0].setheading(RIGHT)

  def left(self):    
    if self.snakes[0].heading() != RIGHT:
      self.snakes[0].setheading(LEFT)
    


