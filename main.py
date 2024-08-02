from turtle import Turtle, Screen
#importing the Turtle class and the Screen class from the turtle module
timmy = Turtle()
#The Turtle class allows us to create a turtle object that we can control to draw on the screen.
#The Screen class provides a canvas (or window) where our turtle can move and draw.
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.right(90)
screen = Screen()
print(screen.canvheight)
screen.exitonclick()
