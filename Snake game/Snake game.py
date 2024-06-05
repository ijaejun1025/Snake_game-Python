from turtle import Turtle, Screen
import pygame
import time
import random

pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\USER\Desktop\Snake game\Background music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# Screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Keyboard
def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)
        
def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)
        
def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Apple
def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y

apple = Turtle()
apple.shape("circle")
apple.color("red")
apple.up()
apple.speed(0)
apple.goto(rand_pos())

# Scoreboard
def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"Score : {score}", font = ("", 15, "bold"))

score = 0
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.pencolor("white")
score_pen.write(f"Score : {score}", font = ("", 15, "bold"))

# Snake
def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("green")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

start_pos = [(0,0), (-20,0), (-40,0)]
snakes = []

for pos in start_pos:
    create_snake(pos)

# Gameover
def game_over():
    score_pen.goto(0,0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))
    pygame.mixer.music.stop()
    pygame.mixer.music.load(r"C:\Users\USER\Desktop\Snake game\Game over.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

# Main function
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snakes) - 1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
    
    snakes[0].forward(10)
    
    # When a snake hits the apple
    if snakes[0].distance(apple) < 15:
        score_update()
        apple.goto(rand_pos())
        create_snake(snakes[-1].pos())

    # When a snake hits the wall
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
        game_on = False
        game_over()
    
    # When a snake hits its own tail
    for body in snakes[1:]:
        if snakes[0].distance(body) < 8:
            game_on = False
            game_over()

screen.exitonclick()