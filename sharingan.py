import turtle as t

screen = t.Screen()

t.home()
t.goto(0, -140)
t.shape('blank')
t.color('black', 'red')
t.width(4)
t.begin_fill()
t.circle(200)
t.end_fill()
t.penup()
t.left(90)
t.forward(160)
t.right(90)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.right(90)
t.forward(60)
t.left(90)
t.pendown()
t.width(3)
t.color('grey')
t.circle(100)


class Yin:
    def __init__(self, turtle):
        self.turtle = turtle.clone()

    def draw(self, angle, distance):
        t.right(angle)

        self.turtle.penup()
        self.turtle.forward(100)
        self.turtle.right(5)
        self.turtle.pendown()
        self.turtle.color('black', 'black')

        self.turtle.begin_fill()
        self.turtle.circle(distance, 180)
        self.turtle.right(180)
        self.turtle.circle(-2 * distance, 180)
        self.turtle.circle(-1 * distance, 180)
        self.turtle.end_fill()


t.penup()
t.goto(0, 60)
t.pendown()
t.shape("blank")


a = Yin(t)
t.right(120)
b = Yin(t)
t.right(120)
c = Yin(t)

i = 0

for j in [a, b, c]:
    j.draw(i, 20)

t.done()