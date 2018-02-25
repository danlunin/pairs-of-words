#!/usr/bin/env python3

import pairs as t
import unittest
import collections


class MyTestCase(unittest.TestCase):
    def test_parse_sentences(self):
        text = ' Макмерфи снимает шапочку и запускает обе руки в рыжие во\
лосы. Теперь все смотрят на него: "ждут, как он ответит, и он понимает эт\
о". Чувствует, что попался в какую-то ловушку. Надевает шапку, трет швы \
на носу.'
        list_sentences = [" Макмерфи снимает шапочку и запускает обе руки \
в рыжие волосы",
                          ' Теперь все смотрят на него: "ждут, как он \
ответит, и он понимает это"',
                          " Чувствует, что попался в какую-то ловушку",
                          " Надевает шапку, трет швы на носу"]
        self.assertEqual(list_sentences, t.parse_sentences(text))

    def test_parse_words(self):
        sentence = 'Думаете, что сможете применить его против мисс \
Гнусен?'
        not_words = 'что, его'
        list_words = ['Думаете', 'что', 'сможете', 'применить', 'его',
                      'против', 'мисс', 'Гнусен']
        self.assertEqual(list_words, t.parse_words(sentence))

    def test_get_pairs(self):
        sentence = 'Думаете, что сможете применить его против мисс \
Гнусен?'
        not_words = 'что, его'
        distance = 2
        list_pairs = [('Думаете', 'сможете'), ('сможете', 'применить'),
                      ('применить', 'против'), ('против', 'мисс'),
                      ('против', 'Гнусен'), ('мисс', 'Гнусен')]
        self.assertEqual(list_pairs, t.get_pairs(sentence, not_words,
                                                 distance))

    def test_get_pairs2(self):
        sentence = 'Думаете, что сможете применить его против мисс \
Гнусен?'
        not_words = 'что, его'
        distance = 1
        list_pairs = [('сможете', 'применить'), ('против', 'мисс'),
                      ('мисс', 'Гнусен')]
        self.assertEqual(list_pairs, t.get_pairs(sentence, not_words,
                                                 distance))

    def test_get_pairs3(self):
        sentence = 'они направились, направились они'
        not_words = 'что, его'
        distance = 1
        list_pairs = [('они', 'направились'), ('направились',
                      'направились'),
                      ('направились', 'они')]
        self.assertEqual(list_pairs, t.get_pairs(sentence, not_words,
                                                 distance))

    def test_get_counter_of_pairs(self):
        text = 'они направились. направились они. они направились.'
        not_words = 'нему, Также, к'
        distance = 2
        counter = collections.Counter({('они', 'направились'): 3})
        self.assertEqual(counter, t.get_counter_of_pairs(text, not_words,
                                                         distance))

    def test_get_text_casemapping(self):
        filename = 'test_text1.txt'
        encoding = 'cp1251'
        text = 'мы вернулись домой.'
        self.assertEqual(text, t.get_text(filename, encoding, True))

    def test_get_text(self):
        filename = 'test_text1.txt'
        encoding = 'cp1251'
        text = 'Мы вернулись домой.'
        self.assertEqual(text, t.get_text(filename, encoding, False))

if __name__ == '__main__':
    unittest.main()
