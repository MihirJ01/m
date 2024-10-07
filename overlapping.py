import turtle
import time

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Overlapping Squares Animation")

# Create turtle object
square_turtle = turtle.Turtle()
square_turtle.shape("square")
square_turtle.color("cyan")
square_turtle.speed(0)  # Fastest drawing speed
square_turtle.penup()

# Function to draw a square
def draw_square(size):
    square_turtle.pendown()
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)
    square_turtle.penup()

# Animation loop
size = 20  # Initial size of the square
for i in range(50):
    square_turtle.goto(-size / 2, size / 2)  # Center each square
    draw_square(size)

    # Rotate the turtle slightly to create the overlapping effect
    square_turtle.right(10)

    # Increase the size of the next square
    size += 5

    # Update the screen
    win.update()

    # Control animation speed
    time.sleep(0.1)

# Close the window on click
win.mainloop()
