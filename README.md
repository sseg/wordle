wordle
======

This is a harness to write bots that play wordle.

See:

https://www.powerlanguage.co.uk/wordle/

To play against the computer:

```
$ python wordle.py human
```

To test a bot named `play` in `my-bot.py` against 100 words in `sowpods_5s.txt`:

```
$ python wordle.py bot sowpods_5s.txt my-bot.play 100
```

To write a bot, write a function `play` in a python file that takes a
string `state`. `state` looks like:

```2 abcd123 adept 31221```

This is guess number `2`, the secret word (in this example it's "apple") has a
hash of `abcd123`, your last guess was `adept`, the first letter was correct
(indicated by a `3`), the third and fourth letters are in the wrong place (`2`),
and the second and fifth letters do not appear in the secret word (`1`).

To "score" your bot:

```
(venv) colins-air:wordle saunders$ python3 wordle.py bot sowpods.txt bot-random-word.play 10 | grep WORD
WORD	1	4947	4947	4947.000000	exactors
WORD	2	27187	32134	16067.000000	polestar
WORD	3	4211	36345	12115.000000	intermits
WORD	4	13036	49381	12345.250000	wormhole
WORD	5	34	49415	9883.000000	bimbo
WORD	6	6658	56073	9345.500000	laser
WORD	7	2496	58569	8367.000000	muchacho
WORD	8	52177	110746	13843.250000	miscarriage
WORD	9	28619	139365	15485.000000	trawlnets
WORD	10	5422	144787	14478.700000	nomograms
```

Here ```bot-random-word``` solved 10 words in 144787 guesses for an average of 14478.7
guesses per word. Can you do better?

