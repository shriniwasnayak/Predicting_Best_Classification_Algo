import csv
import matplotlib.pyplot as plt

input_file_path = "/home/shriniwas/Paper/input/"

output_file_path = "/home/shriniwas/Paper/output/"

list_of_csvfiles = ["adult_stats.csv","bank_stats.csv","breast_cancer_wisconsin_stats.csv","car_stats.csv","heart_disease_stats.csv","iris_stats.csv","wine_quality_stats.csv","wine_stats.csv"]

for filename in list_of_csvfiles:

	csvobj = csv.reader(open(input_file_path + filename,"r"))
	
	temp_list = []
	
	for line in csvobj:
	
		temp_list.append(line)
	
	accuracy_list = []
	time_list = []
	memory_list = []
	
	iteration = 0
	
	while(iteration < 5):
	
		try:
		
			accuracy_list.append(float(temp_list[1][iteration]))
			
		except:
		
			accuracy_list.append(None)
			
		iteration += 1
	
	iteration = 0
		
	while(iteration < 5):
	
		try:
		
			time_list.append(float(temp_list[2][iteration]))
			
		except:
		
			time_list.append(None)
			
		iteration += 1	
	
	iteration = 0
	
	while(iteration < 5):
	
		try:
		
			memory_list.append(float(temp_list[3][iteration]))
			
		except:
		
			memory_list.append(None)
			
		iteration += 1
		
	fig,ax = plt.subplots(nrows = 2,ncols = 2,figsize = (10,10))
	
	
	ax[0,0].scatter(temp_list[0],accuracy_list,color = "red")
	ax[0,0].plot(temp_list[0],accuracy_list,color = "red")
	ax[0,0].set_xlabel("Algorithm")
	ax[0,0].set_ylabel("Accuracy")
	
	ax[0,1].scatter(temp_list[0],time_list,color = "black")
	ax[0,1].plot(temp_list[0],time_list,color = "black",label = "Time")
	ax[0,1].set_xlabel("Algorithm")
	ax[0,1].set_ylabel("Time")
	
	ax[1,0].scatter(temp_list[0],memory_list,color = "yellow")
	ax[1,0].plot(temp_list[0],memory_list,color = "yellow",label = "Memory")
	ax[1,0].set_xlabel("Algorithm")
	ax[1,0].set_ylabel("Memory")
	

	plt.savefig(output_file_path + filename.split("_stats")[0] + "_graph.png")

	plt.clf()



