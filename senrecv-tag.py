from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

if rank == 0:
  comm.send(12,dest=1,tag=1)
  comm.send(234,dest=1,tag=2)
  comm.send(123,dest=2)
  data = comm.recv(source=2)
  print("diterima data pada rank %d yaitu %s" % (rank,data))
elif rank == 1:
  data = comm.recv(source=0,tag=2)
  print("diterima data pada rank %d yaitu %s" % (rank,data))
  data = comm.recv(source=0,tag=1)
  print("diterima data pada rank %d yaitu %s" % (rank,data))
elif rank == 2:
  data = comm.recv(source=0)
  print("diterima data pada rank %d yaitu %s" % (rank,data))
  comm.send(3.14,dest=0)