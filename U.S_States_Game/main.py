import csv

import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

tim = turtle.Turtle()
tim.hideturtle()

correct_Number = 0

correct_states = []

tim.penup()
while correct_Number < 50:
    if correct_Number < 1:
        answer_state = screen.textinput(title=f"Guess the State", prompt="What's another state's name? (Type 'exit' to end game.)")
    else:
        answer_state = screen.textinput(title=f"{correct_Number}/50 States Correct", prompt="What's another state's name? (Type 'exit' to end game.)")
    for state in data.loc[:,"state"]:
        if state.lower() == answer_state.lower() and state not in correct_states:
            correct_states.append(state)
            current_state = data[data.state == state]
            x_position = current_state.x[current_state.index[0]]
            y_position = current_state.y[current_state.index[0]]
            tim.setpos(x_position,y_position)
            tim.write(f"{state}")
            correct_Number += 1
    if answer_state.lower() == "exit":
        missing_states = [state for state in data.loc[:,"state"] if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        with open("states_to_learn.csv", 'r') as csvfile: 
            content = csv.reader(csvfile)
            new_lines = []
            for lines in content:
                if lines[1] in missing_states:
                    new_lines.append(lines[1])
                    new_lines.append("\n")
    
        with open("U.S_States_Game/states_to_learn.csv", 'w') as file:
            file.writelines(new_lines)
        break
tim.setpos(-150,0)
if correct_Number == 50:
    tim.write("You win!", font=('Times New Roman', 50, 'normal'))
else:
    tim.speed('fastest')
    for state in missing_states:
        current_state = data[data.state == state]
        x_position = current_state.x[current_state.index[0]]
        y_position = current_state.y[current_state.index[0]]
        tim.setpos(x_position,y_position)
        tim.pencolor('red')
        tim.write(f"{state}")
    tim.write("You lose", font=('Times New Roman', 50, 'normal'))
turtle.mainloop()
