import pandas as pd
import numpy as np


df = pd.read_csv("/home/shriniwas/Paper/input/adult.csv")

numerical_list = []

categorical_list = []

size = len(df)

for col in df:

	if(df[col].dtype != np.float64 and df[col].dtype != np.int64):
	
		categorical_list.append(col)
		
	else:
	
		temp_dict = {}	
	
		for iteration in range(size):
		
			if(df[col][iteration] in temp_dict):
			
				temp_dict[df[col][iteration]] += 1
				
			else:
			
				temp_dict[df[col][iteration]] = 1
	
		if(len(temp_dict.keys()) <= 5):
		
			categorical_list.append(col)
			
		else:
		
			numerical_list.append(col)
		
print(categorical_list)
print(numerical_list)
