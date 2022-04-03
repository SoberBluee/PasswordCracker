from copyreg import pickle
import statistics
from nltk.util import ngrams
import multiprocessing
import json
from multiprocessing import Process, Event

MAX_GRAMS = 3

# process_count = 5

# def split_data():
#     data_to_split = list()
    
#     with open('rockyou-train.txt',  encoding='ISO-8859-1') as file:
#         data_to_split = [line for line in file]

#     data = [data_to_split[i::process_count] for i in range(process_count)] #split up data into chuncks for each process
    
#     return data

# class calc_statistics():

#     def __init__(self, data, num):
#         self.num = num
#         self.data = data

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
        return [line for line in file]


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

# def main():
#     process_list = []
#     data = split_data()

#     for idx, i in enumerate(range(process_count)):
#         process = calc_statistics(data[idx], idx)
#         p = multiprocessing.Process(target=process.main)
#         process_list.append(p)

#     for process in process_list:
#         process.start()

#     for process in process_list:
#         process.terminate()

#     for process in process_list:
#         process.join()

if __name__ == '__main__':
    main()

# word = ['h','e','l','l','o']
# print(list(ngrams(word,n=3)))