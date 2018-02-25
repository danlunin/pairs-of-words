#!/usr/bin/env python3
import sys
import collections
import time
import re
import argparse


def get_counter_of_pairs(text, not_words_text, distance):
    list_of_tuples = []
    pairs = collections.Counter()
    sentences = parse_sentences(text)
    for sentence in sentences:
        list_of_tuples.extend(get_pairs(sentence, not_words_text,
                                        distance))
    for e in list_of_tuples:
        e2 = e[1], e[0]
        if e in pairs:
            pairs[e] += 1
        elif e2 in pairs:
            pairs[e2] += 1
        else:
            pairs[e] = 1
    return pairs


def get_pairs(sentence, not_words_text, distance):
    list_of_pairs_in_sentence = []
    words = parse_words(sentence)
    not_words = set(parse_words(not_words_text))
    for i in range(len(words)):
            for j in range(i+1, distance+i+1):
                if j < len(words):
                    if words[i] not in not_words and words[j] not in not_words:
                        t = words[i], words[j]
                        list_of_pairs_in_sentence.append(t)
    return list_of_pairs_in_sentence


def parse_words(sentence):
    words = re.split(r'[^\w-]+', sentence)
    final_words = list(filter(lambda x: x, words))
    return final_words


def parse_sentences(text):
    i = 0
    sentence = ''
    sentences = []
    while i < len(text):
        if text[i] == '"':
            sentence += text[i]
            i += 1
            while text[i] != '"' and i < len(text):
                sentence += text[i]
                i += 1
        if text[i] in ('.', '!', '?') and i < len(text):
            sentences.append(sentence)
            sentence = ''
            i += 1
        if i < len(text):
            sentence += text[i]
            i += 1
    return sentences


def get_text(name, coding, casemapping):
    with open(name, encoding=coding) as file:
        if casemapping:
            return file.read().casefold()
        else:
            return file.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('encoding', action='store', type=str,
                        help='display type of encoding of a file')
    parser.add_argument('-c', action='store_true',
                        help='casemapping')
    parser.add_argument('most_frequent_pairs', type=int,
                        help='Number of most frequently used pairs')
    parser.add_argument('-f', nargs=1, metavar='filename', action='store',
                        help='filename of file with text is given')
    parser.add_argument('-w', nargs=1, metavar='incorrect_words',
                        action='store',
                        help='name of file with incorrect words', default=[[]])
    parser.add_argument('-d', nargs=1, metavar='distance',
                        action='store', default=[1], help='distance is given',
                        type=int)
    args = parser.parse_args()
    most_frequent_pairs = args.most_frequent_pairs
    if args.f:
        text = get_text(args.f[0], args.encoding, args.c)
    else:
        text = sys.stdin.read()
    if args.w:
        not_words_text = get_text(args.w[0], args.encoding, args.c)
    sentences = parse_sentences(text)
    pairs = get_counter_of_pairs(text, not_words_text, int(args.d[0]))
    c = pairs.most_common(most_frequent_pairs)
    for i in range(most_frequent_pairs):
        print (str(c[i][0][0]) + ' ' + str(c[i][0][1]) + ' : ' + str(c[i][1]))


if __name__ == '__main__':
    main()
