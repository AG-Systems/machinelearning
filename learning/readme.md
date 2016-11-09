What's the difference between tf.placeholder and tf.Variable

The difference is that with tf.Variable you have to provide an initial value 
when you declare it. With tf.placeholder you don't have to provide an initial value 
and you can specify it at run time with the feed_dict argument inside Session.run
