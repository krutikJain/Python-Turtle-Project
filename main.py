from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(500, 400)
race_on = False
guess = scr.textinput("Turtle Race", "Guess Which Turtle will win?")
allTurtle = []
color = ["red", "orange", "yellow", "green", "blue", "purple"]
index = [-100, -70, -40, -10, 20, 50]
for turtle in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.goto(-230, index[turtle])
    newTurtle.color(color[turtle])
    allTurtle.append(newTurtle)

if guess:
    race_on = True

while race_on:
    for turtle in allTurtle:
        if turtle.xcor() > 230:
            race_on = False
            win = turtle.pencolor()
            if win == guess:
                print(f"Yooo You Won, {win} Turtle came First")
            else:
                print(f"Booo You Lose, {win} Turtle came First")
        else:
            turtle.forward(random.randint(0, 10))

scr.exitonclick()
