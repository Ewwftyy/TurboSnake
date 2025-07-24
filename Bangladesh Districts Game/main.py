import pandas
import turtle

screen = turtle.Screen()
screen.title("Bangladesh Districts Game")
screen.setup(width=450, height=600)

image = 'Bd_map.gif'

screen.bgpic(image)
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Bd_xy.csv")
all_districts = data.District.to_list()
guessed = []

correct = 0
total = len(all_districts)

while correct < total:
    ans = screen.textinput(title=f"{correct}/{total} Districts Correct",
                           prompt="What's the district's name? (Type 'Exit' to quit)").title()
    if ans == "Exit":
       t = turtle.Turtle()
       t.hideturtle()
       t.penup()
       t.goto(0,0)
       t.write(f"You have guessed {correct} correctly", align="center", font=("Arial", 20, "normal"))
       break
    if ans in all_districts and ans not in guessed:
        guessed.append(ans)
        correct += 1

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        dist = data[data.District == ans]
        x = int(dist.X.item()) - 225
        y = 300 - int(dist.Y.item())
        t.goto(x, y)
        t.write(dist.District.item(), align="center", font=("Arial", 8, "normal"))

    elif ans in guessed:
        screen.textinput(title="Already guessed!", prompt=f"You already guessed {ans}. Try again.")
    else:
        screen.textinput(title="Wrong!", prompt=f"{ans} is not a district name. Try again.")

screen.exitonclick()
