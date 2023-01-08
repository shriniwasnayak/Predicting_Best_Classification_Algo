import matplotlib.pyplot as plt
import pickle

metric_file_path = "/home/shriniwas/Paper/input/stats/"
metric_file_name = "efficient_accuracies.pickle"

graph_file_path = "/home/shriniwas/Paper/output/preprocessed_accuracy_graph/"

algolist_inorder = ["LogReg","KNN","GNB","DTree"]

accuracy_dict = pickle.load(open(metric_file_path + metric_file_name,"rb"))

for file_name in accuracy_dict.keys():

	temp_list = accuracy_dict[file_name]
	
	plt.scatter(algolist_inorder,temp_list[0:4],color = "black")
	plt.plot(algolist_inorder,temp_list[0:4],color = "red")
	
	plt.xlabel("Algorithm")
	plt.ylabel("Accuracy")
	
	plt.savefig(graph_file_path + file_name.split(".csv")[0] + "_graph.png")
	
	plt.clf()
