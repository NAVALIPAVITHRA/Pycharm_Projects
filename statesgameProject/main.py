from turtle import Turtle, Screen
import pandas as pd


# Set up the screen
screen = Screen()
t = Turtle()
screen.bgcolor("white")
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
#screen.addshape(image): Registers the image as a shape that can be used by the turtle.
#t.shape(image): Sets the turtle’s shape to the specified image, making it visible on the screen.
screen.addshape(image)
t.shape(image)


data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []
while len(guessed_states)<50 :

 user_input  = screen.textinput(title = f"{len(guessed_states)}/50 states correct ",prompt = "whats the another state name ? ").title()
 print(user_input)
 if user_input == "Exit":
     missing_states = []
     for state in all_state:
         if state not in guessed_states:
             missing_states.append(state)
     print(missing_states)

     break
 if user_input in all_state:
    guessed_states.append(user_input)
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    state_data = data[data.state == user_input]
    print(state_data)
    t1.goto(state_data.x.item(),state_data.y.item())
    t1.write(state_data.state.item())

screen.exitonclick()
