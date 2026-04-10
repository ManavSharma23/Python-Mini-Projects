#importing modules
import turtle
import pandas as pd

data=pd.read_csv("50_states.csv")
# naming variables
all_states=data.state.tolist()
guessed_states=[]

screen = turtle.Screen()
screen.title("Guess the States")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_states)<50:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 Correctly Guessed",prompt="State Name ").title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==answer_state]
        t.goto(state_data["x"].item(),state_data["y"].item())
        t.write(answer_state)

screen.exitonclick()