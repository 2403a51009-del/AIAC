class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    def pop(self):
        """Remove and return the top item of the stack. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    def peek(self):
        """Return the top item of the stack without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0
# Example usage:
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top of stack:", stack.peek())        # 30
    print("Popped:", stack.pop())               # 30
    print("Top of stack after pop:", stack.peek())  # 20
    print("Is stack empty?", stack.is_empty())  # False
