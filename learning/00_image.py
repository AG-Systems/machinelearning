import tensorflow as tf
import matplotlib.image as mpimg

# First, load the image
filename = "machinelearningimage1.jpg"
image = mpimg.imread(filename)

# Print out its shape
print(image.shape)

#output: (5528, 3685, 3)
# This means the image is 5528 pixels high, 3685 pixels wide, and 3 colors “deep”.
