# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:15:50 2019

@author: khlifi
"""
from mpi4py import MPI

import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

value=np.array(rank,'d')
#comm.Bcast(value,root=0)

print(' Rank: ',rank, ' value = ', value)

value_sum      = np.array(0.0,'d')
value_max      = np.array(0.0,'d')
value_gathered=np.array(0.0,'d')
comm.Reduce(value, value_sum, op=MPI.SUM, root=0)
comm.Reduce(value, value_max, op=MPI.MAX, root=0)

if rank == 0:
    print(' Rank 0: value_sum =    ',value_sum)
    print(' Rank 0: value_max =    ',value_max)
 
    

