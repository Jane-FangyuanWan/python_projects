import re
import sys

def main():
    '''
    Count words, non-whitespace characters (including punctuation),
    and alphanumeric characters (letters and numbers, excluding punctuation)
    '''
    filename = input("Enter the file name: ")
    try:
        f = open(filename, "r", encoding="utf-8")
    except OSError as e:
        print(f"Can't open {filename}")
        sys.exit()

    text = f.read()
    words = len(text.split())
    characters = len(re.findall(r'[^\s]', text))
    letters_numbers = len(re.findall(r'\w', text))
    print(f"Words: {words}")
    print(f"Characters: {characters}")
    print(f"Letters & numbers: {letters_numbers}")


main()
