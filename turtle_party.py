import turtle

# created the triangle with a for loop with function and the triangle is still upside down.

side = 100
color = 'blue'
number_of_sides = 3
angle_for_side = 120
upsidedown = "right"


def shapes(side=50, color='black', number_of_sides=3, upsidedown='right', angle_for_side=360):
    turtle.color(color)
    for line in range(number_of_sides):
        turtle.forward(side)
        if upsidedown == "right":
            turtle.right(angle_for_side / number_of_sides)
        elif upsidedown == "left":
            turtle.left(angle_for_side / number_of_sides)


def move(len):
    turtle.penup()
    turtle.back(len)
    turtle.pendown()


# function to draw the triangle
shapes(100, 'green', 3, "left")
move(250)
shapes(200, 'blue', 4)

turtle.mainloop()
