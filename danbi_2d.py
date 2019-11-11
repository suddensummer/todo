import turtle
from math import * 
turtle.shape("turtle")
"""
R = input("공간의 가로 길이를 입력하세요.")/2
H = input("공간의 세로 길이를 입력하세요.")
r = input("프로젝터의 가로길이를 입력하세요.")/2
x = input("프로젝터의 높이를 입력하세요.")
y = input("프로젝터와 반사경 사이 거리를 입력하세요.")
w = input("반사경의 반지름을 입력하세요.")
h = input("반사경의 높이를 입력하세요.")
"""

R = 875/2
H = 260
r = 50/2
x = 50
y = 5
w = 8
h = 8.4

C_H = R*(-h*h+w*w)/(2*h*w) -x-y
print(C_H)

k = w*y/sqrt((y+h)*(y+h)+w*w)
a = k*k-w*w
b = -h*w*(R-w)
c = (R-w)*(R-w)*(k*k-h*h)

C_L = -x-y-h+(-b-sqrt(b*b-a*c))/a
print(C_L)
"""
print(k)
print((h*(R-w)+w*(C_L+x+y+h))/sqrt((R-w)*(R-w)+(C_L+x+y+h)*(C_L+x+h+y)))
"""
turtle.penup()
turtle.goto(-R,0)
turtle.pendown()
turtle.goto(R,0)
turtle.goto(R,-H)
turtle.goto(-R,-H)
turtle.goto(-R,0)

turtle.penup()
turtle.goto(-r,0)
turtle.pendown()
turtle.goto(r,0)
turtle.goto(r,-x)
turtle.goto(-r,-x)
turtle.goto(-r,0)

turtle.penup()
turtle.goto(0, -x-y)
turtle.pendown()
turtle.goto(w,-x-y-h)
turtle.goto(-w,-x-y-h)
turtle.goto(0,-x-y)

turtle.penup()
turtle.goto(0,-x)
turtle.color("RED")
turtle.pendown()
turtle.goto(0,-x-y)
turtle.goto(R,C_H)

turtle.penup()
turtle.goto(0,-x)
turtle.pendown()
turtle.goto(w,-x-y-h)
turtle.goto(R,C_L)
