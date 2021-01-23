"""brain-even game logic."""

from random import randint

from brain_games.game_loop import run_loop
from brain_games.settings import MIN, MAX

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """
    Check if number is even.

    Args:
        number: int

    Returns:
        True or False
    """
    return number % 2 == 0


def get_game_data_even():
    """
    Get game data for brain-even game.

    Returns:
        ordered pair of question and answer
    """
    rand_num = randint(MIN, MAX)
    question = str(rand_num)
    answer = 'yes' if is_even(rand_num) else 'no'

    return (question, answer)


def run():
    """Run game loop with brain-even game data."""
    run_loop(description, get_game_data_even)
