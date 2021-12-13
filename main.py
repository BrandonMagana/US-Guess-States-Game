from tkinter.constants import S
import turtle
import pandas as pd

#Setting up screen
screen = turtle.Screen()
screen.title("U.S States Game")

#Adding image as screen background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#function for getting the states coordinates
# def get_mouse_on_click_coor(x, y):
#     print(x, y)
# screen.onclick(get_mouse_on_click_coor)

#Getting Pandas DataFrame
df  = pd.read_csv("50_states.csv")

def state_exists(states, answer_state):
    state = states[states["state"] == answer_state]
    return not state.empty

def get_state_coor(states, answer_state):
    state = states[states["state"] == answer_state]
    x = int(state.x)
    y = int(state.y)
    return (x, y)

states_guessed = []

while len(states_guessed) < 50:
    answer_state = screen.textinput(f"{len(states_guessed)}/50 States Guessed", "What's another state's name?: ").title()
    if answer_state == "Exit":
        screen.bye()
        break

    if state_exists(df, answer_state):
        states_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coors = get_state_coor(df, answer_state)
        t.goto(x = coors[0], y = coors[1])
        t.write(answer_state)

#States_to_learn.csv
states = df.state.to_list()
states_to_learn = []
for state in states:
    if state not in states_guessed:
        states_to_learn.append(state)


data_dict = {
    "States to learn" : states_to_learn
}

states_to_learn_df = pd.DataFrame(data_dict)

states_to_learn_df.to_csv("States_to_learn.csv")
print(f"Well done you guessed {len(states_guessed)}/50 States")
print("Check out the States you got to learn at States_to_learn.csv File")