def capitalize_vowel(input_string):
    # define vowels
    vowels = "AEIOUaeiou"
    # initialize an empty result string
    result = ""
    # loop through the input string
    for char in input_string:
        # check if the character is a vowel
        if char in vowels:
            # covert vowels to uppercase
            result += char.upper()
            # check if the charater is a letter:
        elif char.isalpha():
            # convert consonants to lowercase:
            result += char.lower()
            # keep non-alphabetic charaters unchanged:
        else:
            result += char
        # return the converted string
    return result


    # get user input and call the function:
user_input = input("Please enter a string: ")
capitalized_vowel = capitalize_vowel(user_input)
print("Capitalized vowels: ", capitalized_vowel)
