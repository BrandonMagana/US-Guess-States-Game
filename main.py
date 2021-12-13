import turtle
import pandas as pd

"""
    Check is a given state is in the current dataframe column
    
    Arguments:
        states(list): list from which is going to check if the given state name exists in
        answer_state(str): string that represents the state to be checked
    
    Returns:
        (bool) indicate whether the state is valid or not
"""
def state_exists(states, answer_state):
    return answer_state in states

"""
    Check is a given state is in the current dataframe column
    
    Arguments:
        states_df(pandas.DataFrame): pandas Dataframe from which is going to retrieve a given state
        answer_state(str): string that represents the state 
    
    Returns:
        coors(tuple): tuple that contains the x and y coordinates of the state
"""

def get_state_coor(states_df, answer_state):
    state = states_df[states_df["state"] == answer_state]
    x = int(state.x)
    y = int(state.y)
    coors = (x, y)
    return coors

"""
    Creates a new .csv file that contains the unguessed states names.
    
    Arguments:
        states(list): list of all names of the states
        states_guessed(list): list that contains the name of the states that have ben guessed
    
    Returns:
        None
"""
def create_states_to_learn_file(states, states_guessed):
    #Fill the states_to_learn list with the names of the states that couldn't be guessed
    states_to_learn = [state for state in states if state not in states_guessed]
   
    #Generate a pandas.DataFrame from a dictionary
    to_learn_dict = {
        "States to learn" : states_to_learn
    }
    states_to_learn_df = pd.DataFrame(to_learn_dict)

    #Create .csv file from dictionary
    states_to_learn_df.to_csv("States_to_learn.csv")

if __name__ == '__main__':

    #Setting up screen
    screen = turtle.Screen()
    screen.title("U.S States Game")

    #Adding image as screen background
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    #Getting the states from a .csv files and turning them into a list
    df  = pd.read_csv("50_states.csv")
    states = df.state.to_list()
    #List that contains the states that have been guessed
    states_guessed = []

    #Game Logic
    while len(states_guessed) < 50:
        #Display input window  and format the given answer
        answer_state = screen.textinput(f"{len(states_guessed)}/50 States Guessed", 
                                        "What's another state's name?: ").title()

        #Check if user wants to end the game before winning and stop it if so.
        #Also creates a .csv file with the unguessed states names
        if answer_state == "Exit":
            create_states_to_learn_file(states, states_guessed)
            print(f"Keep practicing you guessed {len(states_guessed)}/50 States")
            print("Check out the States you got to learn at States_to_learn.csv File")
            break
        
        #Writes the name of the state on top of the image and appends it to the states_guessed list
        if state_exists(states, answer_state):
            states_guessed.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            coors = get_state_coor(df, answer_state)
            t.goto(x = coors[0], y = coors[1])
            t.write(answer_state)

    #Display winning message
    if(len(states_guessed) == 50):
        print("Congratulations, you guessed all the US states!")

    #The turtle.screen window is shut down
    screen.bye()