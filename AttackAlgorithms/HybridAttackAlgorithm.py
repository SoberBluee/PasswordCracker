import time
import hashlib

class HybridAttackAlgorithm():
    """
    Name: __init__
    Description: Initializes multi-processing data 
    Parameters: self, AttackOptions: Object, data: List, rules: List, found: Event()
    returns: none
    """
    def __init__(self, attack_options, data, rules,found):
        #Parameter data
        self.attack_options = attack_options
        self.data = data
        self.rules = rules
        self.found = found

        #attack data
        self.charset = '1234567890!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        self.charset_len = len(self.charset)
        self.hash_to_crack = self.attack_options.hash_value.lower()

        #other data
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
    Name: clean_word
    Description: Will clean a word of numbers and symbols to apply attack to
    Parameters: self, word: String (word to be processed)
    returns: word: String
    """
    def clean_word(self, word):
        word = word.rstrip()
        return ''.join(i for i in word if i not in self.charset)
    
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
    Description:Will save the output to a file and will change filename if already exists
    Parameters: self
    returns: hashing algorithm
    """
    def save_output(self, passwd):
        password = passwd
        filename = ""
        num = 1
        try:
            with open("AppData/result.txt", "x") as result:
                result.write(f"{password}\n")
                result.write(f"{self.time:.4f}")
                result.close()
        except FileExistsError:
            self.recurse_filename(num, passwd)
    
    """
    Name: apply_rules
    Description: Will apply a rule set to a word from a generated file
    Parameters: self, word: String (word to be processed), start_begining:Boolean 
    returns: word: String
    """
    def apply_rules(self, rule, start_begining):  
        for word in self.data:
            word = self.clean_word(word)
            
            if(start_begining):
                temp_word = rule + word
            else:
                temp_word = word + rule

            print(temp_word)
            temp_word = temp_word.rstrip()
            hash = temp_word.encode('UTF-8')
            #hashs the generated password with the given hashing algorithm
            hash_algorithm = self.get_hashing_algorithm()
            hash_algorithm.update(hash)
            hash = hash_algorithm.hexdigest()
        
            #Compare passwords to check if it has cracked
            if(hash == self.hash_to_crack):
                print(f"Found Password: {temp_word}")
                self.end = time.time()
                self.time = self.end - self.start
                print('{:.4f} seconds'.format(self.time))
                self.save_output(word)
                self.found.set()

    """
    Name: hybrid_attack
    Description: Will start a hybrid dictionary attack using brute forceing
    Parameters: self, word: String (word to be processed)
    returns: word: String
    """
    def hybrid_attack(self):
        self.start = time.time()
        for rule in self.rules:
            rule=rule.rstrip()
            self.apply_rules(rule, False)
            self.apply_rules(rule, True)

    """
    Name: main  
    Description: starts a hybird attack
    Parameters: self, word: String (word to be processed)
    returns: word: String
    """
    def main(self):
        print(" - Starting hybrid attack - ")
        self.hybrid_attack()
        