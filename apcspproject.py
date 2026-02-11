import turtle as trtl
x = trtl.Turtle()

# background of image
x.penup()
x.goto(-510,430)
x.speed(0)
x.pendown()
x.begin_fill()
x.fillcolor("#99E1F1")
for step in range(4):
    x.forward(1012)
    x.right(90)
x.end_fill()

# base of house
x.penup()
x.goto(0,-200)
x.begin_fill()
x.fillcolor("blue")
x.pendown()
x.forward(300)
x.left(90)
x.forward(200)
x.left(90)
x.forward(300)
x.end_fill()

# roof of house
x.penup()
x.goto(0,0)
x.begin_fill()
x.fillcolor("red")
x.pendown()
x.forward(50)

x.penup()
x.goto(350,0)
x.pendown()
x.forward(50)
x.right(135)

x.penup()
x.goto(-50,0)

x.pendown()
x.forward(282)
x.right(90)
x.forward(282)
x.end_fill()

# door of house
x.penup()
x.goto(175,-200)
x.begin_fill()
x.fillcolor("red")
x.pendown()
x.left(135)
x.forward(140)
x.left(90)
x.forward(50)
x.left(90)
x.forward(140)
x.end_fill()

# circle window of house
x.penup()
x.goto(40, -85)
x.begin_fill()
x.fillcolor("pink")
x.pendown()
x.circle(30)
x.end_fill()

# triangle window of house
x.penup()
x.goto(260,-110)
x.begin_fill()
x.fillcolor("white")
x.pendown()
x.right(90)
for step in range(3):
    x.forward(60)
    x.right(120)
x.end_fill()

# chimney of house
x.penup()
x.goto(230,118)
x.begin_fill()
x.fillcolor("#1CDAD4")
x.pendown()
x.right(90)
x.forward(70)
x.right(90)
x.forward(30)
x.right(90)
x.forward(100)
x.end_fill()

# add green section to simulate grass
x.penup()
x.goto(-510,-200)
x.begin_fill()
x.fillcolor("#22A90D")
x.pendown()
x.left(90)
x.forward(1012)
x.right(90)
x.forward(250)
x.right(90)
x.forward(1012)
x.end_fill()

# tree trunk
x.penup()
x.goto(-280,-200)
x.begin_fill()
x.fillcolor("sienna")
x.pendown()
x.right(90)
x.forward(110)
x.right(90)
x.forward(40)
x.right(90)
x.forward(110)
x.end_fill()

# tree leaves

x.penup()

for step in range(6):
    x.goto(-260, 10)
    x.setheading(step * 60)
    x.forward(40)       
    x.pendown()
    x.fillcolor("#43DF3E")
    x.begin_fill()
    x.circle(60)
    x.end_fill()
    x.penup()

# a cup on tree leaves
x.penup()
x.goto(-305, -20)
x.begin_fill()
x.fillcolor("#64A2E0")
x.pendown()
x.circle(50)
x.end_fill()

x.penup()
x.goto(-315, -10)
x.begin_fill()
x.fillcolor("#64A2E0")
x.pendown()
x.circle(50)
x.end_fill()

# Sun 
horiz_turtles = [] 

turtle_shapes = ["circle"]
horiz_colors = ["yellow"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(380,320)
  ht.shapesize(8)
  ht.setheading(0)
  
for step in range(50):
    for ht in horiz_turtles:
        ht.backward(9)
        

        if step == 0:
           collision_shape = turtle_shapes.pop() if turtle_shapes else "classic"
           collision_color = "yellow"

# ask user if they want to add details to the tree
user_name = input("What is your name? ")
print("Hi", user_name)
answer = input("Would you like to add some details to the tree? State 'yes' or 'no'. ")
if answer == "yes": 
    print("Ok", user_name, "let's get started")
    
# eyes on the cup
    eyes = input("Do you want to add eyes? State 'yes' or 'no'. ")
    if eyes == "yes":
        x.penup()
        x.goto(-295,25)
        x.begin_fill()
        x.fillcolor("black")
        x.pendown()
        x.circle(10)
        x.end_fill()
        
        x.penup()
        x.goto(-265,25)
        x.begin_fill()
        x.fillcolor("black")
        x.pendown()
        x.circle(10)
        x.end_fill()
        x.penup()
        x.goto(-1000,1000)
    if eyes == "no": 
        print("Ok I will not add eyes. Have a good day! ")

# frown on the cup
    expression = input("Do you want to add a frown? State 'frown' or 'no'. ")
    if expression == "frown":
        x.penup()
        x.pensize(5)
        x.goto(-295,-5)
        x.begin_fill()
        x.fillcolor("black")
        x.pendown()
        x.setheading(0)
        x.forward(50)
        x.end_fill()
        x.penup()
        x.goto(-1000,1000)
    if expression == "no":
        print("Ah dang alright. Byeeeee! ")
        
# end of program if user chooses to not add details
if answer == "no":
    print("That's the end of the painting. Bye! ")




wn = trtl.Screen()
wn.mainloop()






