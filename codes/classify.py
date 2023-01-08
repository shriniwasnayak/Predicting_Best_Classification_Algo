import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score


def decisiontree(data):

	X = data.iloc[:,:-1]
	Y = data.iloc[:,-1]

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state=42)
	
	clf = DecisionTreeClassifier(random_state=45)
	
	clf.fit(X_train, Y_train)

	Y_pred = clf.predict(X_test)

	print(classification_report(Y_test, Y_pred))	
	print(accuracy_score(Y_test, Y_pred))
	
	b = input("Press")
	
	cm = confusion_matrix(Y_test, Y_pred)
	fig = sns.heatmap(cm,annot = True)
	plt.xlabel("Actual")
	plt.ylabel("Predicted")
	
	plt.show()
	
	
	
metric_file_path = "/home/shriniwas/Paper/output/metric/"	
metric_file_name = "temp_metric.csv"

data = pd.read_csv(metric_file_path + metric_file_name)

decisiontree(data)
