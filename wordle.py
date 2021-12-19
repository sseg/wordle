# wordle.py -- botfight harness for wordle


USAGE = '''\
This is a harness to write bots that play wordle.

See: https://www.powerlanguage.co.uk/wordle/

To play against the computer:

   $ python wordle.py human

To test a bot named "play" in "my-bot.py" against 1000 random words in
wordlist "sowpods5.txt":

   $ python wordle.py bot sowpods5.txt my-bot.play 1000
'''


import sys, importlib, hashlib, random


MAGIC = 'WORDLE'


g_random = None
def get_random():
    global g_random
    if None == g_random:
        g_random = random.Random(MAGIC)
    return g_random


def load_wordlist(fn):
    a = set()
    for i in open(fn).readlines():
        a.add(i[:-1])
    return a


def load_bot(s):
    fn, func = s.split('.')
    module = importlib.import_module(fn)
    bot = getattr(module, func)
    return bot


def get_play(bot, guess_num, secret_hash, last_guess, last_score):
    state = '%d\t%s\t%s\t%s' % (guess_num, secret_hash, last_guess, last_score)
    response = bot(state)
    return response


def calc_score(secret, guess, wordlist):
    if not guess in wordlist:
        return '0' * len(secret)
    a = []
    for i, ch in enumerate(secret):
        g = '-'
        if i < len(guess):
            g = guess[i]
        if g == ch:
            a.append('3')
        elif g in secret:
            a.append('2')
        else:
            a.append('1')
    return ''.join(a)


def play_word(bot, secret, wordlist):
    guess_num = 1
    guess = '-' * len(secret)
    score = calc_score(secret, guess, wordlist)
    secret_hash = hashlib.sha256((MAGIC + secret).encode()).hexdigest()[:7]
    while 1:
        guess = get_play(bot, guess_num, secret_hash, guess, score)
        score = calc_score(secret, guess, wordlist)
        sys.stdout.write('PLAY\t%d\t%s\t%s\t%s\t%s\n' % (guess_num, secret_hash, secret, guess, score))
        if guess == secret:
            return guess_num
        if guess_num == len(wordlist):
            return guess_num
        guess_num += 1


def play_bot(bot, wordlist, n):
    total_guesses = 0
    if 0 == n:
        count = len(wordlist)
    else:
        count = n
    wordlist_as_list = sorted(list(wordlist))
    for i in range(count):
        word = get_random().choice(wordlist_as_list)
        guesses = play_word(bot, word, wordlist)
        total_guesses += guesses
        i += 1
        sys.stdout.write('WORD\t%d\t%d\t%d\t%f\t%s\n' % (i, guesses, total_guesses, total_guesses / float(i), word))
    return total_guesses


def play_human(secret, wordlist):
    guess_num = 0
    guess = '-' * len(secret)
    while 1:
        score = calc_score(secret, guess, wordlist)
        sys.stdout.write('guess_num: %d, last_guess: %s, last_score: %s\n' % (guess_num, guess, score))
        sys.stdout.write('Your guess?\n')
        guess = sys.stdin.readline().strip()
        guess_num += 1
        if guess == secret:
            break
    sys.stdout.write('Congratulations! You solved it in %d guesses.\n' % guess_num)
    return guess_num


def main(argv):
    if 0 == len(argv):
        print(USAGE)
        sys.exit()
    c = argv[0]
    if 0:
        pass
    elif 'human' == c:
        if 1 < len(argv):
            wordlist = load_wordlist(argv[1])
        else:
            wordlist = load_wordlist('sowpods_5s.txt')
        secret = get_random().choice(list(wordlist))
        if 2 == len(argv):
            secret = argv[2]
        x = play_human(secret, wordlist)
        return x
    elif 'help' == c:
        print(USAGE)
        sys.exit()
    elif 'score' == c:
        wordlist = load_wordlist(argv[1])
        secret = argv[2]
        guess = argv[3]
        x = calc_score(secret, guess, wordlist)
        print(x)
    elif 'bot' == c:
        fn_wordlist = argv[1]
        bot = load_bot(argv[2])
        n = 0
        if 4 == len(argv):
            n = int(argv[3])
        wordlist = load_wordlist(fn_wordlist)
        x = play_bot(bot, wordlist, n)
        return x
    else:
        print(USAGE)
        sys.exit()


if __name__ == '__main__':
    x = main(sys.argv[1:])
    sys.exit(x)


