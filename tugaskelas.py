from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data1 = [i for i in range(2048)]
    i = ceil(len(data1)/size)
    data = []
    for x in range(0,len(data1),i):
        if (x+i)<=len(data1):
            data.append(data1[x:(x+i)])
        else:
            data.append(data1[x:len(data1)])
else:
    data = None
    
data = comm.scatter(data, root=0)

if rank % 2 == 0: 
    result = [num for num in data if num % 2 == 0]
    print("Rank %d, bilangan genap: %s" % (rank, result))
else: 
    result = [num for num in data if num % 2 != 0]
    print("Rank %d, bilangan ganjil: %s" % (rank, result))
