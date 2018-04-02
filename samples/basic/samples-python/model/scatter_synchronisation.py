"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python scatter_synchronisation.py
"""
__author__ = "Fernando Demarchi Natividade Luiz"
__email__ = "nativanando@gmail.com"

import sys
# Redirecting the library of mpi4py to network file system path shared
sys.path.append("/opt/ohpc/pub/libs/gnu7/openmpi3/mpi4py/2.0.0/lib64/python2.7/site-packages/mpi4py/")
import MPI
from time import time

class ScatterSynchronisation(object):
    def __init__(self):
        self.data = None
        self.data_gather = None
        self.chunks = None
        self.reduction_data = None
        self.comm = MPI.COMM_WORLD
        self.size = self.comm.Get_size()
        self.rank = self.comm.Get_rank()

    def create_array_to_scattering(self):
        if self.rank == 0:
            self.data = [(x+1)**x for x in range(10)] # Create array data
            print('we will be scattering:',self.data)
            self.chunks = [[] for _ in range(self.size)] # Creating a new array with total of processes in running
            for i, chunk in enumerate(self.data):
                self.chunks[i % self.size].append(chunk) # Increasing in the array, starting from the initial one, and dividing it according to the amount of processors

    def run_scatter_reduce(self):
        t0 = time()
        self.data = self.comm.scatter(self.chunks, root=0) # Defines the data and the process that contains the data to be distributed
        print('rank' + str(self.rank) + ' has data:' + str(self.data)) # Print the datas available in each processes distributed by initial Processor
        self.data_gather = self.comm.gather(self.data, root=0) # Gather the data for a specific processor
        for i in range(len(self.data)): # Performs the calculation of the split data
            self.data[i] = self.data[i] + 1
        self.reduction_data = self.comm.reduce(self.data, op=MPI.SUM, root=0) #reduce data to new array with calculation
        self.comm.Barrier()
        t = (time()-t0) * 1000
        print(t)

        if self.rank == 0:
            print(self.data_gather)
            print(self.reduction_data)

if __name__ == '__main__':
    scatter = ScatterSynchronisation()
    scatter.create_array_to_scattering()
    scatter.run_scatter_reduce()
