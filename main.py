from turtle import *
import pandas


from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S State Game")
image = 'blank_states_img.gif'
screen.addshape(image)

jimmy = Turtle()
jimmy.shape(image)

data = pandas.read_csv('50_states.csv')


def moving_answer():
    damesh = Turtle()
    damesh.clear()
    damesh.hideturtle()
    damesh.penup()
    damesh.goto(int(state_data.x), int(state_data.y))
    damesh.write(arg=guess_answer, move=False, align="center", font=("Courier", 10, "normal"))


game_on = True
correct_answer = 0

while game_on:

    guess_answer = screen.textinput(title=f"{correct_answer} /50 Guess the State", prompt="What's the next state name?").title()
    state_data = (data[data.state == guess_answer])
    state = state_data.state

    if state.empty == False:
        moving_answer()
        correct_answer += 1

    if correct_answer == 50:
        game_on = False

screen.exitonclick()
