from word_ladder import WordLadder
from word_ladder_app import load_words

# TODO: Write appropriate unit tests


def test_make_ladder():
    wordlist = load_words()
    wordlist = wordlist[4] if 4 in wordlist else set()
    wl = WordLadder("love", "hate", wordlist)
    result_stack = wl.make_ladder()
    result = [item for item in result_stack.items] if result_stack else None
    expected = ["love", "hove", "have", "hate"]
    assert result == expected, "Test failed"

    wordlist = load_words()
    wordlist = wordlist[5] if 5 in wordlist else set()
    wl = WordLadder("angel", "devil", wordlist)
    result_stack = wl.make_ladder()
    result = [item for item in result_stack.items] if result_stack else None
    expected = ["angel", "anger", "aeger", "leger", "lever", "level",
                "devel", "devil"]
    assert result == expected, "Test failed"


# Call the test functions
test_make_ladder()
