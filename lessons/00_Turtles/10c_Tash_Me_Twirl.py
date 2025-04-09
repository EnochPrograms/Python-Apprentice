
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

import turtle
def set_background_image(window, image_name):
    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)
    image = Image.open(image_path)
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

turtle.setup(width=600, height=600)
tina = turtle.Turtle()
screen = turtle.Screen()
set_background_image(screen, "emoji.png")


def set_turtle_image(turtle, image_name):

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

set_turtle_image(tina, "moustache3.gif")
tina.penup()
tina.goto(x=0, y=215)

tom=turtle.Turtle()
set_turtle_image(tom, "moustache1.gif")

def turtle_clicked(x, y):
    print('X=' + str(x) + ' , y=' + str(y))
    for i in range(0, 360, 20):
        tom.left(20)
tom.onclick(turtle_clicked)

turtle.done()


