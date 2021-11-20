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
$ python wordle.py wordlist sowpods-sample.txt bot-random-word.play | grep WORD | tail
WORD	17	4770	393284	23134.352941	nasalizations
WORD	18	68531	461815	25656.388889	nasalize
WORD	19	24740	486555	25608.157895	nasalized
WORD	20	163797	650352	32517.600000	oxazines
WORD	21	31946	682298	32490.380952	pranksters
WORD	22	10306	692604	31482.000000	refurbishment
WORD	23	8152	700756	30467.652174	secaloses
WORD	24	32534	733290	30553.750000	stapedes
WORD	25	1266	734556	29382.240000	thud
WORD	26	9545	744101	28619.269231	uprouses
```

Here ```bot-random-word``` solved 26 words in 744101 guesses for an average of 28619.3
guesses per word. Can you do better?

