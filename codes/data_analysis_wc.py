import pandas as pd
import json
import numpy as np
import os
from scipy.stats import chi2_contingency

output_file_path = "/home/shriniwas/Paper/output/analysis_c/"

list_of_files = os.listdir("/home/shriniwas/Paper/input/cdata")

input_file_path = "/home/shriniwas/Paper/input/cdata/"

def find_avg_chi_score(df,categorical_list):

	alpha = 0.05

	size_categorical_list = len(categorical_list)

	attr_value_dict = {}

	data_size = len(df)

	for attr in categorical_list:

		temp_set = set()
		
		for i in range(data_size):
		
			temp_set.add(df[attr][i])
			
		attr_value_dict[attr] = list(temp_set)


	#print(attr_value_dict)

	rh0 = 0

	#print(size_categorical_list)

	for i in range(size_categorical_list):

		attr_1 = categorical_list[i]

		for j in range(i+1,size_categorical_list):
		
			attr_2 = categorical_list[j]
			
			contigency_table = [[0 for k in range(len(attr_value_dict[attr_2]))] for l in range(len(attr_value_dict[attr_1]))]
			
			#print(attr_1,attr_2)
			
			for k in range(data_size):
			
				x = attr_value_dict[attr_1].index(df[attr_1][k])
				y = attr_value_dict[attr_2].index(df[attr_2][k])
			
				contigency_table[x][y] += 1
				
			#print(contigency_table)
			
			#print(chi2_contingency(contigency_table)[0])
	
			stat, p, dof, expected = chi2_contingency(contigency_table)		

			if(p <= alpha):
			
				rh0 += 1
		

	avg_rh0 = rh0/(size_categorical_list*(size_categorical_list-1)/2)

	return(avg_rh0)


for file_name in list_of_files:

	print(file_name)

	output_dict = {}

	output_file_name = file_name.split(".csv")[0]

	output_dict["file_name"] = output_file_name

	df = pd.read_csv(input_file_path + file_name)

	list_of_columns = []

	for col in df:

		list_of_columns.append(col)

	if("id" in list_of_columns):

		list_of_columns.remove("id")

	if("target" in list_of_columns):
	
		list_of_columns.remove("target")

	output_dict["Number_of_Attributes"] = len(list_of_columns)

	numerical_list = []

	categorical_list = []

	size = len(df)

	for col in list_of_columns:

		if(df[col].dtype != np.float64 and df[col].dtype != np.int64):
		
			categorical_list.append(col)
			
		else:
		
			temp_dict = {}	
		
			for iteration in range(size):
			
				if(df[col][iteration] in temp_dict):
				
					temp_dict[df[col][iteration]] += 1
					
				else:
				
					temp_dict[df[col][iteration]] = 1
		
			if(len(temp_dict.keys()) <= 8):
			
				categorical_list.append(col)
				
			else:
			
				numerical_list.append(col)


	target_class_dict = {}
	
	for iteration in range(len(df)):
	
		if(df["target"][iteration] in target_class_dict):
		
			target_class_dict[df["target"][iteration]] += 1
			
		else:
		
			target_class_dict[df["target"][iteration]] = 1

	output_dict["classes_in_target"] = len(target_class_dict)

	output_dict["fraction_of_numerical_attributes"] = len(numerical_list)/(len(list_of_columns))
			
	avg_outliers = 0

	file_obj = open(output_file_path + output_file_name + "_analysis.json", "w")

	output_dict["Columns_Outliers"] = []

	output_dict["Size"] = size

	if(len(numerical_list) <= 1):
	
		output_dict["Average_of_count_of_outliers"] = None	
		output_dict["Normalised_Average_count_of_outliers"] = None
		output_dict["Avg_correlation"] = None
				
	else:
	
		for col_name in numerical_list:

			temp_dict = {}

			temp_dict["column_name"] = col_name 

			total_outliers = 0

			Q1 = df[col_name].quantile(0.25)
			
			Q3 = df[col_name].quantile(0.75)
			
			IQR = Q3 - Q1
			
			width = IQR * 1.5
			
			list_of_outliers = []
			
			for num in df[col_name]:
			
				if( ( num < (Q1 - width) ) or ( num > (Q3 + width) ) ):
				
					list_of_outliers.append(num)
					
					total_outliers += 1
								
			temp_dict["list_of_outliers"] = list_of_outliers
			
					
			temp_dict["count_of_outliers"] = total_outliers
			
			avg_outliers += total_outliers

			output_dict["Columns_Outliers"].append(temp_dict)
			
			
		output_dict["Average_of_count_of_outliers"] =  avg_outliers/len(numerical_list)

		output_dict["Normalised_Average_count_of_outliers"] = (avg_outliers/len(numerical_list))/size

		cf = df.corr()

		size_of_numerical_list = len(numerical_list)

		total_correlation = 0

		for i in range(size_of_numerical_list):

			for j in range(i+1,size_of_numerical_list):
			
				total_correlation += abs(cf[numerical_list[i]][numerical_list[j]])
				
				
		total_correlation /= ( size_of_numerical_list * (size_of_numerical_list - 1) / 2 )
		output_dict["Avg_correlation"]  = total_correlation

	try:

		if(len(categorical_list) <= 1):
			
			output_dict["Avg_chi_score"] = None

			output_dict["Average_of_class_types"] = None

		else:
			
			output_dict["Avg_chi_score"] = find_avg_chi_score(df,categorical_list)
			
			sum_of_class = 0
	
			for col_name in categorical_list:
			
				class_set = set()
				
				for iteration in range(len(df)):
			
					class_set.add(df[col_name][iteration])
			
				sum_of_class += len(class_set)
				
			output_dict["Average_of_class_types"] = sum_of_class/len(categorical_list)


	except:
	
		print(file_name)
		raise


	if(len(output_dict) != 11):
	
		raise Exception("Error in size")


	json_obj = json.dumps(output_dict,indent = 2)

	file_obj.write(json_obj)

