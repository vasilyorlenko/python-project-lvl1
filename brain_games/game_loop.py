"""Loop logic common for every game in the package."""

import prompt

from brain_games import messages


def start_new_round(count, get_game_data, player_name):
    """
    Start a new round.

    Args:
        count: int, represents number of played rounds
        get_game_data: function, returns question and correct answer
        player_name: string, contains player's name

    Returns:
        True if player has won, False otherwise
    """
    if count == 3:
        print(messages.VICTORY.format(player_name))
        return True

    question, answer = get_game_data()
    print(messages.QUESTION.format(question))
    player_answer = prompt.string(messages.ANSWER_PROMPT)

    if player_answer != answer:
        print(messages.INCORRECT.format(player_answer, answer))
        print(messages.TRY_AGAIN.format(player_name))
        return False

    print(messages.CORRECT)
    return start_new_round(count + 1, get_game_data, player_name)


def run_loop(description, get_game_data):
    """
    Run game loop.

    Args:
        description: string, contains description of a game
        get_game_data: function, returns question and correct answer

    Returns:
        True if player has won, False otherwise
    """
    print(messages.WELCOME)
    player_name = prompt.string(messages.NAME_PROMPT)
    print(messages.HELLO.format(player_name))
    print(description)

    return start_new_round(0, get_game_data, player_name)
