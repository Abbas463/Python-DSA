class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them
node1.next = node2
node2.next = node3

# Head points to first node
head = node1
print(head.data)  # 10