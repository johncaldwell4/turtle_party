import turtle

# created the triangle with a for loop with function and the triangle is still upside down.

side = 100
color = 'blue'

def shape ():
    turtle.color(color)
    for line in range(3):
        turtle.forward(side)
        turtle.right(120)

#function to draw the triangle
shape()

turtle.mainloop()