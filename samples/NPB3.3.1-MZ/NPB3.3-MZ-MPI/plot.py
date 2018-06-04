'''
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run...
'''
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = 'nativanando@gmail.com'

import csv
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

class BenchmarkNasa():
    def __init__(self):
        self.processors = pd.read_csv('csv/metrics.csv')
        print(self.processors)

if __name__ == '__main__':
    benchmark = BenchmarkNasa()
