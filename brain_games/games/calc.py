"""brain-calc game logic."""

from random import choice, randint

from brain_games.game_loop import run_loop
from brain_games.settings import MIN, MAX

description = 'What is the result of the expression?'
operations = {
    '+': lambda num_a, num_b: num_a + num_b,
    '-': lambda num_a, num_b: num_a - num_b,
    '*': lambda num_a, num_b: num_a * num_b,
}
operators = list(operations.keys())


def get_game_data_calc():
    """
    Get game data for brain-calc game.

    Returns:
        question and correct answer as ordered pair
    """
    rand_num_a = randint(MIN, MAX)
    rand_num_b = randint(MIN, MAX)
    random_operator = choice(operators)

    question = '{0} {1} {2}'.format(rand_num_a, random_operator, rand_num_b)
    answer = str(operations[random_operator](rand_num_a, rand_num_b))

    return (question, answer)


def run():
    """Run game loop with brain-calc game data."""
    run_loop(description, get_game_data_calc)
