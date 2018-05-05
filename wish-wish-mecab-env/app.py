#!/usr/bin/env python
# -*- coding: utf-8 -*-

from natto import MeCab
from pykakasi import kakasi
import random

input_text = input()
kakasi = kakasi()


def tokenize(text):
    tokens = []
    with MeCab('-F%f[0],%f[6]') as nm:
        for n in nm.parse(text, as_nodes=True):
            # ignore any end-of-sentence nodes
            if not n.is_eos() and n.is_nor():
                klass, word = n.feature.split(',', 1)
                if klass in ['名詞', '形容詞', '形容動詞', '動詞', '副詞']:
                    tokens.append(word)
    return tokens


def get_initials(words):
    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')
    # kakasi.setMode("C", True)
    conv = kakasi.getConverter()
    initials = []

    for word in words:
        initial = conv.do(word)[:1].upper()
        initials.append(initial)

    # if initials.count == 0:
    #     print('Error: cannot get initial')
    #     return

    return initials


def shorten_initials(initials):
    if len(initials) == 0:
        print('Error: cannot get initial')
        return
    elif len(initials) <= 4:
        return initials
    elif len(initials) > 4:
        shortened_initials = [initials[0], initials[len(initials) - 1]]
        shortened_initials.extend(random.sample(initials[1:len(initials)-1], 2))

        return shortened_initials


if __name__ == '__main__':
    _words = tokenize(input_text)
    _initials = get_initials(_words)
    _shortened_initials = shorten_initials(_initials)
    print(_shortened_initials)
    print(''.join(_shortened_initials))
