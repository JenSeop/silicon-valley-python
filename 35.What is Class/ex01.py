import time
from turtle import Turtle

jen = Turtle()
print(jen)
jen.shape("turtle")
jen.color("red", "green")
while True:
  jen.forward(5)
  jen.left(5)
  time.sleep(0.1)