from queue import Queue
from stack import Stack
import string


class WordLadder:
    def __init__(self, w1, w2, wordlist):
        self.queue = Queue()
        self.wordlist = wordlist
        self.visited = set()  # To track visited words
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

            for i in range(len(current_word)):
                for letter in string.ascii_lowercase:
                    candidate = current_word[:i] + letter + current_word[i+1:]
                    if candidate == self.w2:
                        current_stack.push(candidate)
                        return current_stack
                    if candidate in self.wordlist and candidate not in\
                       self.visited:
                        new_stack = current_stack.copy()
                        new_stack.push(candidate)
                        self.queue.enqueue(new_stack)
                        self.visited.add(candidate)
        return None
