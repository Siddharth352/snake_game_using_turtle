import turtle
import time
import random

delay = .1
#background screen
screen = turtle.Screen()
screen._bgcolor("white")
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.tracer(0)

#creating snake



snake  = turtle.Turtle()
snake.speed(0) #animation speed as fast as possible

snake.shape('square')
snake.color('black')
snake.penup()
snake.goto(0,0)
snake.direction = 'up'

#scroing
score =0
high_score=0
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0 highscore : 0",align='center',font=("Courier",24,"normal"))


#creating apple

apple = turtle.Turtle()
apple.speed(0)
apple.color('green')
apple.penup()
apple.goto(200,0)
apple.shape('circle')

snake_body = []

#moving snake using function
def move_up():
    snake.direction ='up'
def move_down():
    snake.direction ='down'
def move_right():
    snake.direction = 'right'
def move_left():
    snake.direction = 'left'




def move():
    if snake.direction=='up':
        y = snake.ycor()
        snake.sety(y+10)
    if snake.direction=='down':
        y = snake.ycor()
        snake.sety(y-10)
    if snake.direction=='right':
        x = snake.xcor()
        snake.setx(x+10)
    if snake.direction=='left':
        x = snake.xcor()
        snake.setx(x-10)

#linking keyboard keys with this

screen.listen()
screen.onkeypress(move_up,"w")
screen.onkeypress(move_down,"s")
screen.onkeypress(move_right,"d")
screen.onkeypress(move_left,"a")





#Loop that update screen animation
while True:
    screen.update()
    #collision with wall
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction='stop'
        for i in range(len(snake_body)):
            snake_body[i].goto(1000,11000)
        snake_body.clear()
        score=0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=("Courier", 24, "normal"))


    #eating apple
    if snake.distance(apple)<20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x,y)
        #adding segments to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        snake_body.append(new_segment)
        score += 10
        if high_score < score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align='center',font=("Courier",24,"normal"))
        delay-=.001
    for i in range(len(snake_body)-1,0,-1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].setx(x)
        snake_body[i].sety(y)


    if len(snake_body)>0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].setx(x)
        snake_body[0].sety(y)





    i=0
    move()
    #collision with its body
    while i<len(snake_body):
        if snake.distance(snake_body[i])<10:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = 'stop'
            for i in range(len(snake_body)):
                snake_body[i].goto(1000, 11000)
            snake_body.clear()
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align='center',
                      font=("Courier", 24, "normal"))
        i+=1

    time.sleep(delay)




screen.mainloop()