from turtle import Screen
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
    snake.extend()
    food.refresh()

  # Detect collision with wall
  if snake.snakes[0].xcor() > 285 or snake.snakes[0].xcor() < -285 or snake.snakes[0].ycor() > 285 or snake.snakes[0].ycor() < -285:
    # game_is_on = False
    score.score_reset()
    # score.game_over()
    snake.snake_reset()

  # Detect collision with tail
  for i in snake.snakes[1:]:
    if i == snake.snakes[0]:
      pass
    elif snake.snakes[0].distance(i) < 10:
      score.score_reset()
      snake.snake_reset()
      # game_is_on = False
      # score.game_over()

screen.exitonclick()
