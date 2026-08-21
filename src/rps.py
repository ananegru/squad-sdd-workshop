#!/usr/bin/env python3
import random
import sys

VALID = {
    'rock': 'rock', 'r': 'rock',
    'paper': 'paper', 'p': 'paper',
    'scissors': 'scissors', 's': 'scissors'
}

WIN_MAP = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}


def prompt_move():
    while True:
        try:
            print("Choose [rock|paper|scissors] (or r/p/s):")
            raw = input().strip().lower()
        except EOFError:
            sys.exit(0)
        if raw in VALID:
            return VALID[raw]
        print("Invalid choice. Please enter rock, paper, or scissors (r/p/s).")


def prompt_play_again():
    while True:
        try:
            print("Play again? (y/n):")
            raw = input().strip().lower()
        except EOFError:
            sys.exit(0)
        if raw in ('y', 'yes'):
            return True
        if raw in ('n', 'no'):
            return False
        print("Invalid response. Enter y or n.")


def outcome(player, comp):
    if player == comp:
        return "Tie."
    if WIN_MAP[player] == comp:
        return "You win."
    return "You lose."


def main():
    you = 0
    computer = 0
    ties = 0
    while True:
        player = prompt_move()
        comp = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {comp}")
        res = outcome(player, comp)
        print(f"Result: {res}")
        # update counters
        if res == "You win.":
            you += 1
        elif res == "You lose.":
            computer += 1
        else:
            ties += 1
        # print exact score summary line
        print(f"Score - You: {you} Computer: {computer} Ties: {ties}")
        if not prompt_play_again():
            sys.exit(0)


if __name__ == '__main__':
    main()
