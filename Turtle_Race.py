import random
from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=500,height=400)
colors=['red','yellow','green','blue','black','violet']
turtles=[]

user_bet=screen.textinput(title="Make Your Bet",prompt="Make Your Bet On Who Is Winning : ")

current_x=-200
current_y=-130


for i in range(len(colors)):
    new_turtle=Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(current_x, current_y)
    current_y=current_y+50
    turtles.append(new_turtle)

if user_bet:
    game_on=True

while game_on :

    for i in turtles:
        if i.xcor()>225:
            game_on=False
            print("Game Over")
            winning_Turtle=i
            if user_bet==winning_Turtle:
                print(f"You Have Won The Bet ,{i.pencolor()} Turtle is the winner")
            else:
                print(f"You Have Lost The Bet ,{i.pencolor()} Turtle is the winner")

        distance=random.randint(0,10)
        i.forward(distance)

screen.exitonclick()
