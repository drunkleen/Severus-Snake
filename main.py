import time
from turtle import Screen

from food import Food
from score import Scoreboard
from snake import Snake

# Screen Setup
screen = Screen()
screen.colormode(255)
screen.bgcolor((0, 0, 0))
screen.setup(width=800, height=800)
screen.title("Severus Snake")
screen.tracer(0)

# Snake Setup
snake = Snake()
food = Food()
score = Scoreboard()

# KeyBinding
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

# Main Game Loop
game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Check if snake eat the food
    if snake.snake_head.distance(food) <= 25:
        food.random_new_food()
        score.add_score()
        snake.tail_extend()

    # Check if snake eats itself
    for segment in snake.segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) <= 10:
            game_running = False

screen.mainloop()
