# Fangyuan Wan
# Defind class to roll pair of dice


from die import Die


class PairOfDice:
    """
    Represent a pair of dice
    """
    def __init__(self):
        """
        The constructor initializes the PairOfDice object and
        create two "Die" objects
        """
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        """
        Rolling both dice, calling their roll method for each die
        updating their current_value attributes
        """
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        return self.die1.current_value + self.die2.current_value
