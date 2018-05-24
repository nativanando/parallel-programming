"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run...
"""
__author__ = "Fernando Demarchi Natividade Luiz"
__email__ = "nativanando@gmail.com"

import matplotlib.pyplot as plt
import csv
import pandas as pd

class BenchMarkSpeedUp:
	def __init__(self, file_in):
		self.file_in = file_in
		self.df = pd.read_csv('results/'+self.file_in)
		print (self.df['time'])
	
	def plot_graph(self):
		plt.plot(self.df['time'])
		plt.title('Cluster broadcasting')
   		plt.grid(True)
        	plt.savefig('plot.png')

if __name__ == '__main__':
	plot = BenchMarkSpeedUp('log-out-2x1.txt')
	plot.plot_graph()


