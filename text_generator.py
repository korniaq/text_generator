from nltk.tokenize import word_tokenize
from collections import defaultdict
from collections import Counter
import random


file_name = input()
corpus = ''
with open(file_name, "r", encoding="utf-8") as f:
    for line in f:
        corpus += line

# tokens = word_tokenize(corpus)
tokens = corpus.split()

trigrams = []
for i in range(len(tokens)-2):
    trigrams.append([tokens[i] + ' ' + tokens[i+1], tokens[i+2]])

trigrams_data = defaultdict(list)
for trigram in trigrams:
    trigrams_data[trigram[0]].append(trigram[1])

for i in range(10):
    words = []
    current_head = '.'
    while current_head[0].islower() or not current_head[0].isalpha() or current_head.endswith('.') or current_head.endswith('?') or current_head.endswith('!') or '.' in current_head or '?' in current_head or '!' in current_head:
        current_head = random.choice([trigram[0] for trigram in trigrams])
    sentence = current_head
    current_tail = ' '
    while len(sentence.split()) < 5 or not (current_tail.endswith('.') or current_tail.endswith('?') or current_tail.endswith('!')):
        tails = [tail for tail in trigrams_data[current_head]]
        current_tail = random.choice(tails)
        sentence += ' ' + current_tail
        current_head = current_head.split()[-1] + ' ' + current_tail
    print(sentence)

