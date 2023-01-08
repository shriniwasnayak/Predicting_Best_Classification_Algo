from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

import pandas as pd

filename = "/home/shriniwas/Paper/output/metric/temp.csv"

data = pd.read_csv(filename)

X = data.iloc[:,:-1]
Y = data.iloc[:,-1]

t = [0.4,0.3,0.25,0.2,0.1]

k = [1,2,3,5,6,7,9,10]

ma = 0

at = 0

ak = 0

for i in t:

	X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = i,random_state = 4)

	for j in k:

		
		knn = KNeighborsClassifier(j)

		knn.fit(X_train,Y_train)

		Y_pred = knn.predict(X_test)

		accuracy = metrics.accuracy_score(Y_test,Y_pred)

		if(accuracy > ma):
		
			ma = accuracy
			at = i
			ak = k
		
		if(accuracy == ma):
		
			print("same : ",ma)
			print("test_size : ",i)
			print("K : ",j)			

			
print("max accuracy : ",ma)
print("test_size : ",i)
print("K : ",j)
