import turtle

def draw_rectangle(animal, width, height):
    """Get animal to draw a rectangle of given width and height."""
    for _ in range(2):
        animal.forward(width)
        animal.left(90)
        animal.forward(height)
        animal.left(90)

window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square
for _ in range(15):
    draw_multicolor_square(tess, size)
    size += 10              # Increase the size for next time
    tess.forward(10)        # Move tess along a little
    tess.right(18)          # and give her some turn

window.mainloop()
