
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
    
def checkAndBounceIfPlayerHitsTheBorder():
    #Bounce when turtle hits the border
    if player.xcor() > x-10 or player.xcor() <-x+10 or player.ycor() > y-10 or player.ycor() < -y+10:
        player.right(180)
        
def checkAndBounceIfFoodHitsTheBorder(food):
    #Bounce when turtle hits the border
    if food.xcor() > x-10 or food.xcor() <-x+10 or food.ycor() > y-10 or food.ycor() < -y+10:
        food.right(180)
        
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
    checkAndBounceIfPlayerHitsTheBorder()
    
    for i in range(6):
        food[i].penup()
        food[i].forward(distance)
        checkAndBounceIfFoodHitsTheBorder(food[i])
        if checkIfPlayerHitsFood(player,food[i]):
            print()
            #step by shanker
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