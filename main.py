from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
# turtle = Turtle()
# turtle.write("Score: ", move=False, align='center', font=('Ariel', 8, 'bold'))

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on is True:
  screen.update()
  time.sleep(0.1)

  snake.move()

  
  # Detect collision with food
  if snake.snakes[0].distance(food) < 15:
    score.score_count()
    food.refresh()
    
    
  
    














screen.exitonclick()