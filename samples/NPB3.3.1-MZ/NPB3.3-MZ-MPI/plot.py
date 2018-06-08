'''
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run...
'''
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = 'nativanando@gmail.com'

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class BenchmarkNasa():
    def __init__(self):
        self.metrics = pd.read_csv('csv/metrics.csv')
        print(self.metrics['amount-np'])

    def plot_execution_time_decay(self):
        plt.plot(self.metrics['amount-np'], self.metrics['execution-time'], label='used processors', marker='o', linestyle='--', color='g')
        plt.title('NAS Parallel Benchmarking')
        plt.legend(loc='upper right')
        plt.xlabel('cores')
        plt.ylabel('Execution time (sec)')
        plt.grid(True)
        plt.savefig('execution-time-decay.png')
        self.clear_buffer_plt()

    def plot_speed_up(self):
        plt.plot(self.metrics['amount-np'], self.metrics['speed-up'], label='used processors', marker='o', linestyle='--', color='b')
        plt.title('NAS Parallel Benchmarking')
        plt.legend(loc='upper left')
        plt.xlabel('cores')
        plt.ylabel('Speed up calculation')
        plt.grid(True)
        plt.savefig('speed-up.png')
        self.clear_buffer_plt()

    def efficiency_calculation(self):
		# s(p) = t(1) / t(p)
		for i in range(0, self.metrics['amount-np'].count()):
			self.metrics['efficiency'][i] = (self.metrics['speed-up'][i] / self.metrics['amount-np'][i])
		self.metrics = self.clean_nan_values(self.metrics)
		self.metrics.to_csv('test.csv')

    def plot_graph_efficiency(self):
		plt.plot(self.metrics['amount-np'], self.metrics['efficiency'], label="used processors", marker='o', linestyle='--', color='r')
		plt.title('NAS Parallel benchmarking efficiency')
		plt.legend(loc='upper right')
		plt.xlabel('cores')
		plt.ylabel('efficiency')
            #    plt.axis([8,32,0.99,1])
		plt.grid(True)
		plt.savefig('efficiency.png')
		self.clear_buffer_plt()

    def plot_mops(self):
		plt.plot(self.metrics['amount-np'], self.metrics['total-mops'], label="Mop/s total", marker='o', linestyle='--', color='g')
		plt.title('NAS Parallel benchmarking Mop/s')
		plt.legend(loc='upper left')
		plt.xlabel('cores')
		plt.ylabel('Number os operations/s')
            #    plt.axis([8,32,0.99,1])
		plt.grid(True)
		plt.savefig('mops.png')
		self.clear_buffer_plt()

    def clear_buffer_plt(self):
        plt.cla()
    	plt.clf()

    def clean_nan_values(self, dataset):
		dataset = dataset.fillna(0)
		return dataset

if __name__ == '__main__':
    benchmark = BenchmarkNasa()
    benchmark.plot_execution_time_decay()
    benchmark.plot_speed_up()
    benchmark.efficiency_calculation()
    benchmark.plot_graph_efficiency()
    benchmark.plot_mops()
