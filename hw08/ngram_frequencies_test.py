# Fangyuan Wan
# To test the ngram frequencies

from ngram_frequencies import NgramFrequencies
import pytest


class TestCase:
    """
    To test the ngram frequencies
    """
    FILE_PATH = "./corpse_bride.txt"

    @pytest.mark.parametrize("ngram_name, expected_stop_index",
                             [("unigram", 0),
                              ("bigram", 1),
                              ("trigram", 3)])
    def test_stop_collect_index(
            self,
            ngram_name: str,
            expected_stop_index: int):
        assert NgramFrequencies(
            ngram_name,
            TestCase.FILE_PATH).stop_collect_index() == expected_stop_index

    @pytest.mark.parametrize("ngram_name, expected_word_formula",
                             [("unigram", "hi"),
                              ("bigram", "hi_happy"),
                              ("trigram", "hi_happy_world")])
    def test_manage_ngrams_word_formula(
            self,
            ngram_name: str,
            expected_word_formula: str):
        sentence = ["hi", "happy", "world"]
        index = 0
        assert NgramFrequencies(
            ngram_name,
            TestCase.FILE_PATH).manage_ngrams_word_formula(
            sentence,
            index) == expected_word_formula

    @pytest.mark.parametrize("ngram_name, expected_total_count",
                             [("unigram", 516),
                              ("bigram", 501),
                              ("trigram", 471)])
    def test_get_ngram_dict_total_count(
            self,
            ngram_name: str,
            expected_total_count: int):
        ngram = NgramFrequencies(ngram_name, TestCase.FILE_PATH)
        ngram.manage_ngrams()
        assert ngram.get_ngram_dict_total_count() == expected_total_count

    @pytest.mark.parametrize(
        "ngram_name, n, expected_list", [
            ("unigram", 2, [('the', 0.08914728682170543),
                            ('COMMA', 0.06976744186046512)]),
            ("bigram", 2, [('COMMA_the', 0.015968063872255488),
                           ('in_the', 0.00998003992015968)]),
            ("trigram", 2, [('the_world_of', 0.004246284501061571),
                            ('mr_burton_and', 0.004246284501061571)])])
    def test_top_n_frequencies(
            self,
            ngram_name: str,
            n: int,
            expected_list: list):
        assert NgramFrequencies(
            ngram_name,
            TestCase.FILE_PATH).get_top_n_frequencies(n) == expected_list

    @pytest.mark.parametrize("ngram_name, n, expected_list", [
        ("unigram", 2, [('the', 92), ('COMMA', 72)]),
        ("bigram", 2, [('COMMA_the', 16), ('in_the', 10)]),
        ("trigram", 2, [('the_world_of', 4),
                        ('mr_burton_and', 4)])])
    def test_top_n_count(self,
                         ngram_name: str,
                         n: int,
                         expected_list: list):
        ngram = NgramFrequencies(ngram_name, TestCase.FILE_PATH)
        # Initialized the ngram dict.
        ngram.manage_ngrams()
        assert ngram.top_n_count(n) == expected_list

    @pytest.mark.parametrize("ngram_name, item, expected_frequency",
                             [("unigram", 'and', 0.03875968992248062),
                              ("bigram", 'COMMA and', 0.007984031936127744),
                              ("trigram",
                               'the land of',
                               0.004246284501061571)])
    def test_get_frequency(self,
                           ngram_name: str,
                           item: str,
                           expected_frequency: float):
        assert NgramFrequencies(ngram_name, TestCase.FILE_PATH).frequency(
            item) == expected_frequency

    @pytest.mark.parametrize("ngram_name, item, expected_dict",
                             [("unigram", "hello", {"hello": 1}),
                              ("bigram", "hello_world", {"hello_world": 1}),
                              ("trigram", "hello_h_u", {"hello_h_u": 1})])
    def test_add_item(self, ngram_name: str, item: str, expected_dict: dict):
        ngram_freq = NgramFrequencies(ngram_name, TestCase.FILE_PATH)
        ngram_freq.add_item_to_ngram_dict(item)
        assert ngram_freq._NgramFrequencies__ngram_dict == expected_dict
