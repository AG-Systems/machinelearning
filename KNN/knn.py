import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
#any data with ? replaces the outliners
df.drop(['id'], 1, inplace=True)
#id is not important so we are dropping it. If we dont drop the id, the accuracy goes from 96% to 50%

X = np.array(df.drop(['class'],1))
# x for features
y = np.array(df['class'])
# y for labels / class

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2]])
example_measures = example_measures.reshape(len(example_measures),-1)
prediction = clf.predict(example_measures)
print(prediction)
