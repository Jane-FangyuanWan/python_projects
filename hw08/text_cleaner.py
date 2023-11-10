import re


class TextCleaner:
    @staticmethod
    def clean_text(line: str):
        lower_line: str = line.lower()
        re_period: str = r"(?<=(mr|dr|ms))\."
        re_characters: str = r"[^\s\w.']"
        re_comma: str = lower_line.replace(",", " COMMA")
        split_words: list = []
        re_unne_period = re.sub(re_period,
                                "",
                                re_comma)
        clean_line: str = re.sub(re_characters,
                                 "",
                                 re_unne_period)
        split_sentence: list = clean_line.split(".")
        for sentence in split_sentence:
            words = sentence.split()
            split_words.append(words)
        return split_words
