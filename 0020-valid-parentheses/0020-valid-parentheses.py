class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.stack == []:
            return None
        return self.stack.pop()


class Solution:
    def __init__(self):
        self.stack = Stack()

    def isValid(self, s: str) -> bool:
        for char in s:
            if char in ['(', '[', '{']:
                self.stack.push(char)
            else:
                if self.stack.pop() != self.get_pair(char):
                    return False
        return len(self.stack.stack) == 0

    def get_pair(self, char):
        if char == ')':
            return '('
        if char == ']':
            return '['
        if char == '}':
            return '{'
        return None
    