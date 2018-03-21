# Intro to mpi4py library

There are many situations in parallel programming when groups of processes need to exchange messages. Rather than explicitly sending and receiving such messages as we have been doing, the real power of MPI comes from group operations known as collectives.

### [MPI for python documentation](http://mpi4py.scipy.org/docs/usrman/index.html)

## Colletctive operations

Synchronization operation. Creates a barrier synchronization in a group. Each task, when reaching the Barrier() call, blocks until all tasks in the group reach a Barrier() call. Then all tasks are free to proceed.

```Bash
# Add a Global synchronisation operation
comm.Barrier()
```
