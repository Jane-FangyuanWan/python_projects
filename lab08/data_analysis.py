# Fangyuan Wan
# Use dictionaries to collect statistics


import re
from collections import defaultdict


class DataAnalysis:

    def __init__(self, file):
        """
        Initialize instance variables
        """
        self.languages = defaultdict(int)
        self.country_tlds = defaultdict(int)
        self.row_count = 0
        self.read_data(file)

    def read_data(self, file_name):
        """
        Read data from the CSV file and update counts
        """
        THREE = 3
        SIX = 6
        with open(file_name, 'r') as csvfile:
            for row in csvfile.readlines()[1:]:
                email = row.rstrip().split(",")[THREE]
                res = re.search(r'\.([a-zA-Z]{2})$', email)
                country_tld = res.group(1) if res else None
                if country_tld:
                    self.country_tlds[country_tld] = 1 + \
                        self.country_tlds.get(country_tld, 0)
                language = row.rstrip().split(",")[SIX]
                self.languages[language] = 1 + self.languages.get(language, 0)
                self.row_count += 1

    def top_n_lang_freqs(self, N):
        """
        Return the top N languages by frequency
        """
        sorted_langs = sorted(self.languages.items(),
                              key=lambda x: x[1], reverse=True)
        normalized_langs = [(lang, count / self.row_count) for
                            lang, count in sorted_langs]
        return normalized_langs[:N]

    def top_n_country_tlds_freqs(self, N):
        """
        Return the top N country TLDs by frequency
        """
        sorted_tlds = sorted(self.country_tlds.items(),
                             key=lambda x: x[1], reverse=True)
        normalized_tlds = [(tld, count / self.row_count) for
                           tld, count in sorted_tlds]
        return normalized_tlds[:N]
