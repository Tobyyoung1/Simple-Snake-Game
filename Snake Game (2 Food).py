#Snake Game

import turtle 
import time
import random

delay= 0.1

#variables
score = 0
high_score = 0


#set up the screen
wn= turtle.Screen()
wn.title("Snake Game by Toby")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates

# Snake head
head= turtle.Turtle()
head.speed(0) #animation speed of the turtle module (moves as fast as possible [0])
head.shape("square")
head.color("black")
head.penup() #does not draw
head.goto(0,0) #starts in center of screen
head.direction= "stop"
head.next_direction= "stop"

#Snake Food
food= turtle.Turtle()
food.speed(0) #animation speed of the turtle module (moves as fast as possible [0])
food.shape("circle")
food.color("red")
food.penup() #does not draw
food.goto(20*random.randint(-14,14),20*random.randint(-14,14)) #starting position

#Snake Food 2
food2= turtle.Turtle()
food2.speed(0) #animation speed of the turtle module (moves as fast as possible [0])
food2.shape("circle")
food2.color("yellow")
food2.penup() #does not draw
food2.goto(20*random.randint(-14,14),20*random.randint(-14,14)) #starting position
#Ensures starting position is not on top of other food
while food2.distance(food) < 20:
    food2.goto(20*random.randint(-14,14),20*random.randint(-14,14)) #starting position


#Snake body
segments= []

#Pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))




# Functions
def go_up():
    '''
    Points head up
    Returns: None
    '''
    if head.direction != "down":
        #head.direction = "up"
        head.next_direction = "up"

def go_down():
    '''
    Points head down
    Returns: None
    '''
    if head.direction != "up":
        #head.direction = "down"
        head.next_direction = "down"

def go_left():
    '''
    Points head left
    Returns: None
    '''
    if head.direction != "right":
        #head.direction = "left"
        head.next_direction= "left"
def go_right():
    '''
    Points head right
    Returns: None
    '''
    if head.direction != "left":
        #head.direction = "right"
        head.next_direction= "right"
    
def move():
    '''
    Moves the head of the snake in the direction it is facing
    Returns: None
    '''
    if head.direction == "up":
        y= head.ycor() #saves y coordinate
        head.sety(y + 20) #moves y coordinate up by 20
    if head.direction == "down":
        y= head.ycor() #saves y coordinate
        head.sety(y - 20) #moves y coordinate down by 20
    if head.direction == "left":
        x= head.xcor() #saves x coordinate
        head.setx(x - 20) #moves x coordinate left by 20
    if head.direction == "right":
        x= head.xcor() #saves x coordinate
        head.setx(x + 20) #moves x coordinate right by 20

def move_food(food):
    '''
    Move the food to a random spot on the screen
    Returns None
    '''
    x= 20*random.randint(-14, 14) #screen is 600 pixels wide and tall, use multiples of 20 to make it look cleaner
    y= 20*random.randint(-14, 14)
    food.goto(x,y)
    
    for segment in segments:
        if segment.distance(food) < 20:
            move_food(food)
    
#Keyboard bindings
wn.listen() #tells the window opened to listen for clicking of keyboard
wn.onkeypress(go_up, "w") #assigns a function to a key
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    wn.update() #every time the loop triggers, updates the screen
    
    #Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)           #briefly pauses game
        head.goto(0,0)          #moves head to origin
        head.direction= "stop"  #stops the head to give player time to breathe
        head.next_direction= "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000) #Moves segment off screen because can't figure out how to delete segement
            
        #clear the segments list
        segments = []
        
        #Reset the score
        score= 0
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
        
        #Reset delay
        delay = 0.1
        
        #reset food
        move_food(food)
        move_food(food2)
    

    #Check for collision with food
    if head.distance(food) < 20: #The radius of each turtle object is 10 if the distance between their centers is less than 20 they collide
         # Move the food to a random spot on the screen   
         move_food(food)
         
         #add a segment
         new_segment= turtle.Turtle()
         new_segment.speed(0) #animation speed
         new_segment.shape("square")
         new_segment.color("grey")
         new_segment.penup()
         segments.append(new_segment)
         
         #increase the score
         score += 1
         if score > high_score:
             high_score = score
        
         pen.clear()
         pen.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
         
         #shorten the delay
         delay -= 0.001
         
         
    #Check for collision with food2
    if head.distance(food2) < 20: #The radius of each turtle object is 10 if the distance between their centers is less than 20 they collide
         # Move the food to a random spot on the screen   
         move_food(food2)
         
         #add a segment
         new_segment= turtle.Turtle()
         new_segment.speed(0) #animation speed
         new_segment.shape("square")
         new_segment.color("grey")
         new_segment.penup()
         segments.append(new_segment)
         
         #increase the score
         score += 1
         if score > high_score:
             high_score = score
        
         pen.clear()
         pen.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
         
         #shorten the delay
         delay -= 0.001
         
         
    #Ensure segments move behind the head 
    #   Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x= segments[index-1].xcor() #gives segment the x-coordinate of the previous segment
        y= segments[index-1].ycor() #same for y
        segments[index].goto(x,y) #makes the segment go to said x and y coordinates
        
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    head.direction= head.next_direction
    move()
    
    #Check for a collision with body
    for segment in segments:
        if head.distance(segment)<20:
            time.sleep(1)           #briefly pauses game
            head.goto(0,0)          #moves head to origin
            head.direction= "stop"  #stops the head to give player time to breathe
            head.next_direction= "stop"
            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000) #Moves segment off screen because can't figure out how to delete segement
                
            #clear the segments list
            segments = []
            
            #Reset the score
            score= 0
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
            
            #reset delay
            delay = 0.1
            
            #reset food 
            move_food(food)
            move_food(food2)
    
    time.sleep(delay)
    
    
wn.mainloop() #Located at end of code, keeps the window open

#End the program gracefully
turtle.done()




