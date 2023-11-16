from ec_queue import Queue
from ec_stack import Stack
import string


class WordLadder:
    def __init__(self, w1, w2, wordlist):
        self.queue = Queue()
        self.wordlist = wordlist
        self.visited = set()  # Track visited words to avoid repetition
        self.w1 = w1
        self.w2 = w2

    def make_ladder(self):
        initial_stack = Stack()
        initial_stack.push(self.w1)
        self.queue.enqueue(initial_stack)
        self.visited.add(self.w1)

        while not self.queue.isEmpty():
            current_stack = self.queue.dequeue()
            current_word = current_stack.peek()

            for next_word in self.generate_candidates(current_word):
                if next_word not in self.visited and next_word in \
                        self.wordlist:
                    if next_word == self.w2:
                        current_stack.push(next_word)
                        return current_stack
                    new_stack = current_stack.copy()
                    new_stack.push(next_word)
                    self.queue.enqueue(new_stack)
                    self.visited.add(next_word)

        return None  # No ladder found if the queue is empty

    def generate_candidates(self, word):
        # Insertion and replacement
        for i in range(len(word) + 1):
            for letter in string.ascii_lowercase:
                # Insert a letter (considering word length constraint)
                if len(word) < len(self.w2):
                    yield word[:i] + letter + word[i:]

                # Replace a letter
                if i < len(word):
                    yield word[:i] + letter + word[i+1:]

        # Deletion (only if current word length is greater than
        # target word length)
        if len(word) > len(self.w2):
            for i in range(len(word)):
                yield word[:i] + word[i+1:]
