# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
shape = "circle"
size = 2
color = "brown"
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
Amy = trtl.Turtle(shape = shape)
Amy.color(color)
Amy.shapesize(size)
Amy.speed(0)


ore = trtl.Turtle()
ore.penup()
ore.goto(-370,270)
font = ("comic_sans", 30, "bold")
ore.write("text")
ore.ht()

counter =  trtl.Turtle()

#-----game functions--------
def turtle_clicked(x,y):
    print("Amy was clicked")
    change_position()
    Amy.st()
    score_counter()
def change_position():
    Amy.penup()
    Amy.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    Amy.goto(new_xpos, new_ypos)

def score_counter():
    global score 
    score += 1
    print(score)
    ore.clear()
    ore.write(score, font =font)

def countdown():
  wn.bgcolor("lightgreen")#my game change thing
  global timer, timer_up
  counter.penup()
  counter.goto(350,225)
  counter.ht()
  counter.clear()
  if timer <= 0:
        counter.goto(0,0)
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        game_over()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def game_over():
    wn.bgcolor("red")
    Amy.ht()
    Amy.goto(500,500)
    
    
#-----events----------------

Amy.onclick(turtle_clicked)




wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()