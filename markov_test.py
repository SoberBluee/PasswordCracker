import json
import random
import numpy as np

PASS_COUNT = 100000
MIN_PASS_LEN = 8
MAX_PASS_LEN = 20
starting_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
starting_chars = list(starting_chars)

def get_stats():
    with open("file.txt", "r", encoding="UTF-8") as file:
        return json.load(file)

def choose_char(stats, char):
    if(char in stats):
        return np.random.choice(list(stats[char].keys()), p=list(stats[char].values()))

def get_starting_char(stats, password):
    char_len = 0
    rand_choice = random.randint(0, len(starting_chars) - 1)
    try:
        starting_char = starting_chars[rand_choice]
        password += starting_char
        return choose_char(stats, starting_char)       
    except IndexError:
        char_len = len(starting_chars)
        print(f"Rand: {rand_choice}, Len: {char_len}")

def main():
    stats = get_stats()
    for x in range(PASS_COUNT):
        password = ""
        password += get_starting_char(stats, password)
        
        for pass_len in range(MAX_PASS_LEN):
            next_char = password[-1]
            password += choose_char(stats, next_char)
            
        print(password)
    
if __name__ == '__main__':
    main()