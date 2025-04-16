import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


colors = [ 'red', 'blue', 'green', 'orange']    # define a list of colors
tina.pensize(15)
tina.pendown()
for color in colors:                            # loop through the colors
    tina.pencolor(color)
    tina.forward(50)
    tina.left(90)

tina.penup()
tina.left(180)
tina.forward(200)

for i in range(len(colors)):
    print(colors[i])

tina.pendown()

for color in colors:                            # loop through the colors
    tina.pencolor(color)
    tina.forward(50)
    tina.right(90)

tina.penup()
tina.left(180)
tina.forward(100)

print('You have L rizz')
turtle.exitonclick()                     # Close the window when we click on it