class HashTable:

    def __init__(self, m):
        self.table = [None] * m
        self.m = m
        self.cnt = 0
        self.max = 20

    def __repr__(self):
        table_string = ""
        for i in range(self.m):
            table_string += f"{i}:{self.table[i]}\n"
        return table_string

    def hsh(self, k, i):
        return int((self.h1(k) + i ** 2 + 23 * i) % self.m)

    def h1(self, k):
        pos = 0
        j = 1
        for char in k:
            pos += j * int(ord(char))
            j += 1
        pos *= 19
        return pos

    def insert(self, data):
        if self.cnt == self.m:
            return False
        possible = -1
        for i in range(0, self.max):
            pos = self.hsh(data, i)
            if (not self.table[pos] or self.table[pos] == -1) and possible == -1:
                possible = pos
            if self.table[pos] == data:
                return False
        if possible != -1:
            self.table[possible] = data
            self.cnt += 1
            return True
        return False

    def delete_elem(self, k):
        if k == "":
            self.table[0] = -1
            self.cnt -= 1
            return
        for i in range(0, self.max):
            pos = self.hsh(k, i)
            if not self.table[pos]:
                return False
            if self.table[pos] == -1:
                continue
            if self.table[pos] != k:
                continue
            self.table[pos] = -1
            self.cnt -= 1
            return True
        return False

    def print_table(self):
        print(self.cnt)
        i = 0
        for elem in self.table:
            if (elem and elem != -1) or elem == "":
                print(f"{i}:{elem}")
            i += 1


t = int(input())
for i in range(t):
    table = HashTable(101)
    n1 = int(input())
    for j in range(n1):
        data = input().split(":")
        if data[0] == "ADD":
            table.insert(data[1])
        elif data[0] == "DEL":
            table.delete_elem(data[1])
    table.print_table()
