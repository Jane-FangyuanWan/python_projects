# Fangyuan Wan
# Game controller for dice game


from pair_of_dice import PairOfDice


class GameController:
    """
    Manage the game rules, scoring, and user interaction
    """
    def __init__(self):
        self.pair_of_dice = PairOfDice()
        self.point = []

    def start_game(self):
        print("--------------------------------")
        print("Welcome to street craps!\n")
        print("Rules:")
        print("If you roll 7 or 11 on your first roll, you win.")
        print("If you roll 2, 3, or 12 on your first roll, you lose.")
        print("If you roll anything else, that's your 'point', "
              + "and you keep rolling until you either roll your "
              + "point again (win) or roll a 7 (lose)\n")
        input("Please enter to roll the dice...\n")

        self.pair_of_dice.roll_dice()
        first_roll = self.pair_of_dice.current_value()

        SEVEN = 7
        ELEVEN = 11
        TWO = 2
        THREE = 3
        TWELVE = 12
        if first_roll in [SEVEN, ELEVEN]:
            print(f"You rolled {first_roll}. You win!")
        elif first_roll in [TWO, THREE, TWELVE]:
            print(f"You rolled {first_roll}. You lose.")
        else:
            self.point.append(first_roll)
            print(f"Your point is {first_roll}")
            self.continue_game()

    def continue_game(self):
        SEVEN = 7
        check = True
        while check:
            input("Press enter to roll the dice...\n")
            self.pair_of_dice.roll_dice()
            roll_value = self.pair_of_dice.current_value()
            if roll_value in self.point:
                print(f"You rolled {roll_value}. You win!")
                check = False
            elif roll_value == SEVEN:
                print(f"You rolled {roll_value}. You lose.")
                check = False
            else:
                print(f"Your point is {roll_value}")
                self.point.append(roll_value)
