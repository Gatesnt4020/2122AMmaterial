import random

strategy_name = "Thanks Landen"   
                     
def move(my_history, their_history):
    pick = random.choice(["r", "p", "s","l","i"])
    return pick