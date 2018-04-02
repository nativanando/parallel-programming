"""
This file is a test for shared mpi4py libraries in a cluster environment.
The application can be run by: mpiexec --hostfile /tmp/machines -np $N_PROCES --allow-run-as-root python rank_processers.py
"""
__author__ = 'Fernando Demarchi Natividade Luiz'
__email__ = "nativanando@gmail.com"

import sys

#Redirecting the library of mpi4py to network file system path shared
sys.path.append('/opt/ohpc/pub/libs/gnu7/openmpi3/mpi4py/2.0.0/lib64/python2.7/site-packages/mpi4py/')
import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print (comm)
print (rank)
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
