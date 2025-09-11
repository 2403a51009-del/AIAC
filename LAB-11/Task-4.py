class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node with the given data into the BST."""
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert(node.right, data)
        # If data == node.data, do not insert duplicates

    def search(self, data):
        """Return True if data is found in the BST, False otherwise."""
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def inorder_traversal(self):
        """Return a list of all elements in the BST in sorted order."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Inorder traversal:", bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]
    print("Search 40:", bst.search(40))  # True
    print("Search 100:", bst.search(100))  # False
