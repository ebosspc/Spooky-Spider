#Import turtle library for drawing functions
import turtle as trtl

#Rename turtle painter object to painter
painter = trtl.Turtle()

#Draw filled in black circle for spider body
painter.pensize(40)
painter.circle(20)
painter.penup()

#Draw spider head
painter.goto(0,-35)
painter.pendown()
painter.pensize(17)
painter.circle(8)
painter.penup()

#Draw right spider eye
painter.goto(8,-36)
painter.pendown()
painter.color("blue")
painter.pensize(4)
painter.circle(2)
painter.penup()
painter.pencolor("black")

#Draw left spider eye
painter.goto(-8,-36)
painter.pendown()
painter.color("blue")
painter.pensize(4)
painter.circle(2)
painter.penup()
painter.pencolor("black")
painter.penup()

#Set spider characteristics
num_legs = 8
length_leg = 80
angle_between_leg = 280 / num_legs
painter.pensize(5)

#Initialize while loop that will repeat for each leg of the spider
iteration_count = 0

while (iteration_count < num_legs):
    #Draw the first set of 4 legs on the right
    if iteration_count < 4:
        #Starting position for leg
        painter.penup()
        painter.goto(0,20)
        painter.pendown()

        #Set direction
        painter.setheading(angle_between_leg*iteration_count - 200)

        #Draw leg
        painter.circle(50,-120)

        #Increase iteration count
        iteration_count = iteration_count + 1

    #Draw the set of 4 legs on the left
    else:
        #Starting position for leg
        painter.penup()
        painter.goto(0,20)
        painter.pendown()

        #Set direction
        painter.setheading(angle_between_leg*iteration_count-40)

        #Draw leg
        painter.circle(50, 120)

        #Increase iteration count
        iteration_count = iteration_count + 1

#Display final product on screen and keep screen persistant
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()