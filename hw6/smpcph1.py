"""
SPOJ PORBLEM SMPCPH1
"""
def encode(line):
    encoded = []
    for char in line:
        c = ord(char)
        for j in range(len(letters)):
            if char == letters[j]:
                c = ord(letters[(j + 1) % (len(letters))])
        encoded.append(chr(c))
    return encoded

input()
letters = input()
n = int(input())
for i in range(n):
    line = input()
    encoded = encode(line)
    print("".join(encoded))