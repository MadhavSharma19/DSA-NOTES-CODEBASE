import turtle
import math
import sys
import time

# ------------------ INPUT ------------------
# If running from Streamlit
if len(sys.argv) > 1:
    arr = list(map(int, sys.argv[1].split(",")))
    target = int(sys.argv[2])
else:
    # Manual testing
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 9

n = len(arr)
step = int(math.sqrt(n))

# ------------------ SCREEN SETUP ------------------
screen = turtle.Screen()
screen.title("🐰 Jump Search Visualization")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")

rabbit = turtle.Turtle()
rabbit.shape("turtle")
rabbit.color("cyan")
rabbit.penup()

# ------------------ DRAW ARRAY ------------------
positions = []
start_x = -300

for i, val in enumerate(arr):
    x = start_x + i * 80
    y = 0

    pen.goto(x, y)
    pen.write(val, align="center", font=("Arial", 14, "bold"))

    # Draw index below
    pen.goto(x, y - 30)
    pen.write(f"{i}", align="center", font=("Arial", 10, "normal"))

    positions.append((x, y))

# Move rabbit to start
rabbit.goto(positions[0][0], 60)

# ------------------ DISPLAY TARGET ------------------
pen.goto(0, 150)
pen.write(f"Target: {target}", align="center", font=("Arial", 16, "bold"))

# ------------------ JUMP SEARCH ------------------
prev = 0

# 🔹 Jump phase
while prev < n and arr[min(step, n) - 1] < target:
    jump_index = min(step, n) - 1

    # Move rabbit to jump block
    rabbit.goto(positions[jump_index][0], 60)

    # Highlight block
    pen.goto(positions[jump_index][0], -60)
    pen.write(f"Jump to index {jump_index}", align="center", font=("Arial", 12, "normal"))

    time.sleep(1.5)

    prev = step
    step += int(math.sqrt(n))

    if prev >= n:
        pen.goto(0, -120)
        pen.color("red")
        pen.write("❌ Element Not Found", align="center", font=("Arial", 16, "bold"))
        turtle.done()

# 🔹 Linear search phase
pen.goto(0, -90)
pen.color("yellow")
pen.write("🔍 Linear Search in block", align="center", font=("Arial", 14, "bold"))

for i in range(prev, min(step, n)):
    rabbit.goto(positions[i][0], 60)

    pen.goto(positions[i][0], -60)
    pen.write(f"Check {arr[i]}", align="center", font=("Arial", 10, "normal"))

    time.sleep(1)

    if arr[i] == target:
        rabbit.color("green")

        pen.goto(0, -120)
        pen.color("green")
        pen.write(f"✅ Found at index {i}", align="center", font=("Arial", 16, "bold"))

        turtle.done()

# ------------------ NOT FOUND ------------------
pen.goto(0, -120)
pen.color("red")
pen.write("❌ Element Not Found", align="center", font=("Arial", 16, "bold"))

turtle.done()