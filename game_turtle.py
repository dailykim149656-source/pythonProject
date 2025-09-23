import turtle
import random

screen = turtle.Screen()
screen.title("거북이 레이싱 게임")

colors = ["red", "blue", "green", "orange", "purple"]
turtles = []

# 거북이 생성 및 초기 위치 설정
for i in range(5):
    t = turtle.Turtle()
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(-200, 100 - i * 50)
    turtles.append(t)

# 레이스 시작
winner = None
while not winner:
    for t in turtles:
        t.forward(random.randint(1, 5))
        if t.xcor() > 200:
            winner = t
            break

print(f"승자는 {winner.color()[0]} 거북이입니다!")
screen.mainloop()