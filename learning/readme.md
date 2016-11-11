What's the difference between tf.placeholder and tf.Variable

The difference is that with tf.Variable you have to provide an initial value 
when you declare it. With tf.placeholder you don't have to provide an initial value 
and you can specify it at run time with the feed_dict argument inside Session.run

Machine Learning is the idea that you build algorithms that learn from data, in order to perform actions on new data.


Classification problem = generates an inequality equation to a complex problem. Deterimes this or that. Quantitative 

Regression problem = Generates an equation based these features. Determins a value. Qualitative
