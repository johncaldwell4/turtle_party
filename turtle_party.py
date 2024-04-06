import turtle

# created the triangle with a for loop with function and the triangle is still upside down.

side = 100
color = 'blue'
number_of_sides = 3
angle_for_side = 120


def shape(side = 50, color = 'black', number_of_sides = 3, angle_for_side = 120):
    turtle.color(color)
    for line in range(number_of_sides):
        turtle.forward(side)
        turtle.right(angle_for_side)


# function to draw the triangle
shape(400, 'green', 3)

turtle.mainloop()
