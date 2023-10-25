# Fangyuan Wan
# Define the class for die

import random


class Die:
    """
    Represent a single die
    """
    def __init__(self):
        """
        Hold the face-up value of die
        """
        self.current_value = None

    def roll(self):
        """
        Rolling the dice
        """
        ONE = 1
        SIX = 6
        self.current_value = random.randint(ONE, SIX)
