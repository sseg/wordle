# sample wordle-bots bot, just generate random words


import random


def play(state):
    guess_num, secret_hash, last_guess, last_score = state.split()
    s = ''
    for i in range(len(last_score)):
        s += random.choice('abcdefghijklmnopqrstuvwxyz')
    return s

