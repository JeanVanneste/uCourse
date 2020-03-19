# bigramodel.py
# Author: Sébastien Combéfis
# Version: March 8, 2020

import argparse
import re
import string
import sys

import nltk

from nltk import bigrams, ConditionalFreqDist, FreqDist
from nltk.lm.preprocessing import flatten, pad_both_ends

# bigram -> nltk.util
# FreqDist, ConditionalFreqDist -> nltk.probability

"""
text = ['i like chinese food', 'chinese people like food']
preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
tokens = list(flatten(preprocessed))

fd = FreqDist(tokens)
print(fd['like'])

model = bigrams(tokens)
cfd = ConditionalFreqDist(model)
print(cfd['like']['food'])
"""


def get_text(filename):
    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

    with open(args.file, 'r') as f:
        data = f.read().encode('ascii', errors="ignore").decode().replace('\n', ' ')
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
        data = _RE_COMBINE_WHITESPACE.sub(" ", data).strip()

    data = tokenizer.tokenize(data)

    # Deleting punctuation
    translator = str.maketrans('', '', string.punctuation)

    clean_data = []
    for i in data:
        clean_data.append(i.translate(translator))

    return clean_data


def preprocess_text(sequences):
    # Preprocessed : iterator on sequence
    preprocessed = [pad_both_ends(s.split(' '), n=2) for s in sequences]
    return list(flatten(preprocessed))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", default=sys.stdin,
                        help='corpus text file to analyse')

    args = parser.parse_args()

    sequences = get_text(args.file)

    tokens = preprocess_text(sequences)

    fd = FreqDist(tokens)
    print("FreqDist : ", fd['like'])
