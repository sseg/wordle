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
$ python3 wordle.py bot sowpods\_5s.txt bot-3s.play 10 | grep WORD
WORD    1       30      30      30.000000       gushy
WORD    2       26      56      28.000000       steek
WORD    3       9       65      21.666667       mosks
WORD    4       17      82      20.500000       bourn
WORD    5       23      105     21.000000       okapi
WORD    6       18      123     20.500000       randy
WORD    7       16      139     19.857143       psoas
WORD    8       37      176     22.000000       rigor
WORD    9       27      203     22.555556       clung
WORD    10      42      245     24.500000       rawly
```

Here ```bot-3s``` solved 10 words in 245 guesses for an average of 24.5
guesses per word. Can you do better?

