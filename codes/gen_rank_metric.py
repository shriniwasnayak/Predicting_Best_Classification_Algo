import csv
import json
import os
import pickle

class AlgoClass:

	def __init__(self,algo_name,accuracy_score):
	
		self.algo_name = algo_name
		self.accuracy_score = accuracy_score
		
	def __lt__(self,obj):
	
		return self.accuracy_score < obj.accuracy_score
		
	def __gt__(self,obj):
	
		return self.accuracy_score > obj.accuracy_score
		
	def __eq__(self,obj):
	
		return self.accuracy_score == obj.accuracy_score
		
	def __str__(self):
	
		return "Algorithm Name : {0}\tAccuracy Score : {1}".format(self.algo_name,self.accuracy_score)	
	

target_dict = {"LogReg" : 1, "KNN" : 2, "GNB" : 3, "DTree" : 4, "RandomForest" : 5, "AdaBoost" : 6}


metric_file_path = "/home/shriniwas/Paper/output/metric/"
metric_file_name = "final_naive_metric_1.csv"

pickle_file_path = "/home/shriniwas/Paper/input/stats/"
pickle_file_name = "naive_accuracies.pickle"

accuracy_list = pickle.load(open(pickle_file_path + pickle_file_name,"rb"))


analysis_file_path = "/home/shriniwas/Paper/output/analysis/"
analysis_list_of_files = os.listdir("/home/shriniwas/Paper/output/analysis")

csvobj = csv.writer(open(metric_file_path + metric_file_name,"w"))

csvobj.writerow(["File Name","Size","Average Correlation","Normalised Outliers","Number of Attributes","Fraction of Numeric attributes","Classes in Target","target"])


for analysis_file_name in analysis_list_of_files:

	#to be used for naive
	key_file_name = analysis_file_name.split("_analysis")[0] + ".csv"

	#to be used for efficient
	#key_file_name = analysis_file_name.split("preprocessed_")[1].split("_analysis")[0] + ".csv"

	accuracy_scores = accuracy_list[ key_file_name ]
	
	algoclass_list = []

	algoclass_list.append( AlgoClass( "LogReg" , accuracy_scores[0] ) )
	algoclass_list.append( AlgoClass( "KNN" , accuracy_scores[1] ) )
	algoclass_list.append( AlgoClass( "GNB" , accuracy_scores[2] ) )
	algoclass_list.append( AlgoClass( "DTree" , accuracy_scores[3] ) )
	#algoclass_list.append( AlgoClass( "RandomForest" , accuracy_scores[4] ) )
	#algoclass_list.append( AlgoClass( "AdaBoost" , accuracy_scores[5] ) )
	
	algoclass_list.sort(reverse = True)

	analysis_file_obj = open(analysis_file_path + analysis_file_name)
	
	temp_dict = json.loads(analysis_file_obj.read())
	
	temp_row = [temp_dict["file_name"],temp_dict["Size"],temp_dict["Avg_correlation"],temp_dict["Normalised_Average_count_of_outliers"],temp_dict["Number_of_Attributes"],temp_dict["fraction_of_numerical_attributes"],temp_dict["classes_in_target"],target_dict[algoclass_list[0].algo_name]]
	
	csvobj.writerow(temp_row)
