#!/usr/bin/env python3
# file:brain_even.py
import brain_games.bg_module
my_module = brain_games.bg_module


def main():
    name_of_game = 'brain_calc'
    rules_of_game = 'What is the result of the expression?'
    my_module.begin_the_game(name_of_game, rules_of_game)


if __name__ == '__main__':
    main()
