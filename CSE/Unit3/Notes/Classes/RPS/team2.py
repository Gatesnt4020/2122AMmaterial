"""The function move(my_history, their_history) must return "r", "p", or "s","l","i".
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random

strategy_name = "Random"   
                     
def move(my_history, their_history):
    pick = random.choice(["r", "p", "s","l","i"])
    return pick