# sample wordle bot, pick random words from word list


import random


g_random = None
g_wordlists = {}


def init():
    global g_random, g_wordlists
    g_random = random.Random('')
    for i in open('sowpods.txt').readlines():
        i = i[:-1]
        if not len(i) in g_wordlists:
            g_wordlists[len(i)] = []
        g_wordlists[len(i)].append(i)


def play(state):
    guess_num, secret_hash, last_guess, last_score = state.split()
    global g_random, g_wordlists
    return g_random.choice(g_wordlists[len(last_score)])


init()

