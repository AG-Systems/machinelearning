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

K-Means makes 2 broad assumptions: number of clusters already known, and clusters shape. Very sensitive to initiazlation. It makes it fast however.

Mean-Shift = Does not assume anything about number of clusters. Not sensitive to outliners.  Sensitive to selection of bandwidth however. 

**Accuracy vs Confidence**

Accuracy = Did we get the classfication right?

How close are you to the actual value

Confidence = Comes from the classifer and says " we have only have 60% of the votes and our confidence is only 60%"

How sure you are your program is working
