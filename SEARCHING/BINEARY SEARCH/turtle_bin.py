import turtle
import sys
import time

# ------------------ INPUT ------------------
if len(sys.argv) > 1:
    arr = list(map(int, sys.argv[1].split(",")))
    target = int(sys.argv[2])
else:
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 11

# ------------------ SCREEN ------------------
screen = turtle.Screen()
screen.title("🐰 Binary Search Visualization")
screen.bgcolor("black")

# STATIC PEN (array — NEVER cleared)
static_pen = turtle.Turtle()
static_pen.hideturtle()
static_pen.penup()
static_pen.color("white")

# DYNAMIC PEN (updates — cleared every step)
dynamic_pen = turtle.Turtle()
dynamic_pen.hideturtle()
dynamic_pen.penup()
dynamic_pen.color("yellow")

# RESULT PEN
result_pen = turtle.Turtle()
result_pen.hideturtle()
result_pen.penup()

# Rabbit pointer
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

    static_pen.goto(x, y)
    static_pen.write(val, align="center", font=("Arial", 14, "bold"))

    static_pen.goto(x, y - 30)
    static_pen.write(i, align="center", font=("Arial", 10, "normal"))

    positions.append((x, y))

# Target display
static_pen.goto(0, 150)
static_pen.write(f"Target: {target}", align="center", font=("Arial", 16, "bold"))

rabbit.goto(positions[0][0], 60)

# ------------------ BINARY SEARCH ------------------
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    # Move rabbit
    rabbit.goto(positions[mid][0], 60)

    # CLEAR ONLY dynamic text
    dynamic_pen.clear()

    # Show pointers
    dynamic_pen.goto(0, 100)
    dynamic_pen.write(
        f"L={left}   R={right}   MID={mid}",
        align="center",
        font=("Arial", 14, "bold")
    )

    # Show current check
    dynamic_pen.goto(positions[mid][0], -60)
    dynamic_pen.write(
        f"Check {arr[mid]}",
        align="center",
        font=("Arial", 10, "normal")
    )

    time.sleep(1.5)

    if arr[mid] == target:
        rabbit.color("green")

        result_pen.goto(0, -120)
        result_pen.color("green")
        result_pen.write(
            f"✅ Found at index {mid}",
            align="center",
            font=("Arial", 16, "bold")
        )

        turtle.done()

    elif arr[mid] < target:
        # Mark eliminated left side
        for i in range(left, mid + 1):
            static_pen.goto(positions[i][0], -80)
            static_pen.color("red")
            static_pen.write("X", align="center", font=("Arial", 12, "bold"))
            static_pen.color("white")

        left = mid + 1

    else:
        # Mark eliminated right side
        for i in range(mid, right + 1):
            static_pen.goto(positions[i][0], -80)
            static_pen.color("red")
            static_pen.write("X", align="center", font=("Arial", 12, "bold"))
            static_pen.color("white")

        right = mid - 1

    time.sleep(1.5)

# ------------------ NOT FOUND ------------------
result_pen.goto(0, -120)
result_pen.color("red")
result_pen.write(
    "❌ Element Not Found",
    align="center",
    font=("Arial", 16, "bold")
)

turtle.done()