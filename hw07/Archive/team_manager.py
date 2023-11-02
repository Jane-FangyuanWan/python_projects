#Fangyuan Wan
#A dodgeball team management system


from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return 
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player_from_team(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    """
    Ensure team's name is made up of alphanumeric characters and spaces -- extra credit
    """
    name = input("What do you want to name the team?\n")
    while not name.replace(" ", "").isalnum():
        print("Please note team name should only contain alphanumeric characters and spaces.")
        name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    team.display_roster()


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    if team.is_position_filled(position):
        print(f"Yes, the {position} position is filled")
    else:
        print(f"No, the {position} position is not filled")


def do_add_player_to_team(team):
    """
    Ensure that the player's attributes is an actual numerical value - extra credit
    """
    player_name = input("What's the player's name?\n")
    while not player_name.isalpha() or not player_name.replace(" ", "").isalpha():
        print("Invalid name. Please enter a valid name with alphabetic characters and spaces only.")
        player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    while not player_number.isnumeric():
        print("Please input a vaild number for the player number.")
        player_number = input("What's " + player_name + "'s number?\n")
    valid_positions = ["catcher", "corner", "sniper", "thrower"]
    player_position = input("What's " + player_name + "'s position?\n")
    while player_position not in valid_positions:
        print("Invalid position. Please enter a valid position (catcher, corner, sniper, or thrower).")
        player_position = input("What's " + player_name + "'s position?\n")
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    if team.is_player_on_team(name):
        bench.send_to_bench(name)
    else:
        print(f"{name} isn't on the team")


def do_get_player_from_bench(bench):
    player = bench.get_from_bench()
    if player:
        print(f"Got {player} from bench")
    else:
        print("The bench is empty.")


def do_cut_player_from_team(team, bench):
    name = input("Who do you want to cut?\n")
    if team.cut_player(name):
        bench.get_from_bench()
    else:
        print(f"{name} isn't on the team.")


def do_show_bench(bench):
    bench.display_bench()

def do_not_understand():
    print("I didn't understand that command")

if __name__ == "__main__":
    main()
