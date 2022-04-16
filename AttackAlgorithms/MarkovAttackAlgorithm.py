import time
import hashlib
import json
import random
import numpy as np

class MarkovAttackAlgorithm():
    """
    Name: __init__
    Description: Initializes multi-processing data  
    Parameters: self, attack_options: AttackOptions Object, data: List, found: Event()
    returns: none
    """
    def __init__(self, attack_options, data, found):
        self.attack_options = attack_options
        self.data = data
        self.found = found
        self.max_length = self.attack_options.pass_phrase_len
        self.hash_to_crack = self.attack_options.hash_value.lower()
        self.starting_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    """
    Name: get_hashing_algorithm
    Description: Get the hashing algorithm using a string from attack options
    Parameters: self
    returns: hashing algorithm
    """
    def get_hashing_algorithm(self):
        return hashlib.new(self.attack_options.hash_type)
    
    """
    Name: save_output
    Description: Will save the output to a file and will change filename if already exists
    Parameters: self, passwd: String (password to be saves), num: Integer (number of result file)
    returns: hashing algorithm
    """
    def save_output(self, passwd, num=1):
        filename = ""
        try:
            with open(f"AppData/result{num}.txt", "x") as result:
                result.write(f"{passwd}\n")
                result.write(f"{self.time}")
                result.close()
        except FileExistsError:
            self.save_output(passwd, num+1)

    """
    Name: get_stats
    Description: Gets generated statistics from file
    Parameters: self
    returns: json object (key:value)
    """
    def get_stats(self):
        with open("file.txt", "r", encoding="UTF-8") as file:
            return json.load(file)

    """
    Name: choose_char
    Description: randomly choose character from statics file using that characters statiics
    Parameters: self, char: String (char to randomly choose from statistics file)
    returns: string
    """
    def choose_char(self, stats, char):
        if(char in stats):
            return np.random.choice(list(stats[char].keys()), p=list(stats[char].values()))

    """
    Name: get_starting_char
    Description: 
    Parameters: self
    returns: char
    """
    def get_starting_char(self, stats, password):
        char_len = 0
        rand_choice = random.randint(0, len(self.starting_chars) - 1)
        starting_char = self.starting_chars[rand_choice]
        password += starting_char
        return self.choose_char(stats, starting_char)       

    """
    Name: get_starting_char
    Description: 
    Parameters: self
    returns: none
    """
    def markov_attack(self):
        stats = self.get_stats()
        while(True):
            password = ""
            password += self.get_starting_char(stats, password)
            for pass_len in range(self.max_length):
                next_char = password[-1]
                password += self.choose_char(stats, next_char)
                
            print(password)
            hash = password.encode('UTF-8')
            #hashs the generated password with the given hashing algorithm
            hash_algorithm = self.get_hashing_algorithm()
            hash_algorithm.update(hash)
            hash = hash_algorithm.hexdigest()
        
            #Compare passwords to check if it has cracked
            if(hash == self.hash_to_crack):
                #stops and prints timer
                self.end = time.time()
                self.time = self.end - self.start
                #saves result to file
                self.save_output(password)
                self.found.set()
    """
    Name: main
    Description: Starts markov attack
    Parameters: self
    returns: none
    """
    def main(self):
        print("-Starting Markov Chain Attack-")
        self.markov_attack()