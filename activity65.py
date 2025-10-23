import turtle

screen = turtle.Screen()
screen.title("Colorful Square Design by Dharani")

screen.bgcolor("lightblue")

artist = turtle.Turtle()
artist.pensize(4)
artist.speed(5)

colors = ["red", "green", "blue", "orange"]

for color in colors:
    artist.color(color)
    artist.forward(100)
    artist.right(90)

artist.penup()
artist.goto(-50, -50)
artist.pendown()
artist.color("purple")
artist.circle(100)

artist.hideturtle()

screen.exitonclick()
