"""
This file is a test for shared mpi4py libraries in a cluster environment.
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
        self.file_handle.Write('bytes-length,msec,bandwidth,processor')
        self.file_handle.Write('\n')

    def write(self, msg):
        self.file_handle.Write(msg)

    def close(self):
        self.file_handle.Sync()
        self.file_handle.Close()
