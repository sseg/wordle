# wordle.py -- botfight harness for wordle


USAGE = '''\
This is a harness to write bots that play wordle.

See: https://www.powerlanguage.co.uk/wordle/

to play against the computer:

   $ python wordle.py human

to test a bot named "play" in "my-bot.py" against the word "apple":

   $ python wordle.py word apple my-bot.play

to test your bot against a dictionary:

   $ python wordle.py wordlist wordlist.txt my-bot.play
'''


import sys, importlib, hashlib, random


MAGIC = 'WORDLE'


def load_wordlist(fn):
    a = []
    for i in open(fn).readlines():
        a.append(i[:-1])
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


def calc_score(secret, guess):
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


def play_word(bot, secret):
    guess_num = 0
    guess = '-' * len(secret)
    score = calc_score(secret, guess)
    secret_hash = hashlib.sha256((MAGIC + secret).encode()).hexdigest()[:7]
    while 1:
        guess = get_play(bot, guess_num, secret_hash, guess, score)
        sys.stdout.write('PLAY\t%d\t%s\t%s\t%s\t%s\n' % (guess_num, secret_hash, secret, guess, score))
        if guess == secret:
            return guess_num
        guess_num += 1


def play_wordlist(bot, wordlist):
    total_guesses = 0
    n = 0
    for word in wordlist:
        guesses = play_word(bot, word)
        total_guesses += guesses
        n += 1
        sys.stdout.write('WORD\t%d\t%d\t%d\t%f\t%s\n' % (n, guesses, total_guesses, total_guesses / float(n), word))
    return total_guesses


def play_human(secret):
    guess_num = 0
    guess = '-' * len(secret)
    while 1:
        score = calc_score(secret, guess)
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
        if 2 == len(argv):
            secret = argv[1]
        else:
            secret = random.choice(list(filter(lambda x: len(x) == 5 and len(set(list(x))) == 5, load_wordlist('sowpods.txt'))))
        x = play_human(secret)
        return x
    elif 'help' == c:
        print(USAGE)
        sys.exit()
    elif 'score' == c:
        secret = argv[1]
        guess = argv[2]
        x = calc_score(secret, guess)
        print(x)
    elif 'word' == c:
        secret = argv[1]
        bot = load_bot(argv[2])
        x = play_word(bot, secret)
        return x
    elif 'wordlist' == c:
        fn_wordlist = argv[1]
        bot = load_bot(argv[2])
        wordlist = load_wordlist(fn_wordlist)
        x = play_wordlist(bot, wordlist)
        return x
    else:
        print(USAGE)
        sys.exit()


if __name__ == '__main__':
    x = main(sys.argv[1:])
    sys.exit(x)


