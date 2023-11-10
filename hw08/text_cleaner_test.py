import pytest
from text_cleaner import TextCleaner


class TestCase:
    @pytest.mark.parametrize("text, expected_clean_text",
                             [("Hello, world", [["hello", "COMMA", "world"]]),
                              ("MR. H and MS. U. hi",
                               [["mr", "h", "and", "ms", "u"], ["hi"]])])
    def test_text_cleaner(self, text: str, expected_clean_text: list):
        """
        Test text cleaner.
        """
        assert TextCleaner.clean_text(text) == expected_clean_text
