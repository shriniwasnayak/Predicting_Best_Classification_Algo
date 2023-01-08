from scipy.stats import chi2_contingency
import pandas as pd

file_name = "/home/shriniwas/Paper/input/data/bank-full.csv"

df = pd.read_csv(file_name)

data_size = len(df)

categorical_list = ["job","marital","education","default","housing","loan","contact","month","pdays","previous","poutcome"]

size_categorical_list = len(categorical_list)

attr_value_dict = {}

for attr in categorical_list:

	temp_set = set()
	
	for i in range(data_size):
	
		temp_set.add(df[attr][i])
		
	attr_value_dict[attr] = list(temp_set)

print(attr_value_dict)

avg_chi_stat = 0

for i in range(size_categorical_list):

	attr_1 = categorical_list[i]

	for j in range(i+1,size_categorical_list):
	
		attr_2 = categorical_list[j]
		
		contigency_table = [[0 for k in range(len(attr_value_dict[attr_2]))] for l in range(len(attr_value_dict[attr_1]))]
		
		print(attr_1,attr_2)
		
		for k in range(data_size):
		
			x = attr_value_dict[attr_1].index(df[attr_1][k])
			y = attr_value_dict[attr_2].index(df[attr_2][k])
		
			contigency_table[x][y] += 1
			
		print(contigency_table)
		
		print(chi2_contingency(contigency_table)[0])
		
		avg_chi_stat += chi2_contingency(contigency_table)[0]		


avg_chi_stat /= (size_categorical_list*(size_categorical_list-1)/2)

print(avg_chi_stat)
