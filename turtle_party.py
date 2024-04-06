import turtle

# created the triangle with a for loop with function and the triangle is still upside down.

def shape ():
    turtle.color('red')
    for line in range(3):
        turtle.forward(100)
        turtle.right(120)

#function to draw the triangle
shape()

turtle.mainloop()