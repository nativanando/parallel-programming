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
    def __init__(self, file_in, file_out):
        self.file_in = file_in
        self.file_out = file_out
        self.df = pd.read_csv('../post_processing/'+self.file_in+'.csv')
        self.datasets = []
        self.number_of_processors = self.df['processor'].max() + 1 #becase others loops initiate in 0

    def plot_line_graphic(self):
        if (len(self.datasets) == 0):
            print('dataset empty')
            return 0;
        coluna = self.datasets[0]['bytes-length']
        fig, ax = plt.subplots()
        legend = []
        for i in xrange(len(self.datasets)):
            linha = self.datasets[i]['bandwidth']
            ax.plot(linha, coluna, linestyle='--')
            legend.append('Processor' + str(i))
        plt.legend(legend)
        fig.set_size_inches(12, 8, forward=True)
        plt.title('Cluster broadcasting')
        plt.xlabel('Time (msec)')
        plt.ylabel('Size file (bytes)')
        plt.grid(True)
        plt.savefig('../assets/'+self.file_out+'.png')
        plt.show()
        plt.close()

    def plot_box_graphic(self, columns):
        plt.style.use('ggplot')
        self.df1.boxplot(columns)
        plt.show()

    def plot_corr_graphic(self, columns):
        self.df1[columns].corr().plot()
        plt.show()

    def create_dataframes(self):
        for i in xrange(self.number_of_processors):
            print(i)
            self.datasets.append(self.df[self.df['processor'] == i])
        print(self.number_of_processors)
        
if __name__ == '__main__':
    exportgraphic = GraphicsGenerator('barrier_sync_result', 'cluster_broadcasting')
    exportgraphic.create_dataframes()
    exportgraphic.plot_line_graphic()
