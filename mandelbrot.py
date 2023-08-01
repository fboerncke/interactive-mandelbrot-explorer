# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

# Function to calculate the Mandelbrot set for a given complex number 'c' and maximum number of iterations 'max_iter'
def mandelbrot(c, max_iter):
    z = c  # Initialize z to the complex number 'c'
    for n in range(max_iter):  # Iterate up to 'max_iter' times
        if abs(z) > 2:  # If the absolute value of z exceeds 2, return the current iteration count
            return n
        z = z*z + c  # Update z according to the Mandelbrot formula
    return max_iter  # If z never exceeds 2 after 'max_iter' iterations, return 'max_iter'

# Function to draw the Mandelbrot set for a given range of coordinates and maximum number of iterations
def draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)  # Create a linear space for the real part of the complex numbers
    r2 = np.linspace(ymin, ymax, height)  # Create a linear space for the imaginary part of the complex numbers
    n3 = np.empty((width,height))  # Create an empty array for the Mandelbrot set
    for i in range(width):  # Iterate over the width of the array
        for j in range(height):  # Iterate over the height of the array
            n3[j][i] = mandelbrot(r1[i] + 1j*r2[j],max_iter)  # Calculate the Mandelbrot set for each complex number in the array
    return n3  # Return the Mandelbrot set

# Function to handle the selection of a rectangular area for zooming in
def onselect(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata  # Get the starting coordinates of the selected area
    x2, y2 = erelease.xdata, erelease.ydata  # Get the ending coordinates of the selected area
    ax.clear()  # Clear the previous plot
    # Draw the Mandelbrot set for the selected area
    ax.imshow(draw_mandelbrot(min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2),width,height,max_iter), extent=[min(x1,x2), max(x1,x2), min(y1,y2), max(y1,y2)], origin='lower')
    fig.canvas.draw()  # Redraw the figure

# Define the parameters for the Mandelbrot set
xmin, xmax, ymin, ymax = -2.0,1.0,-1.5,1.5
width, height = 1000, 1000
max_iter = 256

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10,10))
# Set the title of the plot
ax.set_title("Mandelbrot Set")
# Adjust the subplot parameters
plt.subplots_adjust(left=0.0, right=1.0, top=0.9, bottom=0.0)
# Draw the Mandelbrot set
ax.imshow(draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter), extent=[xmin, xmax, ymin, ymax], origin='lower')
# Create a rectangle selector for interactive zooming
rs = RectangleSelector(ax, onselect, interactive=True)
# Show the plot
plt.show()
