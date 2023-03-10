# file:game_progression.py
from random import randint

rules_of_game = 'What number is missing in the progression?'


def create_progression():
    first_number = randint(1, 20)
    step = randint(1, 10)
    length_of_progression = randint(5, 10)
    last_number = first_number + length_of_progression * step
    list_of_progression = [_ for _ in range(first_number, last_number, step)]

    return list_of_progression


def creat_task_and_answer(progression):
    position_of_hidden_element = randint(1, len(progression) - 1)
    hidden_element = progression[position_of_hidden_element]
    answer = str(hidden_element)

    task = ''
    progression[position_of_hidden_element] = '..'
    for element in progression:
        task += str(element) + ' '

    return task[:-1], answer


def formulate_task():
    progression = create_progression()
    task, correct_answer = creat_task_and_answer(progression)

    return task, correct_answer
