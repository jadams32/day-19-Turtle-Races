# For the main project for day 19 I create a turtle race game. The user gets to place a bet on which turtle.
# will reach the finish line first. Feel free to poke around a bit, and have fun betting!

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet!", prompt="Pick a turtle to win the race! Select color:")

colors = ["red", "orange", "green", "yellow", "blue", "purple"]
y_locations = [160, 100, 40, -20, -80, -140]

for num in range(6):
    john = Turtle(shape="turtle")
    john.penup()
    john.color(colors[num])
    john.goto(x=-230, y=y_locations[num])


screen.exitonclick()