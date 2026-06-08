# coding: utf-8

import argparse
import codecs
import os
from kanjiconv import KanjiConv
import re

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

def main():
    dirname=os.path.dirname(__file__)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-f','--file', default=os.path.normpath(f"{dirname}/../etc/base_clean.txt"), help='file')

    args = parser.parse_args()
    file = args.file

    if not os.path.isfile(file):
        print(f"[Error] file not exists: {file}")
    
    content = load_file(file)

    parts = re.split(r'。', content)

    outfile = os.path.normpath(f"{dirname}/../etc/roman.txt")

    kanji_conv = KanjiConv(separator="")

    kana = ""
    count = len(parts)
    i = 1
    for part in parts:
        # print(f"{i}/{count}")
        s = kanji_conv.to_roman(part)
        kana += s
        kana += "。"
        i += 1

    kana = kana.replace("きごう", "")
    kana = kana.replace("kigou", "")
    kana = kana.replace("・", "")
    kana = kana.replace("~", "")
    kana = kana.replace("～", "")
    kana = kana.replace("。", ".")
    kana = kana.replace("、", ",")
    kana = kana.replace("，", ",")
    kana = kana.replace(" ", "")
    # kana = kana.replace("?", "？")
    # kana = kana.replace("!", "！")

    with codecs.open(outfile, 'w', 'utf-8') as f:
        f.write(kana)

    print(f'written to {outfile}')

if __name__ == "__main__":
    main()