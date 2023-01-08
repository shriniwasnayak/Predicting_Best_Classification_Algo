import pandas as pd
import json
import numpy as np
import os

output_file_path = "/home/shriniwas/Paper/output/analysis/"

list_of_files = os.listdir("/home/shriniwas/Paper/input/data")

input_file_path = "/home/shriniwas/Paper/input/data/"


for file_name in list_of_files:

	print(file_name)

	output_dict = {}

	output_file_name = file_name.split(".csv")[0]

	output_dict["file_name"] = output_file_name

	df = pd.read_csv(input_file_path + file_name)

	list_of_columns = []

	for col in df:

		list_of_columns.append(col)

	if("target" in list_of_columns):
	
		list_of_columns.remove("target")

	if("id" in list_of_columns):
	
		list_of_columns.remove("id")


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

	if(len(numerical_list) == 0):
	
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
				
		
		if(len(numerical_list) != 1):
				
			total_correlation /= ( size_of_numerical_list * (size_of_numerical_list - 1) / 2 )
			output_dict["Avg_correlation"]  = total_correlation

		else:
		
			output_dict["Avg_correlation"]  = None

	json_obj = json.dumps(output_dict,indent = 2)

	file_obj.write(json_obj)

