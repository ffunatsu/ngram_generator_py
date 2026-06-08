# coding: utf-8

import argparse
import codecs
import os
from kanjiconv import KanjiConv
import re
import collections
import json

## https://stackoverflow.com/questions/55870326/program-for-letter-n-grams-of-one-word-string-in-python
def create_ngrams(word, n):
    # Break word into tokens
    tokens = [token for token in word]
    # generate ngram using zip
    ngrams = zip(*[tokens[i:] for i in range(n)])
    # concat with empty space & return
    return [''.join(ngram) for ngram in ngrams]

def ngram_json(word, n):
    ngram = create_ngrams(word, n)
    c = collections.Counter(ngram)
    return json.dumps(c.most_common(), ensure_ascii=False)

def load_file(file):
    content = ""

    with codecs.open(file, 'r', 'utf-8') as f:
       for line in f:
            line = line.rstrip()
            # print(line)
            
            if line.startswith(";"):
                pass # ignore
            else:
                content += line

    ls = " \n　"
    for l in ls:
        content = content.replace(l, "")

    return content

def write_file(content, outfile, name):
    with codecs.open(outfile, 'w', 'utf-8') as f:
        f.write(content)

    print(f'{name} written to {outfile}')

def write_ngram(word, n):
    dirname=os.path.dirname(__file__)
    write_file(ngram_json(word, n), os.path.normpath(f"{dirname}/../etc/gram-{n}.json"), f"{n}-gram")

def main():
    dirname=os.path.dirname(__file__)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-f','--file', default=os.path.normpath(f"{dirname}/../etc/kana.txt"), help='file')

    args = parser.parse_args()
    file = args.file

    if not os.path.isfile(file):
        print(f"[Error] file not exists: {file}")
    
    content = load_file(file)
    content = content.replace("？", "。")
    content = content.replace("！", "。")
    content = content.replace("、", "。")

    write_ngram(content, 1)
    write_ngram(content, 2)
    write_ngram(content, 3)

if __name__ == "__main__":
    main()