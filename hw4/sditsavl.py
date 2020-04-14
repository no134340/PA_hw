"""
ZADATAK 4

SDITSAVL - AVL Tree [SPOJ]

Ideja:
    Pratiti broj prethodnika ubacivanog čvora i ažurirati
    broj prethodnika odgovarajućih čvorova koji se posećuju
    pri ubacivanju čvora u stablo. Kako se balansiranjem
    stabla nakon ubacivanja u stablo ne menja in-order
    redosled, ne menja se ni broj prethodnika, tako da nema
    potrebe za ažuriranjem broj pri rotacijama, tj. pri
    balansiranju stabla nakon ubacivanja elementa. Kada se
    zatraži redni broj čvora sa određenim ključem, izvršiti
    pretragu (logaritamska složenost) i samo očitati broj
    prethodnika (+1 pošto se traži indeksiranje od 1).

"""

class Node:

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.bf = 0
        self.pred_count = 0

    def __repr__(self):
        return str([self.key, self.data])

    def update_height(self):
        if self:
            hl, hr = -1, -1
            if self.left:
                hl = self.left.height
            if self.right:
                hr = self.right.height

            self.height = max(hl, hr) + 1

            self.bf = hr - hl

class AVL:

    def __init__(self):
        self.root = None
        self.number_of_elements = 0

    def insert(self, key, data=None):
        node = Node(key, data)
        self.number_of_elements += 1
        if self.root:
            curr = self.root
            p = self.root
            while curr:
                p = curr
                if curr.key > node.key:
                    curr.pred_count += 1
                    curr = curr.left
                else:
                    node.pred_count += curr.pred_count + 1
                    curr = curr.right
            node.parent = p
            if node.key > p.key:
                p.right = node
                node.pred_count += 1
            else:
                p.left = node
        else:
            self.root = node

        curr = node
        while curr:
            curr.update_height()
            self.balance(curr)
            self.root = curr
            curr = curr.parent

        return node

    def search(self, key):
        if self.root:
            node = self.root
            while node:
                if node.key > key:
                    node = node.left
                elif node.key < key:
                    node = node.right
                else:
                    break
            return node
        else:
            return None

    def rotate_left(self, node):
        b = node.right
        c = node.right.left

        if node.parent:
            if node.parent.right == node:
                node.parent.right = node.right
            else:
                node.parent.left = node.right
        b.parent = node.parent
        node.parent = b
        node.right = c

        if c:
            c.parent = node
        b.left = node

        node.update_height()
        b.update_height()

    def rotate_right(self, node):
        b = node.left
        c = node.left.right

        if node.parent:
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        b.parent = node.parent
        node.parent = b
        node.left = c
        if c:
            c.parent = node
        b.right = node

        node.update_height()
        b.update_height()

    def balance(self, node):
        if node.bf > 1:
            if node.right.bf < 0:
                self.rotate_right(node.right)
                node.update_height()
            self.rotate_left(node)
        if node.bf < -1:
            if node.left.bf < 0:
                self.rotate_left(node.left)
                node.update_height()
            self.rotate_right(node)



tree = AVL()
n = int(input())
for _ in range(n):
    command = input().split(" ")
    if command[0] == '1':
        tree.insert(int(command[1]))
    if command[0] == '2':
        ret = tree.search(int(command[1]))
        if not ret:
            print("Data tidak ada")
        else:
            print(ret.pred_count + 1)
