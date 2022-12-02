import turtle
import pandas
screen = turtle.Screen()
screen.title("US game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
game_on = True
guessed_states = []
all_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Whats another state's name?").title()
    if answer_state == "Exit":
        break
    missing_states = [state1 for state1 in all_states if state1 not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("States to Learn")
    for state in data["state"]:
        if answer_state == state:
            correct_answer = answer_state
            row_of_correct_answer = data[data.state == f"{correct_answer}"]
            x = int(row_of_correct_answer["x"])
            y = int(row_of_correct_answer["y"])
            timmy = turtle.Turtle()
            timmy.penup()
            timmy.hideturtle()
            timmy.goto(x, y)
            timmy.write(f"{correct_answer}")
            guessed_states.append(f"{correct_answer}")
            print(missing_states)

