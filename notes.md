**knn**

Pros: Simple, multi thread, and flexible(works on linear & non linear data)  
Cons: Bad against with many points, speed, and with outliners ( Missing data is just plain awful as well)

**svm**

Pros: Accuracy, uses subset of training points

Cons: Speed


**Kernels**

Used when your data is all clumped togeather (used for SVM). It adds another dimmension to the data points to filter them out.

It finds the similarities in points


**Clustering**

K-Means = Flat clustering. Yes or no style. (Is this person a buyer or not a buyer)

Mean-Shift = Hierarchical clustering.  (Is this person a huge buyer, maybe he shops a little bit, or he does not shop at all)



**Accuracy vs Confidence**

Accuracy = Did we get the classfication right?

Confidence = Comes from the classifer and says " we have only have 60% of the votes and our confidence is only 60%"
