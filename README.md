wordle -- botfight harness for wordle game
==========================================

See:

https://www.powerlanguage.co.uk/wordle/

To play against the computer:

```
$ python wordle.py human
```

To test a bot named "play" in "my-bot.py" against the word "apple":

```
$ python wordle.py word apple my-bot.play
```

To test your bot against a dictionary:

```
$ python wordle.py wordlist wordlist.txt my-bot.play
```

To write a bot, write a function `play` in a python file that takes a
string `state`. `state` is a looks like this:

```2 abcd123 adept 31221```

This is guess #2, the secret word has a hash of `abcd123`, your last guess was
`adept`, the first letter was correct, the third and fourth letters are in the
wrong place (the secret was "apple").

