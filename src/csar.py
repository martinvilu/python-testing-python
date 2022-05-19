#!/usr/bin/env python3

import string;

def cesar_encode(word, shift):
    encoded = ''
    letters = string.ascii_letters + string.punctuation + string.digits
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
    return encoded

def cesar_decode(word, shift):
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ''
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) - shift
            encoded = encoded + letters[x]
    return encoded


