class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_value(self, value):
        """Delete the first node with the specified value."""
        curr = self.head
        prev = None
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True  # Value found and deleted
            prev = curr
            curr = curr.next
        return False  # Value not found

    def traverse(self):
        """Return a list of all elements in the linked list."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(5)
    sll.insert_at_end(10)
    sll.insert_at_end(15)
    print("List after insertions:", sll.traverse())  # [5, 10, 15]
    sll.delete_value(10)
    print("List after deleting 10:", sll.traverse())  # [5, 15]
    sll.delete_value(5)
    print("List after deleting 5:", sll.traverse())  # [15]
    sll.delete_value(100)  # Value not in list
    print("List after trying to delete 100:", sll.traverse())  # [15]
