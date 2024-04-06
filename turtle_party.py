import turtle

# created the triangle with a for loop and the triangle is still upside down.

turtle.color('red')
for line in range(3):
    turtle.forward(100)
    turtle.right(120)

turtle.mainloop()