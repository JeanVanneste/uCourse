import argparse
import sys
import re

import nltk

from nltk import bigrams, ConditionalFreqDist, FreqDist
from nltk.lm.preprocessing import flatten, pad_both_ends

# bigram -> nltk.util
# FreqDist, ConditionalFreqDist -> nltk.probability


text = ['i like chinese food', 'chinese people like food']
preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
tokens = list(flatten(preprocessed))
print(tokens)
fd = FreqDist(tokens)
print("FreqDist : ", fd['like'])

model = bigrams(tokens)
cfd = ConditionalFreqDist(model)
print(cfd['<s>']['i'])