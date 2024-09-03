from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):#the parameters passed by the paddle arugments in main
       super().__init__()
       # create and move the paddle

       self.shape("square")
       self.color("white")
       self.shapesize(stretch_wid=5, stretch_len=1)
       self.penup()
       self.goto(position)#the parameters are passed in it

    def  go_up(self):
          new_y = self.ycor() + 20
          self.goto(self.xcor(), new_y)

    def go_down(self):
          new_y = self.ycor() - 20
          self.goto(self.xcor(), new_y)

