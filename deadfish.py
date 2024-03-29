import pyfiglet
import hashlib
class Node():
    def __init__(self, num):
        self.num = num
        self.edges = []
        self.visited = False

nodes = [Node(i) for i in range(256)]

for i in range(1, 16):
    nodes[i].edges.append((nodes[i-1], 'd'))
    nodes[i].edges.append((nodes[i+1], 'i'))
    nodes[i].edges.append((nodes[i**2], 's'))

for i in range(16, 255):
    nodes[i].edges.append((nodes[i-1], 'd'))
    nodes[i].edges.append((nodes[i+1], 'i'))

nodes[0].edges.append((nodes[0], 'd'))
nodes[0].edges.append((nodes[1], 'i'))
nodes[255].edges.append((nodes[255], 'd'))
nodes[255].edges.append((nodes[0], 'i'))
nodes[16].edges.append((nodes[0], 's'))

DP = {}

def BFS(nodes, s, t):
    if (s, t) in DP:
        return DP[(s, t)] + 'o'

    for n in nodes:
        n.visited = False

    queue = [(nodes[s], '')]
    while queue:
        v, path = queue.pop(0)
        v.visited = True
        if v.num == t:
            DP[(s, t)] = path
            return path + 'o'
        
        for (node, c) in v.edges:
            if not node.visited:
                queue.append((node, path+c))
                DP[(s, node.num)] = path+c

# BFS(nodes[13], nodes[127])


def encode(s, start=0):
    """ Encodes input string s into deadfish """
    targets = [start] + [ord(c) for c in s]
    out = ""
    for i in range(len(s)):
        out += BFS(nodes, targets[i], targets[i+1])

    return out


def decode(s, accumulator=0):
    out = ""
    for cmd in s:
        if accumulator == 256 or accumulator == -1:
            # Overflow, reset accumulator
            accumulator = 0
        # Process input
        if cmd == 'i':
            accumulator += 1 # Increment
        elif cmd == 'd':
            accumulator += -1 # Decrement
        elif cmd == 'o':
            out += chr(accumulator) # Output
        elif cmd == 's':
            accumulator *= accumulator # Square

    return out, accumulator
kabi = pyfiglet.figlet_format("E-Med+ Deadfish Encoding")
print(kabi)
print("Username : ")
x = input("")
print("Password : ")
y = input("")
kabi = pyfiglet.figlet_format("Plain text Format")
print(kabi)
print("username : " + x)
print("Password : " +  y)
print("\n")
print("\n")
kabi = pyfiglet.figlet_format("MD5 Format")
print(kabi)
result = hashlib.md5(x.encode()) 
print("MD5 Encrypted Username : " + result.hexdigest()) 
result1 = hashlib.md5(y.encode()) 
print("MD5 Encrypted Password : " + result.hexdigest()) 
print("\n")
print("\n")
kabi = pyfiglet.figlet_format("DeadFish Encryption")
m= ""
n =""
m = result
n= result1
print(kabi)
text = encode(""" + m + """)
text1 = encode(""" + n + """)
print("Deadfish Encrypted Username : " + text)
print("Deadfish Encrypted Username : " + text1)

