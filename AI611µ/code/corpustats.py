# corpustats.py
# Author: Sébastien Combéfis
# Version: March 2, 2020


#TODO delete punctuation from text

import argparse
import json
import string

def compute_stats(text_file):
    f = open(text_file, 'r')

    words = []

    # Get rid of non-ascii characters
    for word in f.read().encode('ascii', errors='ignore').decode().split():
        words.append(word.lower())

    f.close()

    different_words = {}
    for word in words:
        word = del_punctuation(word)
        if word in different_words:
            different_words[word] += 1
        else:
            different_words[word] = 1

    return different_words

def display_to_stdout(stats):
    for word in stats:
        print("{0} | {1}".format(word, stats[word]))

def save_to_file(stats, out_file):
    with open(out_file, 'w') as f:
        json.dump(stats, f)

def del_punctuation(word):
    translator = str.maketrans('','', string.punctuation)
    return word.translate(translator)


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
