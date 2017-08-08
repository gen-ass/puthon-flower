import turtle

window = turtle.Screen()  # Global variables
window.bgcolor("purple")

brad = turtle.Turtle ()
brad.shape("turtle")
brad.speed(10) # Speed of drawing square
brad.width(2) # Width of the line of the square

sides = 3  # Draws a square but depending on the amount of sides will draw another type of shape

def many_square (size, sides):  # Sise and sides is made a defined variable. This will loop the square
    for i in range (sides) :                # until it stops
          brad.forward (size)
          brad.left (360/sides)  # Shape sides is calculated  by  using  the angle of a  circle and dividing by the amount of sides.
                                                # In this case 360 / 4 = 90. So 90 degree angles gives us a square


for i in range (51) : # The square will be redrawn a certain amount of times in this case 50
     many_square (50*2, sides) # Here the size of the square's side is determined in pixels
     brad.left (i) # Here the drawing of a square will  start at  position 0 and  iterate to draw the next
     if  i == 5 : # Below the squares will count to a certain number and then change colour. 
         brad.pencolor ("red")
     if i == 10 : 
            brad.pencolor ("blue")
     if i == 20 : 
            brad.pencolor ("green")
     if i == 50 : 
            brad.pencolor ("white")
            brad.pendown ()
            brad.goto (0, -200)

window.exitonclick()

many_square ()
