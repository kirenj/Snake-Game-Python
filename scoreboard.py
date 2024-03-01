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
    self.score_reading()
    self.show_score()

  # def game_over(self):
  #   self.goto(x=0, y=0)
  #   self.write("GAME OVER", align=ALIGNMENT, font=F_FONT)

  def show_score(self):
    self.clear()
    self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def score_count(self):
    # self.clear()
    self.score += 1
    self.show_score()

  def score_reset(self):
    if self.score > self.high_score:
      update_score = str(self.score)
      with open('data.txt', mode='w') as file:
        file.write(update_score)
      self.score_reading()
      self.score = 0
      self.show_score()

  def score_reading(self):
    with open('data.txt', mode='r') as file:
      old_score = file.read()
    self.high_score = int(old_score)
