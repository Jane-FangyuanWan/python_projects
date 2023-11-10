import sys
import os
from ngram_frequencies import NgramFrequencies


def main():
    file_name: str = sys.argv[1]
    file_path: str = os.getcwd() + "/" + file_name
    if not os.path.exists(file_path):
        print(f"File {file_name} not found.")
        exit(1)
    try:
        f = open(file_path, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Unable to open this file")
        exit(1)
    unigram = NgramFrequencies("unigram", file_path)
    bigram = NgramFrequencies("bigram", file_path)
    trigram = NgramFrequencies("trigram", file_path)
    n = 10
    top_10_unigram_frequencies = unigram.get_top_n_frequencies(n)
    top_10_bigram_frequencies = bigram.get_top_n_frequencies(n)
    top_10_trigram_frequencies = trigram.get_top_n_frequencies(n)
    print("Top 10 unigrams:")
    print_output(top_10_unigram_frequencies)
    print("Top 10 bigrams: ")
    print_output(top_10_bigram_frequencies)
    print("Top 10 trigrams: ")
    print_output(top_10_trigram_frequencies)


def print_output(collection: list):
    for item in collection:
        print(f"\t('{item[0]}', {round(item[1], 3)})")


main()
