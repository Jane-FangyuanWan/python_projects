# Fangyuan Wan
# A dodgeball team management system

class Bench:
    """
    A class representing a sidelines bench
    """
    def __init__(self):
        self.players_on_bench = []

    def send_to_bench(self, player_name):
        self.players_on_bench.append(player_name)

    def get_from_bench(self):
        if self.players_on_bench:
            return self.players_on_bench.pop(0)
        return None

    def display_bench(self):
        if self.players_on_bench:
            print("The bench currently includes:")
            for player in reversed(self.players_on_bench):
                print(player)
        else:
            print("The bench is empty.")
