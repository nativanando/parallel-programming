"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python barrier_synchronisation.py
"""
__author__ = "Fernando Demarchi Natividade Luiz"
__email__ = "nativanando@gmail.com"

import sys
from time import time
import numpy as np
from mpi_log import MPILogFile
# Redirecting the library of mpi4py to network file system path shared
sys.path.append("/opt/ohpc/pub/libs/gnu7/openmpi3/mpi4py/2.0.0/lib64/python2.7/site-packages/mpi4py/")
import MPI

class BarrierSynchronisation(object):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name
        self.sizes = [ 2**n for n in xrange(1,24) ] # Size data [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]
        self.runs  = 20 # Number of iterations
        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.Get_rank() # Number of running processor
        self.log_file = MPILogFile(self.comm, self.log_file_name, MPI.MODE_WRONLY | MPI.MODE_APPEND | MPI.MODE_CREATE)
        self.array_data = []

    def run_barrier(self):
        print("Benchmarking braodcast performance on %d parallel MPI processes..." % self.comm.size)
        print()
        print("%15s | %12s | %12s | %12s" %
        ("Size (bytes)", "Time (msec)", "Bandwidth (MiBytes/s)", "processor (number)"))

        for s in self.sizes:
            data = np.ones(s) # ([ s.,  s.,  s.,  s.,  s.]) Return a new array of given shape and type.
            t0 = time()
            for i in xrange(self.runs):
                self.comm.Bcast( [data, MPI.DOUBLE], 0) # Broadcast a message from one process to all other processes in a group
            t = (time()-t0) / self.runs

            print('waiting synchronisation')
            self.comm.Barrier() # Global synchronisation operation
            print("%15d | %12.3f | %12.3f | %d" % (data.nbytes, t*1000, data.nbytes/t/1024/1024, self.rank) ) #number bytes, time (msec) and bandwidth (mybytes)
            self.array_data.append('' + str(data.nbytes) + ',' + str(t*1000) + ',' + str(data.nbytes/t/1024/1024) + ',' + str(self.rank) )

        self.array_data = self.comm.gather(self.array_data, root=0) # Gather the data for a specific processor

        if self.rank == 0:
            self.export_csv_file()

    def export_csv_file(self):
        for i in xrange(len(self.array_data)):
            for j in xrange(len(self.array_data[i])):
                print(self.array_data[i][j])
                self.log_file.write(self.array_data[i][j])
                self.log_file.write('\n')

if __name__ == '__main__':
    barrierTest = BarrierSynchronisation('barrier_sync_result.csv')
    barrierTest.run_barrier()
