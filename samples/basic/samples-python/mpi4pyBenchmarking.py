#!/usr/bin/env python

"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python mpi4pySharing.py
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"

import sys
from time import time
import numpy as np

#Redirecting the library of mpi4py to network file system path shared
sys.path.append('/opt/ohpc/pub/libs/gnu7/openmpi3/mpi4py/2.0.0/lib64/python2.7/site-packages/mpi4py/')
import MPI

sizes = [ 2**n for n in xrange(1,24) ] #number of bytes
runs  = 20 #number of iterations

comm = MPI.COMM_WORLD

print("Benchmarking braodcast performance on %d parallel MPI processes..." % comm.size)
print()
print("%15s | %12s | %12s" %
    ("Size (bytes)", "Time (msec)", "Bandwidth (MiBytes/s)"))

for s in sizes:
    data = np.ones(s) # ([ s.,  s.,  s.,  s.,  s.]) # return a new array of given shape and type.

    comm.Barrier()
    t0 = time()
    for i in xrange(runs):
        comm.Bcast( [data, MPI.DOUBLE], 0)
    comm.Barrier()
    t = (time()-t0) / runs

    print("%15d | %12.3f | %12.3f" %
        (data.nbytes, t*1000, data.nbytes/t/1024/1024) )
