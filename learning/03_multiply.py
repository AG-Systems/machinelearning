import tensorflow as tf


x = tf.placeholder("float", [None, 3]) #create a symbolic variable 'x'
# The first dimension of the placeholder is None, meaning we can have any number of rows. 
# The second dimension is fixed at 3, meaning each row needs to have three columns of data.

z = x * 2 #multply the variable by 2

with tf.Session() as sess:
    x_data = [[1, 2, 3],
              [4, 5, 6],]
    result = sess.run(z, feed_dict={x: x_data})
    print(result)
    
    # pass the x data though the x variable which gets fed into the dictionary which gets ran & then printed.
