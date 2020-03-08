# bigramodel.py
# Author: Sébastien Combéfis
# Version: March 8, 2020

from nltk import bigrams, ConditionalFreqDist, FreqDist
from nltk.lm.preprocessing import flatten, pad_both_ends

text = ['i like chinese food', 'chinese people like food']
preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
tokens = list(flatten(preprocessed))

fd = FreqDist(tokens)
print(fd['like'])

model = bigrams(tokens)
cfd = ConditionalFreqDist(model)
print(cfd['like']['food'])
