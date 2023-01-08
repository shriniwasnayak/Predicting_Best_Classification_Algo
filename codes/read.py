"""import pickle

fileobj = open("/home/shriniwas/Paper/input/stats/efficient_accuracies.pickle","rb")

obj = pickle.load(fileobj)

print(obj)

print(len(obj))

print(len(obj[0]))
"""

"""
import pandas as pd
import os


list_of_files = os.listdir("/home/shriniwas/Paper/input/data/")

i = 0

for f in list_of_files:

	print(i)

	print(f)

	df = pd.read_csv("/home/shriniwas/Paper/input/data/" + f)
	
	for col in df:
	
		print(df[col][0],end = ":")
		
	print("===========")
	
	i += 1"""


import pandas as pd
import os

list_of_files = os.listdir("/home/shriniwas/Paper/input/data/")

list_of_files = ["car.csv"]

for file_name in list_of_files:

	print(file_name)

	df = pd.read_csv("/home/shriniwas/Paper/input/data/" + file_name)

	categorical_list = ["buying","maint","doors","persons","lug-boot","safety"]
	
	sum_of_class = 0
	
	for col_name in categorical_list:
	
		print(col_name)
	
		class_set = set()
		
		for iteration in range(len(df)):
	
			class_set.add(df[col_name][iteration])
	
		print(class_set)		
		
		sum_of_class += len(class_set)
		
	avg_class = sum_of_class/len(categorical_list)	
	
	print(avg_class)
