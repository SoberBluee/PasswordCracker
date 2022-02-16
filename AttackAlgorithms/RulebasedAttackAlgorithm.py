import time
import hashlib

class RulebasedAttackAlgorithm():
    def __init__(self, attack_options, data, rules, found):
        #parameter data
        self.attack_options = attack_options
        self.data = data
        self.rules = rules
        self.found = found

        self.charset = '1234567890!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

    
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
    Description: Will apply rules to a word from a dictionary
    Parameters: self
    returns: hashing algorithm
    """
    def apply_rules(self, word):
        for rule in self.rules:
            rule = list(rule)
            first_char = rule[0]
            #check if first character is a rule
            if(first_char not in self.charset):
                if(first_char == 'l'):
                    word = word.lower()
                if(first_char == 'u'):
                    word = word.upper()
                if(first_char == 'd'):
                    word = word + word
                if(first_char == 'c'):
                    pass
            
            if("$" in rule):
                pass
            if("^" in rule):
                pass


    """
    Name: rulebased_attack
    Description: Will start the rule based attack, cleaning words from the dictionary
    Parameters: self
    returns: hashing algorithm
    """
    def rulebased_attack(self):
        self.start = time()
        
        for word in self.data:
            word = self.clean_word(word)
            self.apply_rules(word)

        # loop over dictionary
        # clean word
        # call apply rule
        # loop through rules in list
        # check what type of rule it is (prefix & suffix)
        # check for rule to apply to word
        # apply rule to word then add the rest

    def main(self):
        print(" - Starting Rule based attack - ")
        self.rulebased_attack()