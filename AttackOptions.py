"""
Class Name: AttackOptions
Class Description: Storage class to store all attack parameters.
Parameters: None
"""
class AttackOptions:
    def __init__(self, name):
        self.name = name
        self.hash_value = ""
        self.hash_type = ""
        self.attack_type = ""
        self.wordlist_location = ""
        self.hash_file_location = ""
        self.charsetAll = False
        self.charsetLower = False
        self.charsetUpper = False
        self.charsetNumbers = False
        self.charsetSymbols = False
        self.cpu = False
        self.gpu = False
        self.core_count = 1
        self.pass_phrase_len = 0
        self.max_brute_force = 0
        self.min_brute_force = 0