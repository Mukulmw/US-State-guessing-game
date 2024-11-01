import turtle, pandas

data = pandas.read_csv("50_states.csv")
data = data.to_dict(orient="records")
print(data)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")


screen = turtle.Screen()
screen.title("US states game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

is_game_on = True
a = 0
while is_game_on:

    answer = screen.textinput(title=f"{a}/50 Guess the state", prompt="Guess the name of the state").lower()
    #print(answer)
    for i in data:
        state = i["state"].lower()
        #print(state)
        x = i["x"]
        #print(x)
        y = i["y"]

        if answer == "exit":
            break
        if state == answer:
            writer.teleport(x=x, y=y)
            writer.write(f"{answer}", font=("Arial", 10, "normal"))
            a += 1

screen.exitonclick()
