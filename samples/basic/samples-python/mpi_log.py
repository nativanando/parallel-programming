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

class MPILogFile(object):
    def __init__(self, comm, filename, mode):
        self.file_handle = MPI.File.Open(comm, filename, mode)
        self.file_handle.Set_atomicity(True)

    def write(self, msg):
        self.file_handle.Write(msg)

    def close(self):
        self.file_handle.Sync()
        self.file_handle.Close()
