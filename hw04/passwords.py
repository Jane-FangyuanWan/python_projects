import random


LAST_NAME_MIN_LEN = 7
RANDOM_NUMBER_MIN = 0
RANDOM_NUMBER_MAX = 99


def generate_random_num():
    '''
    Return a random number
    '''
    return str(
        random.randrange(
            RANDOM_NUMBER_MIN,
            RANDOM_NUMBER_MAX))


def add_last_name_with_asterisks(last_name: str) -> str:
    '''
    Add asterisks to the last name when the length is less than 7.
    '''
    last_name_with_asterisks: str = last_name
    if len(last_name) < LAST_NAME_MIN_LEN:
        last_name_with_asterisks = last_name + \
            "*" * (
                LAST_NAME_MIN_LEN -
                len(last_name)
            )
    return last_name_with_asterisks


def generate_username(first_name: str, last_name: str) -> str:
    '''
    Generate a username 
    '''
    random_number: str = generate_random_num()
    username: str = first_name[0] + last_name[0:6] + random_number
    return username


def generate_password01(first_name: str, last_name: str) -> str:
    '''
    Generate password01
    '''
    random_number: str = generate_random_num()
    translate_table = str.maketrans("acolsi", "@(01$!")
    password01: str = first_name + random_number + last_name
    rewrite_password01: str = password01.lower().translate(translate_table)
    return rewrite_password01


def generate_password02(
        first_name: str,
        last_name: str,
        favorite_word: str) -> str:
    '''
    Generate password02
    '''
    return ''.join(map(
        lambda i: i[0].lower() + i[-1].upper(),
        [first_name, last_name, favorite_word])
    )


def generate_password03(
        first_name: str,
        last_name: str,
        favorite_word: str) -> str:
    '''
    Generate password03
    '''
    return ''.join(map(
        lambda i: i[: random.randrange(RANDOM_NUMBER_MIN, len(i))],
        [first_name, last_name, favorite_word]
    ))


def main():
    '''
    Take inputs and generate faux user names and suggested passwords
    '''
    # Print the welcome line and
    # get first name, last name and favorite word from user.
    print("Welcome to the username and password generator!")
    first_name: str = input("Please enter your first name: ")
    last_name: str = input("Please enter your last name: ")
    favorite_word: str = input("Please enter your favorite word: ")
    last_name_with_asterisks: str = add_last_name_with_asterisks(last_name)
    username: str = generate_username(first_name, last_name_with_asterisks)
    print(f"\nThanks {first_name}, your user name is {username}\n")
    password01: str = generate_password01(first_name, last_name)
    password02: str = generate_password02(
        first_name, last_name, favorite_word)
    password03: str = generate_password03(
        first_name, last_name, favorite_word)
    print("Here are three suggested passwords for you to consider:\n")
    print(f"Password 1: {password01}")
    print(f"Password 2: {password02}")
    print(f"Password 3: {password03}")


main()
