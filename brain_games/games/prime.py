"""brain-prime game logic."""

from random import randint

from brain_games.game_loop import run_loop
from brain_games.settings import MIN, MAX

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """
    Check if number is prime.

    Args:
        num: int

    Returns:
        True if num is prime, False otherwise
    """
    if num < 2:
        return False

    index = 2
    while index < num / 2:
        if num % index == 0:
            return False
        index += 1

    return True


def get_game_data_prime():
    """
    Get game data for brain-prime game.

    Returns:
        question(str) and correct answer(str) as ordered pair
    """
    rand_num = randint(MIN, MAX)

    question = str(rand_num)
    answer = 'yes' if is_prime(rand_num) else 'no'

    return (question, answer)


def run():
    """Run game loop with brain-prime game data."""
    run_loop(description, get_game_data_prime)
