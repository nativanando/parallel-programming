"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python mpi4pySharing.py
"""
__author__ = "Fernando Demarchi Natividade Luiz"
__email__ = "nativanando@gmail.com"

import sys
from time import time
import numpy as np
import csv
# Redirecting the library of mpi4py to network file system path shared
sys.path.append("/opt/ohpc/pub/libs/gnu7/openmpi3/mpi4py/2.0.0/lib64/python2.7/site-packages/mpi4py/")
import MPI

class BarrierSynchronisation:

    def __init__(self):
        self.sizes = [ 2**n for n in xrange(1,24) ] # size data [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608]
        self.runs  = 20 # number of iterations
        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.Get_rank() #number of running processor

    def run_barrier_test(self):
        print("Benchmarking braodcast performance on %d parallel MPI processes..." % self.comm.size)
        print()
        print("%15s | %12s | %12s | %12s" %
        ("Size (bytes)", "Time (msec)", "Bandwidth (MiBytes/s)", "processor (number)"))

        for s in self.sizes:
            data = np.ones(s) # ([ s.,  s.,  s.,  s.,  s.]) # return a new array of given shape and type.
            t0 = time()
            for i in xrange(self.runs):
                self.comm.Bcast( [data, MPI.DOUBLE], 0) # Broadcast a message from one process to all other processes in a group
            t = (time()-t0) / self.runs
            print('waiting synchronisation')
            self.comm.Barrier() # Global synchronisation operation
            print("%15d | %12.3f | %12.3f | %d" % (data.nbytes, t*1000, data.nbytes/t/1024/1024, self.rank) ) #number bytes, time (msec) and bandwidth (mybytes)

if __name__ == '__main__':
    barrierTest = BarrierSynchronisation()
    barrierTest.run_barrier_test()
