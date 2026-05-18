import turtle
import random
import time
import math

# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.title("Heap Sort Tree Visualization")
screen.bgcolor("black")
screen.setup(width=1400, height=800)

screen.tracer(0)

# ---------------- DATA ----------------
arr = [random.randint(10, 99) for _ in range(10)]

# ---------------- DRAWERS ----------------
tree_pen = turtle.Turtle()
tree_pen.hideturtle()
tree_pen.speed(0)
tree_pen.penup()
tree_pen.color("white")

line_pen = turtle.Turtle()
line_pen.hideturtle()
line_pen.speed(0)
line_pen.penup()
line_pen.color("gray")

text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.penup()
text_pen.color("white")

pointer = turtle.Turtle()
pointer.shape("turtle")
pointer.color("cyan")
pointer.penup()

# ---------------- NODE POSITIONS ----------------
positions = {}

# ---------------- CALCULATE TREE POSITIONS ----------------
def calculate_positions():

    positions.clear()

    levels = math.ceil(math.log2(len(arr) + 1))

    for i in range(len(arr)):

        level = int(math.log2(i + 1))

        level_nodes = 2 ** level

        pos_in_level = i - (2 ** level - 1)

        spacing = 500 // (level + 1)

        x = (
            pos_in_level * spacing
            - ((level_nodes - 1) * spacing / 2)
        )

        y = 250 - level * 120

        positions[i] = (x, y)

# ---------------- DRAW TREE ----------------
def draw_tree(highlight=None, swap=None, sorted_nodes=None):

    tree_pen.clear()
    line_pen.clear()

    if sorted_nodes is None:
        sorted_nodes = []

    # Draw edges
    for i in range(len(arr)):

        left = 2 * i + 1
        right = 2 * i + 2

        x1, y1 = positions[i]

        if left < len(arr):
            x2, y2 = positions[left]

            line_pen.goto(x1, y1)
            line_pen.pendown()
            line_pen.goto(x2, y2)
            line_pen.penup()

        if right < len(arr):
            x2, y2 = positions[right]

            line_pen.goto(x1, y1)
            line_pen.pendown()
            line_pen.goto(x2, y2)
            line_pen.penup()

    # Draw nodes
    for i, value in enumerate(arr):

        x, y = positions[i]

        color = "white"

        if i == highlight:
            color = "yellow"

        if swap and i in swap:
            color = "red"

        if i in sorted_nodes:
            color = "green"

        tree_pen.goto(x, y - 20)

        tree_pen.fillcolor(color)

        tree_pen.begin_fill()
        tree_pen.pendown()
        tree_pen.circle(25)
        tree_pen.end_fill()
        tree_pen.penup()

        tree_pen.goto(x, y - 8)
        tree_pen.color("black")

        tree_pen.write(
            value,
            align="center",
            font=("Arial", 12, "bold")
        )

        tree_pen.color("white")

    screen.update()

# ---------------- HEAPIFY ----------------
def heapify(n, i, sorted_nodes):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    x, y = positions[i]

    pointer.goto(x, y + 50)

    draw_tree(highlight=i, sorted_nodes=sorted_nodes)

    time.sleep(1)

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:

        draw_tree(
            swap=[i, largest],
            sorted_nodes=sorted_nodes
        )

        time.sleep(1)

        arr[i], arr[largest] = arr[largest], arr[i]

        draw_tree(
            swap=[i, largest],
            sorted_nodes=sorted_nodes
        )

        time.sleep(1)

        heapify(n, largest, sorted_nodes)

# ---------------- HEAP SORT ----------------
def heap_sort():

    n = len(arr)

    calculate_positions()

    text_pen.goto(0, 350)

    text_pen.write(
        "Heap Sort Tree Visualization",
        align="center",
        font=("Arial", 22, "bold")
    )

    draw_tree()

    time.sleep(2)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i, [])

    sorted_nodes = []

    # Extract elements
    for i in range(n - 1, 0, -1):

        draw_tree(
            swap=[0, i],
            sorted_nodes=sorted_nodes
        )

        time.sleep(1)

        arr[i], arr[0] = arr[0], arr[i]

        sorted_nodes.append(i)

        draw_tree(sorted_nodes=sorted_nodes)

        time.sleep(1)

        heapify(i, 0, sorted_nodes)

    sorted_nodes.append(0)

    draw_tree(sorted_nodes=sorted_nodes)

    text_pen.goto(0, -350)
    text_pen.color("green")

    text_pen.write(
        "Heap Sort Completed ✅",
        align="center",
        font=("Arial", 18, "bold")
    )

    pointer.color("green")

# ---------------- RUN ----------------
heap_sort()

turtle.done()