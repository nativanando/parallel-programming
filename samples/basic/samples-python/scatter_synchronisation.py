"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python mpi4pySharing.py
"""
__author__ = "Fernando Demarchi Natividade Luiz"
__email__ = "nativanando@gmail.com"

import sys
# Redirecting the library of mpi4py to network file system path shared
sys.path.append("/opt/ohpc/pub/libs/gnu7/openmpi3/mpi4py/2.0.0/lib64/python2.7/site-packages/mpi4py/")
import MPI

class ScatterSynchronisation(object):
    def __init__(self):
        self.data = None
        self.data_gather = None
        self.chunks = None
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

    def run_scatter(self):
        self.data = self.comm.scatter(self.chunks, root=0) # Defines the data and the process that contains the data to be distributed
        print('rank' + str(self.rank) + ' has data:' + str(self.data)) # Print the datas available in each processes distributed by initial Processor
        self.data_gather = self.comm.gather(self.data, root=0) # Gather the data for a specific processor
        if self.rank == 0:
            print(self.data_gather)

if __name__ == '__main__':
    scatter = ScatterSynchronisation()
    scatter.create_array_to_scattering()
    scatter.run_scatter()
