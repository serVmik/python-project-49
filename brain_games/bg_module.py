# file:bg_module.py
import prompt
from random import randint


def greetings():
    print('Welcome to the Brain Games!')


def ask_player_name():
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name


def formulate_a_task():
    task = randint(1, 100)
    if task % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (task, correct_answer)


def display_the_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def ask_player_question(task):
    print(f'Qyestion: {task}')


def get_player_answer():
    return input('Your answer: ')


def display_test_result(player_answer, correct_answer, name):
    if player_answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{player_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")


def congratulate(name):
    print(f'Congratulations, {name}!')


def begin_the_game(name_of_game):
    count_of_questions = 3
    result_of_game = 'win'

    greetings()
    player_name = ask_player_name()
    display_the_rules()

    for _ in range(count_of_questions):
        task, correct_answer = formulate_a_task()
        ask_player_question(task)
        player_answer = get_player_answer()
        display_test_result(player_answer, correct_answer,
                            player_name)

        if player_answer != correct_answer:
            result_of_game = 'game over'
            break

    if result_of_game == 'win':
        congratulate(player_name)