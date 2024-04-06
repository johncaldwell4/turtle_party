import turtle

# created the triangle with a for loop with function and the triangle is still upside down.

side = 100
color = 'blue'
number_of_sides = 3
angle_for_side = 120
upsidedown = "right"


def shapes(side=50, color='black', number_of_sides=3, upsidedown='right', angle_for_side=360):
    turtle.color(color)
    if number_of_sides >= 3:
        for line in range(number_of_sides):
            turtle.forward(side)
            if upsidedown == "right":
                turtle.right(angle_for_side / number_of_sides)
            elif upsidedown == "left":
                turtle.left(angle_for_side / number_of_sides)
    else:
        turtle.write("You need to have at least 3 sides in your shape")


def back(len):
    turtle.penup()
    turtle.back(len)
    turtle.pendown()


def move(len):
    back(-1 * len)


def spiral(len, angle_for_side, upsidedown='right'):
    for i in range(len, 6, -5):
        turtle.forward(i)
        if upsidedown == "right":
            turtle.right(angle_for_side)
        elif upsidedown == "left":
            turtle.left(angle_for_side)


# function to draw the triangle
for i in range(3, 8):
    shapes(100, 'green', i, "right")
    back(50)

spiral(150, 45, "left")

turtle.mainloop()
