
import multiprocessing as mp
import hashlib
import itertools
import queue
import time

class BruteForce():

    #Name: __init__
    #Description: Initializes multi-processing data 
    #Parameters: self, AttackOptions: Object
    #returns: none
    def __init__(self, AttackOptions):
        self.Attack_options = AttackOptions
        self.cores_count = 2
        
    #Name: generate_string
    #Description: Will generate a string password
    #Parameters: self, AttackOptions: Object
    #returns: none
    def generate_string():
        numbers = "1234567890"

        for i in range(1,6):
            for char in itertools.product(numbers, repeat=i):
                char = ''.join(char)
        
    def brute_force(self):
        sum_factors = 0
        n = 100000
        for i in range(1, n):
            if(n % i == 0):
                sum_factors = sum_factors + i
        if (sum_factors == n):
            print('{} is a Perfect number'.format(n))
        
    def main(self):
        
        processes = []
        print("-Start Brute Force-")
        tic = time.time()
        for x in range(5):
            worker = mp.Process(target= self.brute_force)
            processes.append(worker)

        #starts each process
        for process in processes:
            process.start()

        for process in processes: 
            process.join()

        toc = time.time()
        print('Done in {:.4f} seconds'.format(toc-tic))
            
        


