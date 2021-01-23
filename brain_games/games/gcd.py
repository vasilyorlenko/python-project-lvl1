"""brain-gcd game logic."""

from math import gcd
from random import randint

from brain_games.game_loop import run_loop
from brain_games.settings import MIN, MAX

description = 'Find the greatest common divisor of given numbers.'


def get_game_data_gcd():
    """
    Get game data for brain-gcd game.

    Returns:
        question(str) and correct answer(str) as ordered pair
    """
    num_a = randint(MIN, MAX)
    num_b = randint(MIN, MAX)

    question = '{0} {1}'.format(num_a, num_b)
    answer = str(gcd(num_a, num_b))

    return (question, answer)


def run():
    """Run game loop with brain-gcd game data."""
    run_loop(description, get_game_data_gcd)
