from stack import Stack
import sys

sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically


class AnBnCn:
    """Class for evaluating strings of N a's followed by N b's"""
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        expect_a = True
        expect_b = True
        for ch in in_string:
            if ch == "a":
                if expect_a:
                    self.stack_1.push(ch)
                else:
                    return False
            elif ch == "b":
                if self.stack_1.is_empty():
                    return False
                else:
                    if expect_a:
                        expect_a = False
                        self.stack_1.pop()
                    else:
                        self.stack_1.pop()
            if ch == "b":
                if expect_b:
                    self.stack_2.push(ch)
                else:
                    return False
            elif ch == "c":
                if self.stack_2.is_empty():
                    return False
                else:
                    if expect_b:
                        expect_b = False
                        self.stack_2.pop()
                    else:
                        self.stack_2.pop()

        if self.stack_1.is_empty() and self.stack_2.is_empty():
            return True
        return False

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack_1 = Stack()
        self.stack_2 = Stack()
