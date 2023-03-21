import turtle
import sys
import random

locationB = ([-325, 250], [-325, 200], [-175, 150], [-25, 50], [-325, -150],
             [-325, -50], [-325, 50], [125, 50], [275, 100])
surfaceB = ([650, 50], [500, 50], [200, 100], [50, 100], [650, 100],
            [200, 100], [50, 100], [150, 200], [50, 250])


# Car 클래스
class MyCar(turtle.Turtle):
    def __init__(self, image_file, location, speed=1):
        turtle.Turtle.__init__(self)
        self.speed(0)
        s = turtle.Screen()
        self.penup()
        self.hideturtle()
        s.addshape(image_file)
        self.shape(image_file)
        self.goto(location)
        self.showturtle()
        self.speed(speed)

    def up(self):
        self.setheading(90)
        self.forward(5)


    def down(self):
        self.setheading(270)
        self.forward(5)


    def right(self):
        self.setheading(0)
        self.forward(5)


    def left(self):
        self.setheading(180)
        self.forward(5)

    def move(self):
        self.forward(5)


    def collision(self):
        if self.distance(car) < 15:
        # game.minus_score(100)


# Candy 클래스
class MyCandy(turtle.Turtle):
    def __init__(self, location):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        s = turtle.Screen()
        self.penup()
        image = 'candy.gif'
        s.addshape(image)
        self.shape(image)
        self.goto(location)

    def eat(self, car):
        if self.distance(car) < 15:
            self.goto(1000, 1000)
            # game.plus_score(50)


# Background 클래스
class Background(turtle.Turtle):
    def __init__(self, location, surface):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.pencolor((0, 200, 200))
        self.fillcolor((0, 200, 200))
        for i in range(9):
            self.setheading(0)
            self.goto(location[i])
            self.begin_fill()
            self.forward(surface[i][0])
            self.right(90)
            self.forward(surface[i][1])
            self.right(90)
            self.forward(surface[i][0])
            self.right(90)
            self.forward(surface[i][1])
            self.end_fill()
            self.penup()


# 배경 위치 인식
def bg_surface(x, y):
    if -325 <= x <= 325 and 200 <= y <= 250:
        return True
    elif -325 <= x <= 175 and 150 <= y <= 200:
        return True
    elif -325 <= x <= -275 and -50 <= y <= 50:
        return True
    elif -325 <= x <= -125 and -150 <= y <= -50:
        return True
    elif -325 <= x <= 325 and -250 <= y <= -150:
        return True
    elif -175 <= x <= 25 and 50 <= y <= 150:
        return True
    elif -25 <= x <= 25 and -50 <= y <= 50:
        return True
    elif 125 <= x <= 275 and -150 <= y <= 50:
        return True
    elif 275 <= x <= 325 and -150 <= y <= 100:
        return True
    else:
        return False

#게임정보창


# 메인
s = turtle.Screen()
turtle.colormode(255)
turtle.setup(650, 500)
turtle.bgcolor(120, 120, 120)
bg = Background(locationB, surfaceB)
candyCount = 0
candyLoc = []
candies = []
while candyCount < 20:
    loc = [random.randint(-325, 325), random.randint(-250, 250)]
    if bg_surface(loc[0], loc[1]) == False and loc not in candyLoc:
        candies.append(MyCandy(loc))
        candyLoc.append(loc)
        candyCount += 1
for i in candies:
    i.showturtle()
car = MyCar('car_r.gif', [-310, 130])



while True:
    s.update()
    car.move()
    s.onkey(car.right, "Right")
    s.onkey(car.left, "Left")
    s.onkey(car.up, "Up")
    s.onkey(car.down, "Down")
    s.listen()
    for candy in candies:
        candy.eat(car)
turtle.done()
