import time
import hashlib

class MarkovAttackAlgorithm():
    def __init__(self, attack_options, data, found):
        pass
    def get_hashing_algorithm(self):
        pass

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
            
    def markov_attack(self):
        pass
    def main(self):
        pass