"""CLI for brain-games package."""


import prompt


def welcome_user():
    """Welcomes user, asks his name."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
