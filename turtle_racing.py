import random
import turtle
import time

WIRDTH, HEIGHT = 500, 500
COLORS = ["red",
          "green",
          "blue",
          "orange",
          "yellow",
          "black",
          "purple",
          "pink",
          "brown",
          "cyan"
          ]

screen = turtle.Screen()
screen.setup(WIRDTH, HEIGHT)
screen.title("Turtle Racing")
def get_num_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10) ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric ... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number in range 2-10 ... Try again!")


def create_turtles(colors):
    turtles = []
    spacing_x = WIRDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIRDTH//2 + (i+1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):

    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]




def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIRDTH, HEIGHT)
    screen.title("Turtle Racing")

racers = get_num_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is {winner} turtle!")

