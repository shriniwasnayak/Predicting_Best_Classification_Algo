import csv
import json
import os

class Stat:

	def __init__(self,algo,accuracy):
	
		self.algo = algo
		
		try:
		
			self.accuracy = float(accuracy)*100
			
		except:
		
			self.accuracy = 0.0
		
	def __lt__(self,obj):
	
		return self.accuracy < obj.accuracy
		
	def __gt__(self,obj):
	
		return self.accuracy > obj.accuracy

	def __eq__(self,obj):
	
		return self.accuracy == obj.accuracy
		
	def __str__(self):
	
		return "Algo : {0}\tAccuracy : {1}".format(self.ago,self.accuracy)
		
		

list_of_files = os.listdir("/home/shriniwas/Paper/output/data_stats")

input_file_path = "/home/shriniwas/Paper/output/data_stats/"

stat_file_path = "/home/shriniwas/Paper/input/"

metric_filename = "/home/shriniwas/Paper/output/metric.csv"

csvobj = csv.writer(open(metric_filename,"w"))

csvobj.writerow(["File Name","Size","Average Correlation","Normalised Outliers","Accuracy"])

for file_name in list_of_files:

	stat_filename = file_name.split(".json")[0] + "_stats.csv"
	
	csv_stat_file_obj = csv.reader(open(stat_file_path + stat_filename))
	
	temp_list = []
	
	for line in csv_stat_file_obj:
	
		temp_list.append(line)

	Stat_list = []

	for i in range(len(temp_list[0])):
	
		Stat_list.append(Stat(temp_list[0][i],temp_list[1][i]))
		
	Stat_list.sort(reverse = True)

	accuracy_str = ""

	for obj in Stat_list:
	
		accuracy_str += (obj.algo + "({0})".format(obj.accuracy) + "\t")

	output_dict = json.loads(open(input_file_path + file_name,"r").read())

	temprow = [output_dict["file_name"],output_dict["Size"],output_dict["Avg_correlation"],output_dict["Normalised_Average_count_of_outliers"],accuracy_str]
	
	csvobj.writerow(temprow)
