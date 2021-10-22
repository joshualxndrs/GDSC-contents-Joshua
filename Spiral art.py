import turtle

colors = ["#4285F4", "#DB4437", "#F4B400", "#0F9D58"]
turtle.bgcolor("black")

turtle.speed(0)

size=1

while size < 500:
  turtle.pencolor(colors[size%4])
  turtle.forward(size)
  turtle.right(1000)
  size = size + 1