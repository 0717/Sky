import turtle as t
t.setup(800,800)
t.penup()
t.goto(-270,300)
t.pendown()
t.color('purple','red')
t.speed(10)
for i in range(5):
    for j in range(5,i,-1):
        t.seth(90)
        t.begin_fill()
        t.circle(30,230) 
        t.fd(65)
        t.seth(50)
        t.fd(65)
        t.circle(30,210)
        t.end_fill()
        t.penup()
        t.goto((-270+65*i)+130*(6-j),300-i*100)
        t.pendown()
    t.penup()
    t.goto(-270+65*(i+1),300-(i+1)*100)
    t.pendown()

