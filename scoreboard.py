from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Ariel', 8, 'bold')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()    
    self.penup()
    self.pencolor('white')
    self.goto(x=0, y=280)
    self.hideturtle()
    self.score = 0
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    
    
  def score_count(self):   
    self.clear()
    self.score += 1
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)