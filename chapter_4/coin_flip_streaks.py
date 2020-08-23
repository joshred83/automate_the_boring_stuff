"""Coin Flip Streaks
====================================================================================================

For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H”
for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.”
If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail
 results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random.
 A human will almost never write down a streak of six heads or six tails in a row, even though it is
 highly likely to happen in truly random coin flips. Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a
randomly generated list of heads and tails. Your program breaks up the experiment into two parts:
the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part
checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000
times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a
row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1
value the other 50% of the time.

You can start with the following template:
"""
from random import choice


def flip_coin():
    return choice(['H', 'T'])


def flip_n(n: int) -> list:
    return [flip_coin() for _ in range(n)]


def count_streaks(coin_flips: list, streak_size=6) -> int:
    streaks = 0
    current_streak = 1
    for idx in range(1, len(coin_flips)):
        if coin_flips[idx] == coin_flips[idx - 1]:
            current_streak += 1
            if current_streak == 6:
                streaks += 1
        else:
            current_streak = 1
    return streaks


if __name__ == '__main__':

    TRIALS = 10000
    TRIAL_SIZE = 100
    successes = 0
    for idx in range(TRIALS):
        trial = flip_n(TRIAL_SIZE)

        if count_streaks(trial, streak_size=6) > 0:
            successes += 1

    print(f'Chance of streak: {(successes / TRIALS) *100:.2f}%.')
