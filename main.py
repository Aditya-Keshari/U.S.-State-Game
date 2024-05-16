import turtle
from turtle import Turtle
import pandas

Screen=turtle.Screen()
Screen.title("U.S. State Game")
image= "blank_states_img.gif"
Screen.addshape(image)
turtle.shape(image)
drawer= Turtle()
drawer.hideturtle()
drawer.penup()

game_is_on= True
left=[]
correct_guess=[]
data=pandas.read_csv("50_states.csv")
state_list= data.state.to_list()

while game_is_on:
    Guess = Screen.textinput(title=f"{len(correct_guess)}/50 Correct Guress", prompt="What's another state name?").title()
    if Guess== "Exit":
        game_is_on= False
    if Guess in  state_list and Guess not in correct_guess:
        correct_guess.append(Guess)
        guess_row=data[data.state== Guess]
        drawer.goto(int(guess_row.x),int(guess_row.y))
        drawer.write(f"{Guess}",align="center")
        if  len(correct_guess)==50:
            game_is_on=False

left = [remaining for remaining in state_list if remaining not in correct_guess]
left_dict={"States to learn": left}
df=pandas.DataFrame(left_dict)
df.to_csv("states_to learn")