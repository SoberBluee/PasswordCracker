from copyreg import pickle
import statistics
from nltk.util import ngrams
import multiprocessing
import json
from multiprocessing import Process, Event

MAX_GRAMS = 3

def generate_ngrams(word, gram_num):
    return list(ngrams(word ,n=gram_num))

def convert_probabilities(statistics):
    for gram in statistics:
        occurance = []
        
        for key, value in statistics[gram].items():
            occurance.append(value)

        total = sum(occurance)
        
        for key, value in statistics[gram].items():
            statistics[gram][key] = float(value / total)

    return statistics

def get_data():
    with open('rockyou-train.txt',  encoding='ISO-8859-1') as file:
        lst = set([line for line in file])

    with open("rockyou.txt", encoding='ISO-8859-1') as file:
        lst2 = set([line for line in file])

    lst += "\n"
    lst += lst2

def main():
    statistics = {}
    data = get_data()
    for line in data:
        for gram_num in range(2, MAX_GRAMS + 1):
            ngrams = generate_ngrams(line.rstrip(), gram_num)
            for gram in ngrams:
                previous = gram[0]
                next = gram[1]

                if(not previous in statistics):
                    statistics[previous] = {}

                if(not next in statistics[previous]):
                    statistics[previous][next] = 0

                statistics[previous][next] += 1

    statistics = convert_probabilities(statistics)

    with open("file.txt", "w", encoding="UTF-8") as file:
        file.write(json.dumps(statistics))

if __name__ == '__main__':
    main()
