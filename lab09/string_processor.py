from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self) -> None:
        pass

    def process_string(self, line):
        solution_string = []
        stack = Stack()
        for char in line:
            if char == "*":
                temp = stack.pop()
                solution_string.append(temp)
            if char == "^":
                temp = stack.pop()
                solution_string.append(temp)
                temp = stack.pop()
                solution_string.append(temp)
            else:
                stack.push(char)
        filtered_list = [item for item in solution_string if item is not None]
        solution_str = ''.join(filtered_list)
        return solution_str
