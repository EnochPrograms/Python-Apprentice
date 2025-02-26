
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can copy and paste most of it! )

"""
import turtle                 # I think that these just add the turtle to the screen
turtle.setup(500,500)         # when adressing the turtle, we named it "Tina." so now when we are making the turtle do something,
tina = turtle.Turtle()        # we say Tina.forward or Tina.left to make the turtle do that thing.

Sides = 5                     # this is a varible and makes life easier.
distance = 100
angle = 360/Sides

for i in range(Sides):        # range of Sides is telling it the data from the var "Sides"
    tina.forward(distance)    # same here.
    tina.left(angle)

turtle.exitonclick()          # exitonclick exits the screen when you click.