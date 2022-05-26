# Adding multiple turtles and making them move

def drawPlayGround():
    #Draw the playground        
    arch.speed(0)
    arch.pensize(5)
    arch.penup()
    arch.goto(-x,-y)
    arch.pendown()

    for i in range(2):
        arch.forward(x*2)
        arch.left(90)
        arch.forward(y*2)
        arch.left(90)
        
    arch.penup()
    arch.goto(0,y+5)
    arch.pendown()

    arch.pencolor('blue')
    arch.write('HUNGRY TURTLE',align='center',font=('Courier New',40))

    arch.hideturtle()

def createPlayer():
    #create the hungry turtle    
    player.shape('turtle')
    player.shapesize(2)
    
def createFood(foodpiece):
    #create food    
    foodpiece.speed(0)
    foodpiece.shape('circle')
    foodpiece.color('red')
    foodpiece.penup()
    randomx = random.randint(-x,x)
    randomy = random.randint(-y,y)
    foodpiece.goto(randomx,randomy)
    randomAngle = random.randint(0,360)
    foodpiece.right(randomAngle)
    foodpiece.pendown()
    

def turnLeft():
    player.left(10)
    
def turnRight():
    player.right(10)
    
def createListener():
    turtle.listen()
    turtle.onkey(turnLeft,'Left')
    turtle.onkey(turnRight,'Right')
    turtle.onkey(increaseSpeed,'Up')
    turtle.onkey(decreaseSpeed,'Down')
    # turtle.onkey(quit(),'Esc')
    
def increaseSpeed():
    global distance
    distance += 1
    
def decreaseSpeed():
    distance = 1
    distance -= 1
    
def checkAndBounceIfAnyTurtleHitsTheBorder(AnyTurtle):
    #Bounce when turtle hits the border
    if AnyTurtle.xcor() > x-10 or AnyTurtle.xcor() <-x+10 or AnyTurtle.ycor() > y-10 or AnyTurtle.ycor() < -y+10:
        AnyTurtle.right(180)
        
def checkIfPlayerHitsFood(t1,t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    n = (((x2-x1)**2) + ((y2-y1)**2))
    d = n ** 0.5
    if d < 20:
        return True
    else:
        return False
    

###########################    
#Main Execution starts here

from tkinter import N, font
import turtle
import random
x = 300
y = 250
arch = turtle.Turtle()
player = turtle.Turtle()
Scoret = turtle.Turtle()
Scoret.hideturtle()
distance = 1
score = 0
foodspeed = 1

food = []
for i in range(6):
    food.append(turtle.Turtle())
    
drawPlayGround()
createPlayer()
createListener()

for i in range(6):
    createFood(food[i])


player.penup()
while True:
    player.forward(distance)
    checkAndBounceIfAnyTurtleHitsTheBorder(player)
    
    for i in range(6):
        food[i].penup()
        food[i].forward(foodspeed)
        checkAndBounceIfAnyTurtleHitsTheBorder(food[i])
        if checkIfPlayerHitsFood(player,food[i]):
            foodspeed += 1
            print()
            
            #Step 1 : increment the score
            score += 10
            
            #Step 2 : Display the score
            scoreMsg = "Score : " + str(score)
            
            print(scoreMsg)        
            Scoret.speed(0)
            Scoret.penup()
            Scoret.goto(0,-y-30)
            Scoret.clear()
            Scoret.write(scoreMsg,align='center',font=('Courier New',20,'bold'))
            
            
            #Step 3: Hide the food
            food[i].hideturtle()
            
            #Step 4:Make the food appear in a new random location
            # randomx = random.randint(-x,x)
            # randomy = random.randint(-y,y)
            # foodpiece.goto(randomx,randomy)
            createFood(food[i])             
            food[i].showturtle()


turtle.done()