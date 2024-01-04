import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = pd.read_csv("50_states.csv")

# def get_mouse_click_coor(x, y):
#    print(x, y) <- gets you coordinates of places on screen as you click.
#
# turtle.onscreenclick(get_mouse_click_coor)


def turtle_setup(x_coord, y_coord):
    answered = turtle.Turtle()
    answered.hideturtle()
    answered.penup()
    answered.goto(x_coord, y_coord)
    return answered


def write_name(state_name):
    turtle_setup(x_coord=x, y_coord=y).write(arg=state_name, align="center")


answered_correct = []
answer_state = screen.textinput(title="Guess The State!", prompt="What's another state's name?").title()

while len(answered_correct) < 50:
    if answer_state == "Exit":
        missed_states = [state for state in all_states.state if state not in answered_correct]
        df = pd.DataFrame(missed_states)
        df.to_csv("states-you-missed.csv")
        break

    # iloc[] (or .item() function) removes index, leaving only singular input
    if all_states["state"].isin([answer_state]).any() and answer_state not in answered_correct:
        state_data = all_states[all_states.state == answer_state]
        x = state_data.x.iloc[0]
        y = state_data.y.iloc[0]
        write_name(state_name=answer_state)
        answered_correct.append(answer_state)

    answer_state = screen.textinput(title=f"{len(answered_correct)}/50 correct!",
                                    prompt="What's another state's name?").title()

turtle.mainloop()
answer_state.split()