"""
You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop.
Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:



# Use the `next' attribute to get the following node
node.next
Notes:

do NOT mutate the nodes!
in some cases there can be just a loop, with no dangling piece.
Don't miss dmitry's article in the discussion after you pass the Kata !!
"""

def loop_size(node):
    tortoise = node.next if node else None
    hare = node.next.next if node and node.next else None
    while hare and hare != tortoise:
        tortoise = tortoise.next if tortoise else None
        hare = hare.next.next if hare and hare.next else None
    if not hare:
        return 0
    loop_start = tortoise
    current = loop_start.next
    length = 1
    while current != loop_start:
        length += 1
        current = current.next
    return length

# Teste

class Node:
    def __init__(self):
        self.next = None

nodes = [Node() for _ in range(15)]
for i in range(14):
    nodes[i].next = nodes[i+1]
nodes[14].next = nodes[2]

print(loop_size(nodes[0]))