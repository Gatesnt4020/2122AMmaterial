"""The function move(my_history, their_history) must return 'r', 'p', or 's','i','l'.
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random

strategy_name = "Beat last move if repeating"

def beat_move(move):
    if (move=="r"):
        return "p"
    if (move == "p"):
        return "s"
    if (move=="s"):
        return "r"
    if (move=="l"):
        return "s"
    if (move=="i"):
        return "p"

def move(my_history, their_history):
    """This player always starts with rock
    """
    if (len(their_history) < 2):
        return "r"
    if (their_history[-1] == their_history[-2]):
        return beat_move(their_history[-1])
    return random.choice(["r", "p", "s","l","i"])