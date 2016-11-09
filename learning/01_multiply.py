import tensorflow as tf

a = tf.placeholder("float") # Create a symbolic variable 'a'
b = tf.placeholder("float") # Create a symbolic variable 'b'
x = tf.placeholder("float", 3) #create a symbolic variable 'x' with 3 storage var's ?

y = tf.add(a, b) # multiply the symbolic variables
z = x * 2 #multply the variable by 2


with tf.Session() as sess: # create a session to evaluate the symbolic expressions
    result = sess.run(y, feed_dict={a: 5, b: 5}) #adds a and b togeather. Passes 5 
    print(result)
    result = sess.run(z, feed_dict={x: [1, 2, 3]}) # passes an array 1 to 3 to x
    print(result)
