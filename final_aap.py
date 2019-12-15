# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:44:07 2019

@author: khlifi
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
"-------------------------------Data and Scatter to #proc--------------------------------------------"

if rank == 0:
   data = [int(input("Hello Miss/Sir:------Please Enter Your Values:")) for i in range(size)]
   print ('we will be scattering:',(data))
else:
   data = None
   
data = comm.scatter(data, root=0)
print ('rank',rank,'has data:',data)

"--------------------------Reduce and application of #operations(sum,min,max,prod)-------------------------------------------------"
value_min = comm.reduce(data, op=MPI.MIN, root=0)
value_sum= comm.reduce(data, op=MPI.SUM, root=0)
value_max = comm.reduce(data, op=MPI.MAX, root=0)
value_prod = comm.reduce(data, op=MPI.PROD, root=0)


"---------------------------Retrieve Data------------------------------------------------"

if rank == 0:
   print ('value min =',value_min)
   print(' value sum =    ',value_sum)
   print(' value max =    ',value_max)
   print(' value prod =    ',value_prod)

   