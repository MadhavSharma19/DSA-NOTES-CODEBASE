import turtle
import random
import time

# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.title("Insertion Sort Visualization")
screen.bgcolor("black")
screen.setup(width=1200, height=700)

# Turn off automatic updates for smoother animation
screen.tracer(0)

# ---------------- DATA ----------------
arr = [random.randint(20, 300) for _ in range(12)]

# ---------------- DRAWING TURTLE ----------------
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

# ---------------- POINTER TURTLE ----------------
pointer = turtle.Turtle()
pointer.shape("turtle")
pointer.color("cyan")
pointer.penup()
pointer.speed(1)

# ---------------- TEXT TURTLE ----------------
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.color("white")
text_pen.penup()

# ---------------- DRAW FUNCTION ----------------
def draw_array(highlight1=None, highlight2=None, sorted_index=None):
    drawer.clear()

    start_x = -500
    width = 60

    for i, value in enumerate(arr):

        x = start_x + i * 80
        y = -250

        # Default color
        color = "white"

        # Current key
        if i == highlight1:
            color = "yellow"

        # Comparing element
        if i == highlight2:
            color = "red"

        # Sorted section
        if sorted_index is not None and i <= sorted_index:
            color = "green"

        # Draw bar
        drawer.goto(x, y)
        drawer.fillcolor(color)

        drawer.begin_fill()

        drawer.pendown()
        drawer.setheading(90)

        for _ in range(2):
            drawer.forward(value)
            drawer.right(90)
            drawer.forward(width)
            drawer.right(90)

        drawer.end_fill()
        drawer.penup()

        # Draw number
        drawer.goto(x + 20, y - 25)
        drawer.color("white")
        drawer.write(value, align="center", font=("Arial", 10, "bold"))

    screen.update()

# ---------------- INSERTION SORT ----------------
def insertion_sort():

    text_pen.goto(0, 300)
    text_pen.write(
        "Insertion Sort Visualization",
        align="center",
        font=("Arial", 20, "bold")
    )

    draw_array()

    time.sleep(1)

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        # Move pointer to current key
        pointer.goto(-500 + i * 80 + 20, 120)

        draw_array(highlight1=i, sorted_index=i-1)

        time.sleep(1)

        while j >= 0 and arr[j] > key:

            # Move pointer
            pointer.goto(-500 + j * 80 + 20, 120)

            draw_array(
                highlight1=i,
                highlight2=j,
                sorted_index=i-1
            )

            time.sleep(1)

            arr[j + 1] = arr[j]
            j -= 1

            draw_array(
                highlight1=j + 1,
                sorted_index=i
            )

            time.sleep(1)

        arr[j + 1] = key

        draw_array(sorted_index=i)

        time.sleep(1)

    # Final message
    text_pen.goto(0, -320)
    text_pen.color("green")
    text_pen.write(
        "Sorting Completed ✅",
        align="center",
        font=("Arial", 18, "bold")
    )

    pointer.color("green")

# ---------------- RUN ----------------
insertion_sort()

turtle.done()