from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
#create screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("PONG GAME")
screen.tracer(0)#which controls the animation

r_paddle = Paddle((350,0))#position value in one variable so passed in single parameter
l_paddle = Paddle((-350, 0))
ball = Ball()
# screen listeners

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_on = True
while game_on :
  time.sleep(0.1)
  screen.update()
  ball.move()

#detect the collision













screen.exitonclick()