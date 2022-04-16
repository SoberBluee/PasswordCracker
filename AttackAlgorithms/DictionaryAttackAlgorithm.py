import time
import hashlib

class DicionaryAttackAlgorithm():
    """
    Name: __init__
    Description: Initializes multi-processing data  
    Parameters: self, AttackOptions: Object, data: List, found: Event()
    returns: none
    """
    def __init__(self, attack_options, data, found):
        #process parameters
        self.attack_options = attack_options
        self.data= data
        self.found = found

        #more variable definitions
        self.hash_to_crack = self.attack_options.hash_value.lower()
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
                result.write(f"1.032")
                result.close()
        except FileExistsError:
            self.save_output(passwd, num+1)
        
    """
    Name: dictionary_attack
    Description: Starts dictionary attack  
    Parameters: self 
    returns: none
    """
    def dictionary_attack(self):
        start = time.time()
        #Loop over data from wordlist
        for passwd in self.data:
            passwd = passwd.rstrip()
            passwd = passwd.encode('UTF-8')
            #Hashes the password with the correct hashing algorithm
            hash_algorithm = self.get_hashing_algorithm()
            hash_algorithm.update(passwd)
            hash = hash_algorithm.hexdigest()
            passwd = str(passwd, 'UTF-8')
            
            if(hash == self.hash_to_crack):
                #return data back to main window to be outputted to output box
                print(f"found password: {passwd}")
                end = time.time()
                self.time = end-start
                print(f'{self.time:.4f} seconds')
                
                #output result to file and terminate cpus
                self.save_output(passwd)
                self.found.set()

            self.passwords_tried+=1;
    """
    #Name: main
    #Description: Main entry point for dictionary attack
    #Parameters: self 
    #returns: output: String
    """
    def main(self):
        print("-= Start Dictionary =-")
        self.dictionary_attack()


    