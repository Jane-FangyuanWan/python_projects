# Fangyuan Wan
# A dodgeball team management system

from player import Player


class Team:
    """
    A class representing a dodgeball team
    """
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return True
        print(f"{player_name} isn't on the team")
        return False

    def is_position_filled(self, position):
        for player in self.players:
            if player.position == position:
                return True
        return False

    def is_player_on_team(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return True
        return False

    def display_roster(self):
        print(f"The lineup for {self.name} is:")
        if not self.players:
            print("The team currently has no players")
        else:
            for player in self.players:
                print(f"{player.number}\t{player.name}\t\t{player.position}")
