# Fangyuan Wan
# Create a class for Ngram frequencies


from text_cleaner import TextCleaner


class NgramFrequencies:
    """
    Create a class for Ngram frequencies
    """
    NGRAM_LIMIT_INDEX_STOP: dict = {"unigram": 0,
                                    "bigram": 1,
                                    "trigram": 3}

    def __init__(self, ngram: str, file_path: str):
        self.ngram: str = ngram
        self.file_path: str = file_path
        self.__ngram_dict: dict = {}

    def manage_ngrams(self):
        ngram_stop_collect_index: int = self.stop_collect_index()
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                clean_text: list = TextCleaner.clean_text(line)
                for sentence in clean_text:
                    for word_index in range(len(sentence) -
                                            ngram_stop_collect_index):
                        ngram_word = self.manage_ngrams_word_formula(
                            sentence, word_index)
                        self.add_item_to_ngram_dict(ngram_word)

    def stop_collect_index(self):
        return NgramFrequencies.NGRAM_LIMIT_INDEX_STOP[self.ngram]

    def manage_ngrams_word_formula(self, sentence: list, word_index: int):
        ngram_word: str | None = None
        if self.ngram == "unigram":
            ngram_word = sentence[word_index]
        elif self.ngram == "bigram":
            ngram_word = sentence[word_index] + "_" + sentence[word_index + 1]
        elif self.ngram == "trigram":
            ngram_word = (sentence[word_index] +
                          "_" + sentence[word_index + 1] +
                          "_" + sentence[word_index + 2])
        return ngram_word

    def add_item_to_ngram_dict(self, ngram_word: str,):
        if ngram_word in self.__ngram_dict.keys():
            self.__ngram_dict[ngram_word] += 1
        else:
            self.__ngram_dict[ngram_word] = 1

    def get_ngram_dict_total_count(self):
        total_count: int = 0
        for key in self.__ngram_dict.keys():
            count_value = self.__ngram_dict[key]
            total_count += count_value
        return total_count

    def top_n_count(self, n: int):
        self.manage_ngrams()
        ordered_count_list: list = sorted(
            self.__ngram_dict.items(),
            key=lambda x: x[1],
            reverse=True)
        return ordered_count_list[:n]

    def get_top_n_frequencies(self, n=None):
        self.manage_ngrams()
        ngram_dict_total_count: int = self.get_ngram_dict_total_count()
        unordered_dict_frequencies: dict = {}
        for key in self.__ngram_dict.keys():
            unordered_dict_frequencies[key] = self.__ngram_dict[key] / \
                ngram_dict_total_count
        ordered_dict_frequencies: list = sorted(
            unordered_dict_frequencies.items(),
            key=lambda x: x[1],
            reverse=True)
        return ordered_dict_frequencies[:n]

    def frequency(self, item: str):
        converted_item = item.replace(" ", "_")
        ngram_frequencies = self.get_top_n_frequencies()
        for frequency in ngram_frequencies:
            if converted_item == frequency[0]:
                return frequency[1]
        return "There is no such item"
