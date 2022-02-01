
import time
import multiprocessing as mp
import numpy as np
import hashlib
import logging

class DicionaryAttack():
    """
    Name: __init__
    Description: Initializes multi-processing data  
    Parameters: self, AttackOptions: Object
    returns: none
    """

    def __init__(self, attack_options, data, found):
        self.attack_options = attack_options
        self.data= data
        self.found = found
        self.passwords_tried = 0
        self.password = ""
        self.time = 0.0
        
        
    """
    Name: get_hashing_algorithm
    Description: Get the hashing algorithm using a string
    Parameters: self
    returns: hashing algorithm
    """

    def get_hashing_algorithm(self):
        return hashlib.new(self.attack_options.hash_type)

    def saveOutput(self, passwd, s = 0):
        password = passwd
        filename = ""
        num = 1
        try:
            with open("result.txt", "x") as result:
                result.write(f"{password}\n")
                result.write(f"{self.time:.4f}")
                result.close()
        except FileExistsError:
            num +=1
            with open("result{num}.txt") as result:
                result.write(f"{password}\n")
                result.write(f"{self.time:.4f}")
                result.close()



    """
    Name: dictionary_attack
    Description: Starts dictionary attack  
    Parameters: self 
    returns: none
    """
    def dictionary_attack(self):
        start = time.time()
        self.hash_to_crack = self.attack_options.hash_value.lower()
        
        for passwd in self.data:
            passwd = passwd.rstrip()
            passwd = passwd.encode('utf-8')
            
            hash_algorithm = self.get_hashing_algorithm()
            hash_algorithm.update(passwd)
            hash = hash_algorithm.hexdigest()
            
            # print(f"{hash}:{self.hash_to_crack}")
            if(hash == self.hash_to_crack):
                ##return data back to main window to be outputted to output box
                print(f"found password: {passwd}")
                end = time.time()
                self.time = end-start
                print(f'{self.time:.4f} seconds')
                self.password = passwd.decode('utf-8')
            
                self.saveOutput(passwd)

                self.found.set()


            self.passwords_tried+=1;
    """
    #Name: main
    #Description: Main entry point for dictionary attack
    #Parameters: self 
    #returns: output: String
    """
    def main(self):
        print("-Start Dictionary-")
        
        self.dictionary_attack()
        print(str(self.password) + ":" + str(self.passwords_tried) + str(self.time))

        exit(str(self.password) + ":" + str(self.passwords_tried) + str(self.time))


    