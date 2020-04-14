"""
ZADATAK 3

TREEVERSE - Traversing Tree [SPOJ #30847]
"""


class Node:

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def inorder(self):
        if self.left:
            yield from self.left.inorder()

        yield self.key

        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        yield self.key

        if self.left:
            yield from self.left.preorder()

        if self.right:
            yield from self.right.preorder()

    def postorder(self):
        if self.left:
            yield from self.left.postorder()

        if self.right:
            yield from self.right.postorder()

        yield self.key


class BST:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root:
            curr = self.root
            p = self.root
            while curr:
                p = curr
                if curr.key > node.key:
                    curr = curr.left
                else:
                    curr = curr.right
            node.parent = p
            if node.key >= p.key:
                p.right = node
            else:
                p.left = node
        else:
            self.root = node

    def inorder(self):
        if self.root:
            yield from self.root.inorder()
        else:
            yield None

    def preorder(self):
        if self.root:
            yield from self.root.preorder()
        else:
            yield None

    def postorder(self):
        if self.root:
            yield from self.root.postorder()
        else:
            yield None


n = int(input())
chars = input().split(" ")
nums = [int(x) for x in chars]
tree = BST()
for x in nums:
    tree.insert(Node(x))
preorder = [x for x in tree.preorder()]
inorder = [x for x in tree.inorder()]
postorder = [x for x in tree.postorder()]
output = "Pre order :"
for x in preorder:
    output += f' {x}'
print(output)
output = "In order  :"
for x in inorder:
    output += f' {x}'
print(output)
output = "Post order:"
for x in postorder:
    output += f' {x}'
print(output)
