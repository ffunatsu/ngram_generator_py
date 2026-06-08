# coding: utf-8

import argparse
import codecs
import os

def main():
    dirname=os.path.dirname(__file__)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # parser.add_argument('-f','--file', default=os.path.normpath(f"{dirname}/../etc/base.txt"), help='file')
    parser.add_argument('-f','--file', default=os.path.normpath(f"{dirname}/../etc/base_clean.txt"), help='file')

    args = parser.parse_args()
    file = args.file

    if not os.path.isfile(file):
        print(f"[Error] file not exists: {file}")
    
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

    # letters = content.split('')
    print(len(content))

if __name__ == "__main__":
    main()