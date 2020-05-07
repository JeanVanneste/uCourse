import argparse
import string
import nltk

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    f = open(args.file, 'r')

    """
    s = f.read()
    sentences = []
    for char in s:
        sentence = ""
        if char not in ['.', ';', '?', '!']:
            sentence.append(char)
        else:
            sentences.append(sentence)

    print(sentences)
    """

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    data = f.read().encode('ascii', errors='ignore').decode()
    print('\n-------\n'.join(tokenizer.tokenize(data)))

    f.close()

    print(f.closed)
