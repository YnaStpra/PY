from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

data = rank #harus ada yg namanya sama
print("1 rank %d data %d" % (rank,data))
if rank%2==0: #harus mencakup rank yg akan di jadikan root dalam bcast
  data = comm.bcast(data,root=6) 
  #rank yg menjadi root harus memenuhi syarat if
  #root harus genap dong!
else:
  data = comm.bcast(data,root=5)
  #root harus ganjil dong!
print("2 rank %d data %d" % (rank,data))