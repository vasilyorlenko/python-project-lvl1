"""brain-progression game logic."""

from random import randint, choice

from brain_games.game_loop import run_loop
from brain_games.settings import MIN, MAX

description = 'What number is missing in the progression?'


def get_arithmetic_progression(start, step, length=10):
    """
    Get arithmetic progression.

    Args:
        start: int, number from which progression begins
        step: int, progression step
        length: int, progression length

    Returns:
        progression(list of integers)
    """
    progression = []
    index = 0
    while index < length:
        progression.append(start + index * step)
        index += 1
    return progression


def get_game_data_progression():
    """
    Get game data for brain-progression game.

    Returns:
        question(str) and correct answer(str) as ordered pair
    """
    progression = get_arithmetic_progression(
        randint(MIN, MAX),
        randint(MIN, MAX),
    )
    number_to_mask = choice(progression)
    progression_masked = [
        '..' if num == number_to_mask else str(num) for num in progression
    ]

    question = ' '.join(progression_masked)
    answer = str(number_to_mask)

    return (question, answer)


def run():
    """Run game loop with brain-progression game data."""
    run_loop(description, get_game_data_progression)
