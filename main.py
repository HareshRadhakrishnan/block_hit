from turtle import Turtle, Screen
from time import sleep
import random
#TODO:Create a class to bounce & move the ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.speed = 0.1
    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor()+self.y_move
        self.goto(x_pos,y_pos)
    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
    def reposition(self):
        self.goto(0,-260)
        self.bounce_y()
#TODO:Create a class to manage paddle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(1,8)
        self.goto(0,-280)
    def l_move(self):
        self.goto((self.xcor()-10),self.ycor())
    def r_move(self):
        self.goto((self.xcor()+10),self.ycor())
#TODO:Create a class to build and manage blocks
class Blocks():
    def __init__(self):
        self.all_blocks =[]
    def create_blocks(self):
        x_start_point = -380
        y_start_point = 150
        for color in ["yellow", "green", "blue",'red']:
            x_start_point = -380
            for _ in range(0,14):
                block = Turtle()
                block.speed('fastest')
                block.shape('square')
                block.shapesize(1,2)
                block.color(color)
                block.penup()
                x_start_point += 50
                block.goto(x_start_point,y_start_point)
                self.all_blocks.append(block)
            y_start_point -= 25
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
    def show_score(self,score):
        self.write(f"Your Score is :{score}", align='center', font=("Courier", 36, "normal"))

is_game_over = False
screen = Screen()
score_count  = 0
ball = Ball()
ball.reposition()
paddle = Paddle()
score = Score()
chances = 3
chance_num = Turtle()
chance_num.color('white')
chance_num.penup()
chance_num.hideturtle()
chance_num.goto(170,260)

screen.bgcolor("black")
screen.setup(width=800, height=600)
block = Blocks()
block.create_blocks()
window = screen.getcanvas()
screen.tracer(0)
while not is_game_over:
    sleep(0.1)
    ball.move()
    screen.update()
    chance_num.write(f"Life Remaining: {chances}", font=("Courier", 16, "bold"))
    cursor_x = window.winfo_pointerx()
    if chances == 0:
        is_game_over = True
    elif chances > 0 and block.all_blocks ==[]:
        is_game_over = True
    for blk in block.all_blocks:
        if ball.distance(blk) < 30:
            blk.hideturtle()
            block.all_blocks.remove(blk)
            score_count += 1
            if ball.xcor() > blk.xcor() or ball.xcor() < blk.xcor():
                ball.bounce_y()
            elif ball.ycor() > blk.ycor() or ball.ycor() < blk.ycor():
                ball.bounce_x()
    if ball.xcor()> 380 or ball.xcor() < -380:
        ball.bounce_x()
    elif ball.ycor() > 280 :
        ball.bounce_y()
    if paddle.distance(ball)<100 and ball.ycor() < -260:
        ball.bounce_y()
    elif ball.ycor() < -265:
        chances -= 1
        chance_num.clear()
        ball.reposition()

    if cursor_x > 440 and cursor_x < 840:
        paddle.l_move()
    elif cursor_x > 840 and cursor_x < 1240:
        paddle.r_move()
screen.clear()
score.show_score(score_count)
screen.mainloop()