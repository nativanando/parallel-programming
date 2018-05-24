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
	def __init__(self):
		self.df1 = pd.read_csv('results/log-out-2x1.txt')
		self.df2 = pd.read_csv('results/log-out-2x2.txt')
		self.df3 = pd.read_csv('results/log-out-4x2.txt')
		self.df4 = pd.read_csv('results/log-out-6x2.txt')
		self.df5 = pd.read_csv('results/log-out-4x4.txt')

	def plot_graph(self):
		# plt.plot(self.df1['time'])
		plt.plot(self.df1['time'], label="2 processors")
		plt.plot(self.df2['time'], label="4 processors")
		plt.plot(self.df3['time'], label="8 processors")
		plt.plot(self.df4['time'], label="12 processors")
		plt.plot(self.df5['time'], label="16 processors")
		plt.title('CELTAB cluster metric')
		plt.legend(loc='upper left')
		plt.xlabel("Epochs")
		plt.ylabel("Execution time (sec)")
   		plt.grid(True)
        	plt.savefig('plot2.png')

if __name__ == '__main__':
	plot = BenchMarkSpeedUp()
	plot.plot_graph()
