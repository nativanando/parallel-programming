/*
  * (c) Fernando Demarchi Natividade Luiz <nativanando@gmail.com>
  * For the full copyright and license information, please view the LICENSE
  * file that was distributed with this source code.
*/

#include <mpi.h>
#include <stdio.h>

int main (int argc, char* argv[]) {
  int rank, size;

  MPI_Init (&argc, &argv);      /* starts MPI */
  MPI_Comm_rank (MPI_COMM_WORLD, &rank);        /* get current process id */
  MPI_Comm_size (MPI_COMM_WORLD, &size);        /* get number of processes */
  printf( "Response from process %d of %d\n", rank, size );
  MPI_Finalize();
  return 0;
}
