"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python mpi4pySharing.py
"""
__author__ = "Fernando Demarchi Natividade Luiz"
__email__ = "nativanando@gmail.com"

import matplotlib.pyplot as plt
import csv
import pandas as pd

class GraphicsGenerator:
    def __init__(self, file_in, file_out, number_processor):
        self.file_in = file_in
        self.file_out = file_out
        self.number_processor = number_processor
        self.df = pd.read_csv('../post_processing/'+self.file_in+'.csv')
        self.df1 = self.df[self.df['processor'] == self.number_processor]

    def plot_line_graphic(self):
        linha = self.df1['msec']
        coluna = self.df1['bytes-length']
        fig, ax = plt.subplots()
        ax.plot(linha, coluna, linestyle='--', color='r')
        fig.set_size_inches(12, 8, forward=True)
        plt.title('Cluster broadcasting')
        plt.xlabel('Time (msec)')
        plt.ylabel('Size file (bytes)')
        plt.grid(True)
        plt.savefig('../assets/'+self.file_out+'.png')
        plt.show()
        plt.close()

if __name__ == '__main__':
    exportgraphic = GraphicsGenerator('barrier_sync_result', 'cluster_broadcasting', 5)
    exportgraphic.plot_line_graphic()
