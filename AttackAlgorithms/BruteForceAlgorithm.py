
import multiprocessing as mp
import hashlib
import itertools
import queue
import time
from itertools import cycle

class BruteForce():

    #Name: __init__
    #Description: Initializes multi-processing data 
    #Parameters: self, AttackOptions: Object
    #returns: none
    def __init__(self, AttackOptions, starting_point, charset, found):
        self.attack_options = AttackOptions
        self.starting_point = starting_point
        self.charset = charset
        self.charset_len = len(charset)
        # self.charset = self.charset.split("")
        self.starting_point = self.get_charset_starting_point()
        self.found = found
        self.password_set = False

        self.start = 0.0
        self.end = 0.0
        self.time = 0.0

    """
    Name: get_hashing_algorithm
    Description: Get the hashing algorithm using a string
    Parameters: self
    returns: hashing algorithm
    """
    def get_hashing_algorithm(self):
        return hashlib.new(self.attack_options.hash_type)

    """
    Name: get_charset_starting_point
    Description: Gets the posistion of the starting point using the charset array
    Parameters: self
    returns: idx:Ineter (posistion in the charset)
    """
    def get_charset_starting_point(self):
        # return [idx for idx,x in enumerate(self.charset) if str(x) == self.starting_point]
        for idx, x in enumerate(self.charset):
            if(str(x) == self.starting_point):
                return idx

    """
    Name: recurse_filename
    Description: Will recursivly change the filename if the same one already exists
    Parameters: self, num:Integer, password:String
    returns: none
    """
    def recurse_filename(self, num, password):
        try:
            new_filename = f"AppData/result{num}.txt"
            with open(new_filename, "x") as result:
                result.write(f"{password}\n")
                result.write(f"{self.time:.4f}")
                result.close()
        except FileExistsError:
            self.recurse_filename(num+1, password)
        

    """
    Name: saveOutput
    Description: Get the hashing algorithm using a string
    Parameters: self
    returns: hashing algorithm
    """
    def save_output(self, passwd):
        password = passwd
        filename = ""
        num = 1
        try:
            with open("AppData/result.txt", "x") as result:
                result.write(f"{password}")
                result.write(f"{self.time:.4f}")
                result.close()
        except FileExistsError:
            self.recurse_filename(num, passwd)

    """
    Name: crack
    Description: Will attempt to crack passwords up to a given length
    Parameters: self, len:Integer (length of password to crack), password:String (password to check against), hash_to_crack:String
    returns: idx:Ineter (posistion in the charset)
    """
    def crack(self, len, password, hash_to_crack):
        guess = ""
        #If the length is 0 then we have built the full password for that length
        if(len == 0):
            # print(f"Password: {password}")
            hash = password.rstrip()
            hash = hash.encode('UTF-8')
            #hashs the generated password with the given hashing algorithm
            hash_algorithm = self.get_hashing_algorithm()
            hash_algorithm.update(hash)
            hash = hash_algorithm.hexdigest()
            # password = str(hash, 'UTF-8')
            #Compare passwords to check if it has cracked
            if(hash == hash_to_crack):
                
                print(f"Found Password: {password}")
                self.end = time.time()
                self.time = self.end - self.start
                print('{:.4f} seconds'.format(self.time))
                self.save_output(password)

                self.found.set()

                
            return
        #Build password using each character from charset
        for i in range(self.starting_point, self.charset_len + self.starting_point):
            
            #if we reach end of array and have not finished then go back to begnning
            if(i >= self.charset_len):
                i = i - self.charset_len
            #build password
            # print(f"i:{i}")
            guess = password + self.charset[i]
            self.crack(len - 1, guess, hash_to_crack)
            

    def brute_force(self):
        i = 0
        length = 1
        hash_to_crack = self.attack_options.hash_value.lower()
        self.start = time.time()

        if(self.attack_options.max_brute_force == 0):
            while(True):
                self.crack(length, "", hash_to_crack)
                length+=1
        else:
            while(length != self.attack_options.max_brute_force):
                self.crack(length, "", hash_to_crack)
                length+=1
        
    def main(self):
        print(" - Starting brute force - ")
        self.brute_force()
        
            
        


