# corpustats.py
# Author: Sébastien Combéfis
# Version: March 2, 2020


#TODO delete punctuation from text

import argparse
import json
import unittest

def compute_stats(text_file):
    f = open(text_file, 'r')

    words = []

    for word in f.read().split():
        words.append(word.lower())

    f.close()

    different_words = {}
    for word in words:
        if word in different_words:
            different_words[word] += 1
        else:
            different_words[word] = 1
    
    #print(different_words)

    return different_words

def display_to_stdout(stats):
    for word in stats:
        print("{0} | {1}".format(word, stats[word]))

def save_to_file(stats, out_file):
    with open(out_file, 'w') as f:
        json.dump(stats, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='corpus text file to analyse')
    parser.add_argument('-o', '--out', metavar='PATH', help='path to the file where to output the result of the analysis')
    args = parser.parse_args()

    print('Analysing {0}\n'.format(args.file))

    stats = compute_stats(args.file)

    if args.out:
        print('Writing output to', args.out)
        save_to_file(stats, args.out)
    else:
        print('Writing output to stdout\n')
        display_to_stdout(stats)
