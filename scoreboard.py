from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Ariel', 8, 'bold')
F_FONT = ('Ariel', 15, 'bold')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()    
    self.penup()
    self.pencolor('white')
    self.goto(x=0, y=280)
    self.hideturtle()
    self.score = 0
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
  def game_over(self):
    self.goto(x=0, y=0)
    self.write("GAME OVER", align=ALIGNMENT, font=F_FONT)
    
    
  def score_count(self):   
    self.clear()
    self.score += 1
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)