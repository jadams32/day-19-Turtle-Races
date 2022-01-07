# For the main project for day 19 I create a turtle race game. The user gets to place a bet on which turtle.
# will reach the finish line first. Feel free to poke around a bit, and have fun betting!

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet!", prompt="Pick a turtle to win the race! Select color:")
placed_bet = False
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_locations = [160, 100, 40, -20, -80, -140]
turtles = []
for num in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[num])
    new_turtle.goto(x=-230, y=y_locations[num])
    turtles.append(new_turtle)

if user_bet:
    placed_bet = True

while placed_bet:
    for turtle in turtles:
        if turtle.xcor() > 230:
            placed_bet = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"The {winner} turtle has won! You win!")
            else:
                print(f"The {winner} turtle has won! You lose.")
        turtle.forward(random.randint(0, 20))


screen.exitonclick()
