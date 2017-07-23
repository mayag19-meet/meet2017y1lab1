import turtle

# Everything that comes after the # is a # comment.
# It is a note to the person reading the code.
# The computer ignores it.



# This is the M 
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
turtle.goto(-200,-100+200)
turtle.goto(-200+50,-100)
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

# This is the E
turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(-50,-100+200)
turtle.goto(-50+50,-100+200)
turtle.penup()
turtle.goto(-50,-100+100)
turtle.pendown()
turtle.goto(-50+50,-100+100)
turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(-50+50,-100)

# This is the other E
turtle.penup()
turtle.goto(50,-100)
turtle.pendown()
turtle.goto(50,-100+200)
turtle.goto(50+50,-100+200)
turtle.penup()
turtle.goto(50,-100+100)
turtle.pendown()
turtle.goto(50+50,-100+100)
turtle.penup()
turtle.goto(50,-100)
turtle.pendown()
turtle.goto(50+50,-100)

# This is the T
turtle.penup()
turtle.goto(100+50,-100+200)
turtle.pendown()
turtle.goto(100+150,-100+200)
turtle.penup()
turtle.goto(100+100,-100+200)
turtle.pendown()
turtle.goto(100+100,-100)


# DONE
turtle.mainloop()
