import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import time
import warnings



warnings.filterwarnings("ignore")


def GNB(data_df,target_df,t = 0.25,r = 3):

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = t, random_state = r)

	model = GaussianNB()
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
	
	return accuracy
	
	

def KNN(data_df,target_df,t = 0.25,r = 3,k = 3):

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = t, random_state = r)

	model = KNeighborsClassifier(k)
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
		
	return accuracy	


def DTree(data_df,target_df,t = 0.25,r = 3):

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = t, random_state = r)

	model = DecisionTreeClassifier()
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
		
	return accuracy	


def SVM(data_df,target_df,t = 0.25,r = 3):

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = t, random_state = r)

	model = SVC(kernel = "linear")
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
	
	end_time = time.time()
	
	return accuracy		
	

def LogReg(data_df,target_df,t = 0.25,r = 3):

	X_train , X_test , Y_train , Y_test = train_test_split(data_df , target_df , test_size = t, random_state = r)

	model = LogisticRegression()
	
	model.fit(X_train,Y_train)
	
	Y_pred = model.predict(X_test)
	
	accuracy = metrics.accuracy_score(Y_test,Y_pred)
	
	end_time = time.time()
	
	return accuracy	
	

df = pd.read_csv("/home/shriniwas/Paper/input/test_c.csv")
target_df = df["target"]
del df["target"]
data_df = df


for t in [0.2,0.25,0.3]:

	for r in [3,4,5,6,7]:
	
		for k in [3,5,6,7]:
	
			print("t : {0}\tr : {1}\tk : {2}".format(t,r,k))
	
			GNB_accuracy = GNB(data_df,target_df,t,r)

			KNN_accuracy = KNN(data_df,target_df,t,r,k)

			SVM_accuracy = SVM(data_df,target_df,t,r)

			DTree_accuracy = DTree(data_df,target_df,t,r)

			LogReg_accuracy = LogReg(data_df,target_df,t,r)

			accuracy_list = [LogReg_accuracy,GNB_accuracy,KNN_accuracy,DTree_accuracy,SVM_accuracy]

			print(accuracy_list)
			input()

"""
plt.bar(["LogReg","GNB","KNN","DTree","SVM"],accuracy_list,0.3,color = ["red","green","blue","yellow","orange","brown"])
plt.xlabel("Algorithm")
plt.ylabel("Accuracy")
plt.savefig("/home/shriniwas/Paper/output/final_accuracy_graph_c.png")
plt.clf()
"""

