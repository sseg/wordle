wordle
======

This is a harness to write bots that play wordle.

See:

https://www.powerlanguage.co.uk/wordle/

To play against the computer:

```
$ python wordle.py human
```

To test a bot named `play` in `my-bot.py` against the word "apple":

```
$ python wordle.py word apple my-bot.play
```

To test your bot against a wordlist:

```
$ python wordle.py wordlist wordlist.txt my-bot.play
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
$ python wordle.py wordlist sowpods-sample-5s.txt bot-random-word.play | grep WORD | tail
WORD	80	16662	708084	8851.050000	toyos
WORD	81	10504	718588	8871.456790	tufas
WORD	82	9654	728242	8881.000000	umped
WORD	83	10280	738522	8897.855422	vacua
WORD	84	24327	762849	9081.535714	vines
WORD	85	2512	765361	9004.247059	walls
WORD	86	1078	766439	8912.081395	whews
WORD	87	28879	795318	9141.586207	wodge
WORD	88	11686	807004	9170.500000	yauds
WORD	89	515	807519	9073.247191	zetas
```

Here ```bot-random-word``` solved 89 words in 807519 guesses for an average of 9073.2
guesses per word. Can you do better?

