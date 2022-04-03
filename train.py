import pickle
import time

stats = {}
max_ngrams = 2

# create a list of ngrams from a single line in
# the training data
def ngram(line, n):
	output = []
	for i, char in enumerate(line):
		# use backticks as start of line characters
		# e.g. test == "```t... ``te... `tes... test" for 4grams
		if i - n < 0:
			buff = ''
			for j in range(abs(i - n)):
				buff += '`'
			buff += line[0:i]
			output.append((buff, char))
		else:
			output.append((line[i - n:i], char))
	return output

start = time.time()

with open('rockyou-train.txt', encoding='ISO-8859-1') as file:
    data = [i for i in file]

end = time.time()
print("Time: {:4f}".format(end-start))

for line in data:
    # add ngrams to the stats dict for all n less than or
    # equal to max_ngrams (unigrams, bigrams, trigrams, etc...)
    for i in range(3):
        for gram in ngram(line, i + 1):
            prev = gram[0] # previous characters, ngram
            nxt = gram[1] # next character

            # if this ngram hasn't been seen yet
            # add it to the stats dict
            if not prev in stats:
                stats[prev] = {}
            # if the next character hasn't been seen to
            # follow the ngram yet, add it the ngram's 
            # dict of seen characters
            if not nxt in stats[prev]:
                stats[prev][nxt] = 0
            # increment the statistic
            stats[prev][nxt] += 1

# convert frequency counts to probabilities
for ngram in stats:
	occur = []

	for key, value in stats[ngram].items():
		occur.append(value)

	total = sum(occur)

	for key, value in stats[ngram].items():
		stats[ngram][key] = float(value) / float(total)

# save ro
with open('{}-gram.pickle'.format(max_ngrams), 'w') as file:
	pickle.dump(stats, file)
		