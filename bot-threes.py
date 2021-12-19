# bot-3s.py -- pick a random starting word, then pick random words that match 3s


import random


g_random = random.Random('bot-3s')


g_wordlists = None
def get_wordlist(n):
    global g_wordlists
    if None == g_wordlists:
        g_wordlists = {}
        for i in open('sowpods.txt').readlines():
            i = i[:-1]
            if not len(i) in g_wordlists:
                g_wordlists[len(i)] = []
            g_wordlists[len(i)].append(i)
    return g_wordlists[n]


# this has lots of false positives, only pay attention to 3s
#
def could_match(target, last_guess, last_score):
    for i, ch in enumerate(last_score):
        if '3' == ch:
            if target[i] != last_guess[i]:
                return False
        else:
            if target[i] == last_guess[i]:
                return False
    return True


def play(state):
    guess_num, secret_hash, last_guess, last_score = state.split()
    possible = list(filter(lambda x: could_match(x, last_guess, last_score), get_wordlist(len(last_score))))
    return g_random.choice(possible)
