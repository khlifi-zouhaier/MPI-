# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:37:27 2019

@author: khlifi
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'key1' : [1,2, 3],
            'key2' : ( 'abc', 'xyz')}
else:
    data = None

data = comm.bcast(data, root=0)
print('Rank: ',rank,', data: ' ,data)