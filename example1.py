

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# each rank gets a number
val = rank * 10 +12+13+45+17+18+19+20+16
print ("Rank %d/%d has value %d" %(rank, size, val))

sum = comm.reduce(val, op=MPI.SUM, root=0)
Max = comm.reduce(val, op=MPI.MAX, root=0)
Min = comm.reduce(val, op=MPI.MIN, root=0)



if rank==0:
    print ("Rank 0 got the sum, the total is %d" %sum)
    print ("Rank 0 got the MAX, the total is %d" %Max)
    print ("Rank 0 got the MIN, the total is %d" %Min)


