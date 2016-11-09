import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# First, load the image again
filename = "machinelearningimage1.jpg"
image = mpimg.imread(filename)

# Create a TensorFlow Variable
x = tf.Variable(image, name='x')

model = tf.initialize_all_variables()

with tf.Session() as sess:
    x = tf.transpose(x, perm=[1, 0, 2])
    sess.run(model)
    result = sess.run(x)


plt.imshow(result)
plt.show()
