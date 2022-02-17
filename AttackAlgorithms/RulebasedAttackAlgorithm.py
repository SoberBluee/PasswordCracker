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
        self.hash_to_crack = self.attack_options.hash_value.lower() 
    
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
            temp_word = word
            # rule = list(rule)
            first_char = rule[0]
            #check if first character is a rule
            if(first_char not in self.charset):
                if(first_char == 'l'):
                    temp_word = temp_word.lower()
                if(first_char == 'u'):
                    temp_word = temp_word.upper()
                if(first_char == 'd'):
                    temp_word = temp_word + temp_word
                if(first_char == 'c'):
                    temp_word = temp_word[0].upper()

            #suffix
            if("$" in rule):
                rule = rule.split("$")
                rule.pop(0)
                rule = ''.join(rule)
                temp_word = rule + temp_word

            #prefix
            if("^" in rule):
                rule = rule.split("^")
                rule.pop(0)
                rule = ''.join(rule)
                temp_word = temp_word + rule

            print(temp_word + "\n")

            if(temp_word == '7560abcabcdanieldaniel3085'):
                print("something")

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
                self.save_output(temp_word)
                self.found.set()

    """
    Name: rulebased_attack
    Description: Will start the rule based attack, cleaning words from the dictionary
    Parameters: self
    returns: hashing algorithm
    """
    def rulebased_attack(self):
        self.start = time.time()
        
        for word in self.data:
            word = self.clean_word(word)
            if(word == ''):
                continue
            else:
                self.apply_rules(word)

    def main(self):
        print(" - Starting Rule based attack - ")
        self.rulebased_attack()